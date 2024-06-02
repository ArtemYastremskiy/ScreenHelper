# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 650)
        MainWindow.setStyleSheet(u"background-color: rgb(189, 189, 189);\n"
"font-family: Trebuchet MS;\n"
"font-size: 22px;")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 461, 291))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_select_area = QPushButton(self.layoutWidget)
        self.btn_select_area.setObjectName(u"btn_select_area")
        self.btn_select_area.setMinimumSize(QSize(0, 50))
        self.btn_select_area.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(222, 222, 222);\n"
"border: 2px solid rgb(34, 34, 34);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(170, 170, 170)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/screenshot_region.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_area.setIcon(icon)
        self.btn_select_area.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_select_area)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))
        self.textEdit.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"border: 2px solid rgb(34, 34, 34);\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_select_type = QLabel(self.layoutWidget)
        self.lbl_select_type.setObjectName(u"lbl_select_type")
        self.lbl_select_type.setStyleSheet(u"font-family: arial;\n"
"font-size: 22pt;")

        self.verticalLayout.addWidget(self.lbl_select_type)

        self.cb_select_type = QComboBox(self.layoutWidget)
        self.cb_select_type.addItem("")
        self.cb_select_type.addItem("")
        self.cb_select_type.addItem("")
        self.cb_select_type.setObjectName(u"cb_select_type")
        self.cb_select_type.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"border: 2px solid rgb(34, 34, 34);\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.cb_select_type)

        self.btn_send_request = QPushButton(self.layoutWidget)
        self.btn_send_request.setObjectName(u"btn_send_request")
        self.btn_send_request.setMinimumSize(QSize(0, 40))
        self.btn_send_request.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(222, 222, 222);\n"
"border: 2px solid rgb(34, 34, 34);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(170, 170, 170)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_request.setIcon(icon1)
        self.btn_send_request.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_send_request)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 390, 461, 201))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_output = QLabel(self.layoutWidget1)
        self.lbl_output.setObjectName(u"lbl_output")
        self.lbl_output.setStyleSheet(u"font-family: arial;\n"
"font-size: 22pt;")

        self.verticalLayout_4.addWidget(self.lbl_output)

        self.tb_result = QTextBrowser(self.layoutWidget1)
        self.tb_result.setObjectName(u"tb_result")
        self.tb_result.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"border: 2px solid rgb(34, 34, 34);\n"
"border-radius: 10px;")
        self.tb_result.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.tb_result)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 461, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_help = QPushButton(self.layoutWidget2)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(0, 45))
        self.btn_help.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(170, 170, 170)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon2)
        self.btn_help.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_help)

        self.btn_settings = QPushButton(self.layoutWidget2)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(170, 170, 170)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon3)
        self.btn_settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_settings)

        self.btn_history = QPushButton(self.layoutWidget2)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setMinimumSize(QSize(0, 45))
        self.btn_history.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(170, 170, 170)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/history.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_history.setIcon(icon4)
        self.btn_history.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_history)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_select_area.setText(QCoreApplication.translate("MainWindow", u"Select area", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[no text recognized]", None))
        self.lbl_select_type.setText(QCoreApplication.translate("MainWindow", u"Select type:", None))
        self.cb_select_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Llama-3", None))
        self.cb_select_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Google translate", None))
        self.cb_select_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Wolfram Alpha", None))

        self.btn_send_request.setText(QCoreApplication.translate("MainWindow", u"Send reqest", None))
        self.lbl_output.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.tb_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PLEACE SEND A REQUEST TO GET RESULTS ", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
    # retranslateUi

