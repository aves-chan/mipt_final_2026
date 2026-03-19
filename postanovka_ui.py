# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postanovka.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(751, 412)
        self.verticalLayout_5 = QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.tableView_events = QTableView(Dialog)
        self.tableView_events.setObjectName(u"tableView_events")

        self.verticalLayout_4.addWidget(self.tableView_events)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableView_schema = QTableView(Dialog)
        self.tableView_schema.setObjectName(u"tableView_schema")

        self.verticalLayout.addWidget(self.tableView_schema)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableView_type_events = QTableView(Dialog)
        self.tableView_type_events.setObjectName(u"tableView_type_events")

        self.verticalLayout_2.addWidget(self.tableView_type_events)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_create_event = QPushButton(Dialog)
        self.pushButton_create_event.setObjectName(u"pushButton_create_event")

        self.verticalLayout_3.addWidget(self.pushButton_create_event)

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"C\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u044b \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439", None))
        self.pushButton_create_event.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0432\u0438\u0434 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0438\u0434 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0435 ", None))
    # retranslateUi

