# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Loading(object):
    def setupUi(self, Loading):
        if not Loading.objectName():
            Loading.setObjectName(u"Loading")
        Loading.resize(231, 123)
        self.gridLayout_2 = QGridLayout(Loading)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Loading)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Loading)

        QMetaObject.connectSlotsByName(Loading)
    # setupUi

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(QCoreApplication.translate("Loading", u"Form", None))
        self.label.setText(QCoreApplication.translate("Loading", u"TextLabel", None))
    # retranslateUi

