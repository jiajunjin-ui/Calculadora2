# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(459, 278)
        self.btsuma = QPushButton(Dialog)
        self.btsuma.setObjectName(u"btsuma")
        self.btsuma.setGeometry(QRect(290, 80, 61, 51))
        self.btresta = QPushButton(Dialog)
        self.btresta.setObjectName(u"btresta")
        self.btresta.setGeometry(QRect(360, 80, 61, 51))
        self.btmulti = QPushButton(Dialog)
        self.btmulti.setObjectName(u"btmulti")
        self.btmulti.setGeometry(QRect(290, 140, 61, 51))
        self.btdivi = QPushButton(Dialog)
        self.btdivi.setObjectName(u"btdivi")
        self.btdivi.setGeometry(QRect(360, 140, 61, 51))
        self.salir = QPushButton(Dialog)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(290, 200, 131, 51))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 10, 221, 61))
        self.entrada1 = QLineEdit(Dialog)
        self.entrada1.setObjectName(u"entrada1")
        self.entrada1.setGeometry(QRect(20, 80, 261, 51))
        self.entrada2 = QLineEdit(Dialog)
        self.entrada2.setObjectName(u"entrada2")
        self.entrada2.setGeometry(QRect(20, 140, 261, 51))
        self.resultado = QLabel(Dialog)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(28, 215, 241, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btsuma.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.btresta.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.btmulti.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.btdivi.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.salir.setText(QCoreApplication.translate("Dialog", u"salir", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">Calculadora</span></p></body></html>", None))
        self.resultado.setText("")
    # retranslateUi

