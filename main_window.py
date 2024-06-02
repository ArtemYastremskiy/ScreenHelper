import json, wolframalpha, easyocr #venv\Scripts\activate

from deep_translator import GoogleTranslator
from groq import Groq

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Slot

from ui_main import Ui_MainWindow
from screenshot_window import ScreenshotWidget
from settings_window import SettingsWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open('settings.json') as f:
            self.settings = json.load(f)

        self.ui.btn_settings.clicked.connect(self.open_settings_window)

        self.ui.btn_select_area.clicked.connect(self.select_area)
        self.ui.btn_send_request.clicked.connect(self.send_request)

        self.wolfram = wolframalpha.Client(self.settings["API_keys"]["wolfram"])
        self.translator = GoogleTranslator(source='auto', target=self.settings["General"]["Translation"]['target_languege'])

        self.output = None
    

    def open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

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

        if self.ui.cb_select_type.currentText() == 'Llama-3':
            print(self.settings["API_keys"]["llama3"])
            


        elif self.ui.cb_select_type.currentText() == 'Wolfram Alpha':
            res = self.wolfram.query(query)
            self.output = next(res.results).text

        elif self.ui.cb_select_type.currentText() == 'Google translate':
            self.output = self.translator.translate(query)

        
        if self.settings["General"]["Translation"]["autotranslate"] and self.ui.cb_select_type.currentText() != 'Google translate':
           self.output = self.translator.translate(self.output)
        
        self.ui.tb_result.setText(self.output)
