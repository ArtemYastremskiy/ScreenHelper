# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(618, 392)
        Dialog.setStyleSheet(u"background-color: rgb(189, 189, 189);\n"
"font-family: Trebuchet MS;\n"
"font-size: 18px;")
        self.TabWidget = QTabWidget(Dialog)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setGeometry(QRect(-10, 0, 641, 331))
        self.General = QWidget()
        self.General.setObjectName(u"General")
        self.groupBox_translation = QGroupBox(self.General)
        self.groupBox_translation.setObjectName(u"groupBox_translation")
        self.groupBox_translation.setGeometry(QRect(10, 10, 571, 91))
        self.groupBox_translation.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.groupBox_translation)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 284, 62))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_target_lang = QLabel(self.layoutWidget)
        self.lbl_target_lang.setObjectName(u"lbl_target_lang")

        self.horizontalLayout.addWidget(self.lbl_target_lang)

        self.cb_target_lang = QComboBox(self.layoutWidget)
        self.cb_target_lang.addItem("")
        self.cb_target_lang.addItem("")
        self.cb_target_lang.addItem("")
        self.cb_target_lang.setObjectName(u"cb_target_lang")
        self.cb_target_lang.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"border: 2px solid rgb(34, 34, 34);\n"
"border-radius: 5px;")

        self.horizontalLayout.addWidget(self.cb_target_lang)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.checkbox_autotranslate = QCheckBox(self.layoutWidget)
        self.checkbox_autotranslate.setObjectName(u"checkbox_autotranslate")
        self.checkbox_autotranslate.setChecked(False)
        self.checkbox_autotranslate.setTristate(False)

        self.verticalLayout_4.addWidget(self.checkbox_autotranslate)

        self.TabWidget.addTab(self.General, "")
        self.API_keys = QWidget()
        self.API_keys.setObjectName(u"API_keys")
        self.lbl_please_register = QLabel(self.API_keys)
        self.lbl_please_register.setObjectName(u"lbl_please_register")
        self.lbl_please_register.setGeometry(QRect(10, 10, 611, 21))
        self.layoutWidget1 = QWidget(self.API_keys)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 40, 581, 221))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_llama3 = QGroupBox(self.layoutWidget1)
        self.groupBox_llama3.setObjectName(u"groupBox_llama3")
        self.layoutWidget2 = QWidget(self.groupBox_llama3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 20, 351, 56))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_groq = QLabel(self.layoutWidget2)
        self.lbl_groq.setObjectName(u"lbl_groq")

        self.verticalLayout.addWidget(self.lbl_groq)

        self.lineEdit_llama3 = QLineEdit(self.layoutWidget2)
        self.lineEdit_llama3.setObjectName(u"lineEdit_llama3")

        self.verticalLayout.addWidget(self.lineEdit_llama3)


        self.verticalLayout_3.addWidget(self.groupBox_llama3)

        self.groupBox_wolfram = QGroupBox(self.layoutWidget1)
        self.groupBox_wolfram.setObjectName(u"groupBox_wolfram")
        self.layoutWidget3 = QWidget(self.groupBox_wolfram)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 20, 351, 56))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_wolfram = QLabel(self.layoutWidget3)
        self.lbl_wolfram.setObjectName(u"lbl_wolfram")

        self.verticalLayout_2.addWidget(self.lbl_wolfram)

        self.lineEdit_wolfram = QLineEdit(self.layoutWidget3)
        self.lineEdit_wolfram.setObjectName(u"lineEdit_wolfram")

        self.verticalLayout_2.addWidget(self.lineEdit_wolfram)


        self.verticalLayout_3.addWidget(self.groupBox_wolfram)

        self.TabWidget.addTab(self.API_keys, "")
        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 340, 561, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_apply = QPushButton(self.layoutWidget_2)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setMinimumSize(QSize(0, 30))
        self.btn_apply.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_apply)

        self.btn_save = QPushButton(self.layoutWidget_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 30))
        self.btn_save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(self.layoutWidget_2)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 30))
        self.btn_cancel.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_cancel)


        self.retranslateUi(Dialog)

        self.TabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_translation.setTitle(QCoreApplication.translate("Dialog", u"Translation", None))
        self.lbl_target_lang.setText(QCoreApplication.translate("Dialog", u"target language:", None))
        self.cb_target_lang.setItemText(0, QCoreApplication.translate("Dialog", u"English", None))
        self.cb_target_lang.setItemText(1, QCoreApplication.translate("Dialog", u"Ukrainian", None))
        self.cb_target_lang.setItemText(2, QCoreApplication.translate("Dialog", u"Russian", None))

        self.checkbox_autotranslate.setText(QCoreApplication.translate("Dialog", u"Translate AI answers automaticly", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.General), QCoreApplication.translate("Dialog", u"General", None))
        self.lbl_please_register.setText(QCoreApplication.translate("Dialog", u"Please register for the following services to use them inside this application.", None))
        self.groupBox_llama3.setTitle(QCoreApplication.translate("Dialog", u"Llama 3", None))
        self.lbl_groq.setText(QCoreApplication.translate("Dialog", u"https://groq.com/", None))
        self.lineEdit_llama3.setPlaceholderText(QCoreApplication.translate("Dialog", u"gsk_*****************************", None))
        self.groupBox_wolfram.setTitle(QCoreApplication.translate("Dialog", u"Wolfram Alpha", None))
        self.lbl_wolfram.setText(QCoreApplication.translate("Dialog", u"https://www.wolframalpha.com/", None))
        self.lineEdit_wolfram.setPlaceholderText(QCoreApplication.translate("Dialog", u"Paste your api here", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.API_keys), QCoreApplication.translate("Dialog", u"API keys", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

