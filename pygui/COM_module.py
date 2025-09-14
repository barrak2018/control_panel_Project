# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'COM_module_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_COM_UI(object):
    def setupUi(self, COM_UI):
        if not COM_UI.objectName():
            COM_UI.setObjectName(u"COM_UI")
        COM_UI.resize(510, 401)
        COM_UI.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(COM_UI)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.port_combobox = QComboBox(COM_UI)
        self.port_combobox.addItem("")
        self.port_combobox.setObjectName(u"port_combobox")

        self.horizontalLayout.addWidget(self.port_combobox)

        self.label = QLabel(COM_UI)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 32))
        self.label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.connection_button = QPushButton(COM_UI)
        self.connection_button.setObjectName(u"connection_button")
        self.connection_button.setEnabled(True)
        self.connection_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.connection_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(COM_UI)

        QMetaObject.connectSlotsByName(COM_UI)
    # setupUi

    def retranslateUi(self, COM_UI):
        COM_UI.setWindowTitle(QCoreApplication.translate("COM_UI", u"Selector de Puerto", None))
        self.port_combobox.setItemText(0, QCoreApplication.translate("COM_UI", u"None", None))

        self.label.setText(QCoreApplication.translate("COM_UI", u"TextLabel", None))
        self.connection_button.setText(QCoreApplication.translate("COM_UI", u"0/1", None))
    # retranslateUi

