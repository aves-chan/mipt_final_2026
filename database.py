from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os

db_name = "database_mipt.db"

class Database:
    def __init__(self):
        exist = os.path.exists(os.path.join(os.getcwd(), db_name))

        db = QSqlDatabase().addDatabase("QSQLITE")
        db.setDatabaseName(db_name)
        db.open()

        query = QSqlQuery()
        query.exec("""
        CREATE TABLE IF NOT EXISTS schema (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        capacity INTEGER 
        );
        """)
        query = QSqlQuery()
        query.exec("""
        CREATE TABLE IF NOT EXISTS events_type (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        );
        """)
        query = QSqlQuery()
        query.exec("""
        CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        create_date TEXT,
        event_type INTEGER,
        name TEXT,
        data_begin TEXT,
        time_begin TEXT,
        time_end TEXT,
        room INTEGER,
        caption TEXT,
        premer TEXT,
        FOREIGN KEY (event_type)  
        REFERENCES events_type(id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
        FOREIGN KEY (room)  
        REFERENCES schema(id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
        );
        """)

        if not exist:
            query = QSqlQuery()
            query.exec("""
            INSERT INTO schema (name, capacity) VALUES 
            ('большой зал', 150),
            ('малый зал', 50),
            ('гримерная комната 1', 5),
            ('гримерная комната 2', 7),
            ('гримерная комната 3', 2),
            ('реквизиторская комната', 9),
            ('Хранилище декораций и костюмов', 23),
            ('кабинет режиссёра', 3),
            ('художественный кабинет', 10),
            ('бухгалтерия', 8);
            """)
            query = QSqlQuery()
            query.exec("""
            INSERT INTO events_type (name) VALUES 
            ('спектакль'),
            ('постановка'),
            ('пробы'),
            ('репетиция'),
            ('фестиваль'),
            ('концерт');         
            """)
            query = QSqlQuery()
            query.exec("""
            INSERT INTO events (create_date, event_type,  name,  data_begin,  time_begin,  time_end, room,  caption, premer) VALUES
            ('2025-05-09', 1, 'первый', '2025-07-19', '14:00', '15:00', 1, 'пам пам', 'да'),
            ('2025-06-09', 2, 'второй', '2025-07-20', '13:00', '14:00', 2, 'пам бум пам', ''),
            ('2025-05-22', 3, 'третий', '2025-07-21', '12:00', '14:00', 1, 'пам мэм пам', ''),
            ('2025-07-18', 4, 'пятый', '2025-07-22', '11:00', '16:00', 2, 'пам гым пам', '');
            """)




