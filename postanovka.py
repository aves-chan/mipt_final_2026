from PySide6.QtWidgets import QDialog
from PySide6.QtSql import QSqlQueryModel
from database import Database
from postanovka_ui import Ui_Dialog
from PySide6.QtCore import Qt

class PostanovkaDialog(QDialog):
    def __init__(self, parent, db: Database):
        super().__init__(parent=parent)
        self.db = db
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.fresh_data()

    def fresh_data(self):
        model = QSqlQueryModel()
        model.setQuery("""
        SELECT * FROM schema;
        """)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "название")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "вместимость")
        self.ui.tableView_schema.setModel(model)
        self.ui.tableView_schema.resizeRowsToContents()
        self.ui.tableView_schema.resizeColumnsToContents()

        model = QSqlQueryModel()
        model.setQuery("""
        SELECT * FROM events_type;
        """)
        model.setHeaderData(0, Qt.Orientation.Horizontal, "id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "вид")
        self.ui.tableView_type_events.setModel(model)
        self.ui.tableView_type_events.resizeRowsToContents()
        self.ui.tableView_type_events.resizeColumnsToContents()

        model = QSqlQueryModel()
        model.setQuery("""
        SELECT 
        e.create_date,
        e.id,
        t.name,
        e.name,
        e.data_begin,
        e.time_begin,
        e.time_end,
        s.name,
        e.caption,
        e.premer
        FROM events AS e
        JOIN events_type AS t ON t.id == e.event_type
        JOIN schema AS s ON s.id == e.room;
        """)
        model.setHeaderData(0, Qt.Orientation.Horizontal, "дата рег.")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "id")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "вид")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "название")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "дата")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "время нач.")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "время конца")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "помещение")
        model.setHeaderData(8, Qt.Orientation.Horizontal, "описание")
        model.setHeaderData(9, Qt.Orientation.Horizontal, "премьера")
        self.ui.tableView_events.setModel(model)
        self.ui.tableView_events.resizeRowsToContents()
        self.ui.tableView_events.resizeColumnsToContents()

