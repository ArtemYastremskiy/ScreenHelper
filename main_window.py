import wolframalpha, easyocr #venv\Scripts\activate

from deep_translator import GoogleTranslator
from selenium import webdriver

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSettings, Slot

from ui_main import Ui_MainWindow
from screenshot_window import ScreenshotWidget
from settings_window import SettingsWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.settings = QSettings('config.ini', QSettings.IniFormat)
        self.ui.btn_settings.clicked.connect(self.open_settings_window)

        self.ui.btn_help.clicked.connect(self.open_github)

        self.ui.btn_select_area.clicked.connect(self.select_area)
        self.ui.btn_send_request.clicked.connect(self.send_request)

        self.wolfram = wolframalpha.Client(self.settings.value('apikeys/wolfram'))
        self.translator = GoogleTranslator(source='auto', target=self.settings.value('translation/target_languege'))

        self.output = None
    

    def open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()
    

    def open_github(self):
        driver = webdriver.Firefox()
        driver.get("https://github.com/ArtemYastremskiy/ScreenHelper#readme")


    @Slot()
    def select_area(self):
        self.hide()
        self.screenshot_window = ScreenshotWidget()
        self.screenshot_window.closed.connect(self.recognize_screenshot_data)
        self.screenshot_window.showFullScreen()


    def recognize_screenshot_data(self, fpath='screenshot.png'):
            self.show()

            reader = easyocr.Reader(lang_list=["ru","rs_cyrillic","be","bg","uk","mn","en"])
            result = reader.readtext(fpath, detail=0, paragraph=True)
            
            if result:
                self.ui.textEdit.setText(''.join(result).replace(':', '.').replace(';', ','))
            
            return result
    

    def send_request(self):
        query = self.ui.textEdit.toPlainText()
        rq_type = self.ui.cb_select_type.currentText()
        
        if query:
            if rq_type == 'Llama-3':
                if not self.settings.value('apikeys/llama3'):
                    self.output = 'Please set API key for Wolfram Alpha in settings to use it inside this app'

            elif rq_type == 'Wolfram Alpha':
                if not self.settings.value('apikeys/wolfram'):
                    self.output = 'Please set API keyfor Wolfram Alpha in settings to use it inside this app'
                else:
                    res = self.wolfram.query(query)
                    self.output = next(res.results).text

            elif rq_type == 'Google translate':
                self.output = self.translator.translate(query)

            elif rq_type == 'Google search':
                driver = webdriver.Firefox()
                driver.get(f"https://www.google.com/search?q={'+'.join(query.split(' '))}")
            
            if self.settings.value('translation/autotranslate') and rq_type != 'Google translate' and self.output:
                self.output = self.translator.translate(self.output)

            self.ui.tb_result.setText(self.output)

        else:
            self.ui.tb_result.setText("Input is empty")
