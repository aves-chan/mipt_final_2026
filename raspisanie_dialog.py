from PySide6.QtWidgets import QDialog
from PySide6.QtSql import QSqlTableModel, QSqlQueryModel, QSqlQuery
from database import Database
from raspisanie_ui import Ui_Dialog

class RaspisanieDialog(QDialog):
    def __init__(self, parent, db: Database):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.ui.pushButton_courses_create.setAutoDefault(False)
        self.ui.pushButton_courses_create.setDefault(False)
        self.ui.pushButton_remove_line.setAutoDefault(False)
        self.ui.pushButton_remove_line.setDefault(False)
        self.ui.pushButton_teachers_create.setAutoDefault(False)
        self.ui.pushButton_teachers_create.setDefault(False)
        self.ui.pushButton_teachers_create.setAutoDefault(False)
        self.ui.pushButton_teachers_create.setDefault(False)
        self.ui.pushButton_begin_courses_create.setAutoDefault(False)
        self.ui.pushButton_begin_courses_create.setDefault(False)

        query = QSqlQuery()
        query.exec("""select * from teachers""")
        while query.next():
            self.ui.comboBox_6_remove_table.addItem(query.value(1), query.value(0) * 100)


        self.ui.comboBox_7_remove_line.setEnabled(False)
        self.ui.comboBox_6_remove_table.currentIndexChanged.connect(self.f)

        self.update_data()

    def f(self, x):
        print(f"index {x}")
        print(f"text {self.ui.comboBox_6_remove_table.currentText()}")
        print(f"data {self.ui.comboBox_6_remove_table.currentData()}")
        self.ui.comboBox_7_remove_line.setEnabled(True)
        print("====")
        query = QSqlQuery()
        query.exec("INSERT INTO teachers (fullname) VALUES ('ПРИВЕТ КАРИМ ЫЫЫЫЫ');")
        self.update_data()
        self.ui.comboBox_7_remove_line.addItems(["hello", "world", "lox"])


    def update_data(self):
        query_teachers = QSqlQueryModel()
        query_teachers.setQuery("""
        SELECT * FROM teachers;
        """)
        self.ui.tableView_teachers.setModel(query_teachers)
        query_courses = QSqlQueryModel()
        query_courses.setQuery("""
        SELECT * FROM courses JOIN age_types ON courses.age_type == age_types.id;
        """)
        self.ui.tableView_courses.setModel(query_courses)
        query_begin_courses = QSqlQueryModel()
        query_begin_courses.setQuery("""
        SELECT 
        a.data_create, 
        b.name, 
        vv.name, 
        a.start_data, 
        a.end_data, 
        c.fullname, 
        a.first_lesson, 
        a.second_lesson, 
        a.time_lesson 
        FROM begin_courses AS a
        JOIN courses AS b ON a.course == b.id
        JOIN teachers AS c ON a.teacher == c.id
        JOIN age_types AS vv ON vv.id == b.age_type;
        """)
        self.ui.tableView_begin_courses.setModel(query_begin_courses)
        self.ui.tableView_begin_courses.horizontalHeader().hide()

        self.ui.tableView_teachers.resizeColumnsToContents()
        self.ui.tableView_courses.resizeColumnsToContents()
        self.ui.tableView_begin_courses.resizeColumnsToContents()

        self.ui.tableView_teachers.resizeRowsToContents()
        self.ui.tableView_courses.resizeRowsToContents()
        self.ui.tableView_begin_courses.resizeRowsToContents()