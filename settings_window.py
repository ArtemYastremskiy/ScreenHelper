import json

from PySide6.QtWidgets import QDialog
from ui_settings import Ui_Settings


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        with open('settings.json') as f:
            self.settings = json.load(f)

        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        
    
    def apply(self):
        self.settings["API_keys"]["llama3"] = self.ui.lineEdit_llama3.text()
        self.settings["API_keys"]["wolfram"] = self.ui.lineEdit_wolfram.text()

        self.settings["General"]["Translation"]["target_languege"] = self.settings["General"]["Translation"]["supported_langueges"][self.ui.cb_target_lang.currentText()]
        self.settings["General"]["Translation"]["autotranslate"] = self.ui.checkbox_autotranslate.isChecked()


        with open('settings.json', 'w') as f:
            json.dump(self.settings, f, ensure_ascii=False, indent=4)


    def save(self):
        self.apply()
        self.close()


    def cancel(self):
        self.close()