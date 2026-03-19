from PySide6.QtWidgets import QDialog
from PySide6.QtSql import QSqlQueryModel
from database import Database
from finance_ui import Ui_Dialog
from PySide6.QtCore import Qt

class FinanceDialog(QDialog):
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

