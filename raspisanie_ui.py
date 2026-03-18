# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'raspisanie_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDialog, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1164, 658)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableView_courses = QTableView(Dialog)
        self.tableView_courses.setObjectName(u"tableView_courses")
        self.tableView_courses.setMinimumSize(QSize(400, 0))

        self.verticalLayout.addWidget(self.tableView_courses)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.lineEdit_courses_name = QLineEdit(Dialog)
        self.lineEdit_courses_name.setObjectName(u"lineEdit_courses_name")

        self.verticalLayout_6.addWidget(self.lineEdit_courses_name)

        self.comboBox_courses_age_type = QComboBox(Dialog)
        self.comboBox_courses_age_type.setObjectName(u"comboBox_courses_age_type")

        self.verticalLayout_6.addWidget(self.comboBox_courses_age_type)

        self.textEdit_courses_caption = QTextEdit(Dialog)
        self.textEdit_courses_caption.setObjectName(u"textEdit_courses_caption")

        self.verticalLayout_6.addWidget(self.textEdit_courses_caption)

        self.pushButton_courses_create = QPushButton(Dialog)
        self.pushButton_courses_create.setObjectName(u"pushButton_courses_create")

        self.verticalLayout_6.addWidget(self.pushButton_courses_create)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 2, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.tableView_begin_courses = QTableView(Dialog)
        self.tableView_begin_courses.setObjectName(u"tableView_begin_courses")
        self.tableView_begin_courses.setMinimumSize(QSize(400, 0))

        self.verticalLayout_4.addWidget(self.tableView_begin_courses)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.dateTimeEdit_begin_courses_data = QDateTimeEdit(Dialog)
        self.dateTimeEdit_begin_courses_data.setObjectName(u"dateTimeEdit_begin_courses_data")

        self.verticalLayout_9.addWidget(self.dateTimeEdit_begin_courses_data)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.comboBox_2_begin_courses_courses = QComboBox(Dialog)
        self.comboBox_2_begin_courses_courses.setObjectName(u"comboBox_2_begin_courses_courses")

        self.verticalLayout_9.addWidget(self.comboBox_2_begin_courses_courses)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.dateEdit_begin_courses_start_data = QDateEdit(Dialog)
        self.dateEdit_begin_courses_start_data.setObjectName(u"dateEdit_begin_courses_start_data")

        self.horizontalLayout.addWidget(self.dateEdit_begin_courses_start_data)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.dateEdit_2_begin_courses_end_data = QDateEdit(Dialog)
        self.dateEdit_2_begin_courses_end_data.setObjectName(u"dateEdit_2_begin_courses_end_data")

        self.horizontalLayout_2.addWidget(self.dateEdit_2_begin_courses_end_data)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.comboBox_3_begin_courses_teacher = QComboBox(Dialog)
        self.comboBox_3_begin_courses_teacher.setObjectName(u"comboBox_3_begin_courses_teacher")

        self.verticalLayout_9.addWidget(self.comboBox_3_begin_courses_teacher)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.comboBox_begin_courses_first_lesson = QComboBox(Dialog)
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.addItem("")
        self.comboBox_begin_courses_first_lesson.setObjectName(u"comboBox_begin_courses_first_lesson")

        self.verticalLayout_8.addWidget(self.comboBox_begin_courses_first_lesson)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.comboBox_5_begin_courses_second_lesson = QComboBox(Dialog)
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.addItem("")
        self.comboBox_5_begin_courses_second_lesson.setObjectName(u"comboBox_5_begin_courses_second_lesson")

        self.verticalLayout_7.addWidget(self.comboBox_5_begin_courses_second_lesson)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.timeEdit__begin_courses_time_lesson = QTimeEdit(Dialog)
        self.timeEdit__begin_courses_time_lesson.setObjectName(u"timeEdit__begin_courses_time_lesson")

        self.verticalLayout_9.addWidget(self.timeEdit__begin_courses_time_lesson)

        self.pushButton_begin_courses_create = QPushButton(Dialog)
        self.pushButton_begin_courses_create.setObjectName(u"pushButton_begin_courses_create")

        self.verticalLayout_9.addWidget(self.pushButton_begin_courses_create)


        self.gridLayout.addLayout(self.verticalLayout_9, 0, 1, 2, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.tableView_teachers = QTableView(Dialog)
        self.tableView_teachers.setObjectName(u"tableView_teachers")
        self.tableView_teachers.setMinimumSize(QSize(300, 0))

        self.verticalLayout_3.addWidget(self.tableView_teachers)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.lineEdit_teachers_fullname = QLineEdit(Dialog)
        self.lineEdit_teachers_fullname.setObjectName(u"lineEdit_teachers_fullname")

        self.verticalLayout_5.addWidget(self.lineEdit_teachers_fullname)

        self.pushButton_teachers_create = QPushButton(Dialog)
        self.pushButton_teachers_create.setObjectName(u"pushButton_teachers_create")

        self.verticalLayout_5.addWidget(self.pushButton_teachers_create)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_10.addWidget(self.label_11)

        self.comboBox_6_remove_table = QComboBox(Dialog)
        self.comboBox_6_remove_table.setObjectName(u"comboBox_6_remove_table")

        self.verticalLayout_10.addWidget(self.comboBox_6_remove_table)

        self.comboBox_7_remove_line = QComboBox(Dialog)
        self.comboBox_7_remove_line.setObjectName(u"comboBox_7_remove_line")

        self.verticalLayout_10.addWidget(self.comboBox_7_remove_line)

        self.pushButton_remove_line = QPushButton(Dialog)
        self.pushButton_remove_line.setObjectName(u"pushButton_remove_line")

        self.verticalLayout_10.addWidget(self.pushButton_remove_line)


        self.gridLayout.addLayout(self.verticalLayout_10, 1, 2, 1, 1)


        self.retranslateUi(Dialog)
        self.comboBox_6_remove_table.currentIndexChanged.connect(self.comboBox_7_remove_line.clear)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0440\u0443\u0436\u043a\u0438", None))
        self.lineEdit_courses_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u0440\u0443\u0436\u043a\u0430", None))
        self.comboBox_courses_age_type.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u043e\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))
        self.textEdit_courses_caption.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_courses_create.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u0440\u0443\u0436\u043e\u043a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0440\u0442 \u043a\u0440\u0443\u0436\u043a\u043e\u0432", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u0438\u043a\u0430\u0437\u0430", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u041a\u0440\u0443\u0436\u043e\u043a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0431\u043e\u0442\u044b \u043a\u0440\u0443\u0436\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0421", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u0435", None))
        self.comboBox_begin_courses_first_lesson.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u041d", None))
        self.comboBox_begin_courses_first_lesson.setItemText(1, QCoreApplication.translate("Dialog", u"\u0412\u0422", None))
        self.comboBox_begin_courses_first_lesson.setItemText(2, QCoreApplication.translate("Dialog", u"\u0421\u0420", None))
        self.comboBox_begin_courses_first_lesson.setItemText(3, QCoreApplication.translate("Dialog", u"\u0427\u0422", None))
        self.comboBox_begin_courses_first_lesson.setItemText(4, QCoreApplication.translate("Dialog", u"\u041f\u0422", None))
        self.comboBox_begin_courses_first_lesson.setItemText(5, QCoreApplication.translate("Dialog", u"\u0421\u0411", None))
        self.comboBox_begin_courses_first_lesson.setItemText(6, QCoreApplication.translate("Dialog", u"\u0412\u0421", None))

        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u0435", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u041d", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(1, QCoreApplication.translate("Dialog", u"\u0412\u0422", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(2, QCoreApplication.translate("Dialog", u"\u0421\u0420", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(3, QCoreApplication.translate("Dialog", u"\u0427\u0422", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(4, QCoreApplication.translate("Dialog", u"\u041f\u0422", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(5, QCoreApplication.translate("Dialog", u"\u0421\u0411", None))
        self.comboBox_5_begin_courses_second_lesson.setItemText(6, QCoreApplication.translate("Dialog", u"\u0412\u0421", None))

        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0437\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.pushButton_begin_courses_create.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0430\u0440\u0442 \u043a\u0440\u0443\u0436\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.lineEdit_teachers_fullname.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e", None))
        self.pushButton_teachers_create.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0440\u0443\u0436\u043e\u043a/\u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f/\u0441\u0442\u0430\u0440\u0442 \u043a\u0440\u0443\u0436\u043a\u0430", None))
        self.comboBox_6_remove_table.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u0438\u0441\u043e\u043a \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.comboBox_7_remove_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u0430\u043f\u0438\u0441\u044c \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_remove_line.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

