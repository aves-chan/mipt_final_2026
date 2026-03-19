# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 369)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_events = QPushButton(self.centralwidget)
        self.pushButton_events.setObjectName(u"pushButton_events")

        self.horizontalLayout.addWidget(self.pushButton_events)

        self.pushButton_postanovka = QPushButton(self.centralwidget)
        self.pushButton_postanovka.setObjectName(u"pushButton_postanovka")

        self.horizontalLayout.addWidget(self.pushButton_postanovka)

        self.pushButton_finance = QPushButton(self.centralwidget)
        self.pushButton_finance.setObjectName(u"pushButton_finance")

        self.horizontalLayout.addWidget(self.pushButton_finance)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_events.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.pushButton_postanovka.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0441\u043f\u0435\u043a\u0442\u0430\u043a\u043b\u0435\u0439", None))
        self.pushButton_finance.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043d\u0430\u043d\u0441\u044b", None))
    # retranslateUi

