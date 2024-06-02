import sys

from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from settings_window import SettingsWindow



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
