from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os

age_type = {
    "a": "Младший дошкольный возраст(3-5 лет)",
    "b": "Старший дошкольный возраст (5-7 лет)",
    "c": "Младший школьный возраст (7-10 лет)",
    "d": "Средний школьный возраст (10-14 лет)",
    "e": "Старший школьный возраст (14-17 лет)",
}

db_name = "mipt_final.db"

class Database:
    def __init__(self):
        exist = os.path.exists(os.path.join(os.getcwd(), db_name))
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_name)
        self.db.open()
        print(self.db.isOpen())

        query = QSqlQuery()
        query.exec(f"""
        CREATE TABLE IF NOT EXISTS age_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        );""")
        query.exec(f"""
        CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age_type INTEGER,
        caption TEXT,
        FOREIGN KEY (age_type) REFERENCES age_types(id) ON DELETE CASCADE ON UPDATE CASCADE
        );""")
        query.exec(f"""
        CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT
        );""")
        query.exec(f"""
        CREATE TABLE IF NOT EXISTS begin_courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_create TEXT,
        course INTEGER,
        start_data TEXT,
        end_data TEXT,
        teacher INTEGER,
        first_lesson TEXT,
        second_lesson TEXT,
        time_lesson TEXT,
        FOREIGN KEY (course) REFERENCES courses(id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (teacher) REFERENCES teachers(id) ON DELETE CASCADE ON UPDATE CASCADE
        );""")
        if not exist:
            query = QSqlQuery()
            query.exec("""
            INSERT INTO age_types (name) VALUES
            ('Младший дошкольный возраст(3-5 лет)'),
            ('Старший дошкольный возраст (5-7 лет)'),
            ('Младший школьный возраст (7-10 лет)'),
            ('Средний школьный возраст (10-14 лет)'),
            ('Старший школьный возраст (14-17 лет)');
            """)
            query.exec(f"""
            INSERT INTO teachers (fullname) VALUES 
            ('Олег Филкоф Иванович'),
            ('Мария Флюс Ивановна'),
            ('Виктор Смирнов Ивановн'),
            ('Дима Огнименшин Викторович');
            """)
            query.exec(f"""
            INSERT INTO courses (name, age_type, caption) VALUES
            ('рисование', 1, 'тут на бумаге пишут что то'),
            ('пение', 2, 'люди поют тут\nиногда'),
            ('танцы', 3, 'здесь учат танцам всегда'),
            ('баскетбол', 4, 'учат пинать мяч руками людей'),
            ('бокс', 3, 'учат людей уважать');
            """)
            query.exec(f"""
            INSERT INTO begin_courses (data_create, course, start_data, end_data, teacher, first_lesson, second_lesson, time_lesson) VALUES
            ('2025-09-11 7:0', 1, '2025-09-15', '2025-10-21', 1, 'ПН', 'ВС', '17:00'),
            ('2025-05-01 12:50', 4, '2025-06-11', '2027-09-11', 2, 'СР', 'ЧТ', '10:00'),
            ('2025-01-20 22:00', 5, '2025-02-11', '2025-12-11', 3, 'ПТ', 'СБ', '12:00');
            """)


