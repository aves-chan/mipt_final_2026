from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from events import EventsDialog
from finance import FinanceDialog
from postanovka import PostanovkaDialog
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.ui.pushButton_events.clicked.connect(self.f)
        self.ui.pushButton_postanovka.clicked.connect(self.ff)
        self.ui.pushButton_finance.clicked.connect(self.fff)

    def f(self):
        dialog = EventsDialog(self, self.db)
        dialog.show()

    def ff(self):
        dialog = PostanovkaDialog(self, self.db)
        dialog.show()

    def fff(self):
        dialog = FinanceDialog(self, self.db)
        dialog.show()


app = QApplication()
window = MainWindow()
window.show()
app.exec()