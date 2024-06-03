import json

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSettings

from ui_settings import Ui_Settings


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)

        with open('supported_languges.json') as f:
            self.supported_langueges = json.load(f)
        

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.settings = QSettings('config.ini', QSettings.IniFormat)

        self.load_settings()

        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_cancel.clicked.connect(self.cancel)
    
    def load_settings(self):
        self.ui.lineEdit_llama3.setText(self.settings.value('apikeys/llama3'))
        self.ui.lineEdit_wolfram.setText(self.settings.value('apikeys/wolfram'))

        self.ui.cb_target_lang.setCurrentText(self.settings.value('translation/target_languege'))
        self.ui.checkbox_autotranslate.setChecked(bool(self.settings.value('translation/autotranslate')))
    

    def apply(self):
        self.settings.setValue('apikeys/llama3', self.ui.lineEdit_llama3.text())
        self.settings.setValue('apikeys/wolfram', self.ui.lineEdit_wolfram.text())

        self.settings.setValue('translation/target_languege', self.supported_langueges[self.ui.cb_target_lang.currentText().lower()])
        self.settings.setValue('translation/autotranslate', self.ui.checkbox_autotranslate.isChecked())


    def save(self):
        self.apply()
        self.close()


    def cancel(self):
        self.close()