# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'events.ui'
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
    QLabel, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(762, 338)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.tableView_schema = QTableView(Dialog)
        self.tableView_schema.setObjectName(u"tableView_schema")

        self.verticalLayout_3.addWidget(self.tableView_schema)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableView_type_events = QTableView(Dialog)
        self.tableView_type_events.setObjectName(u"tableView_type_events")

        self.verticalLayout_2.addWidget(self.tableView_type_events)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"C\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u044b \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439", None))
    # retranslateUi

