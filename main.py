from PySide6.QtWidgets import QApplication, QMainWindow
from database import Database
from main_ui import Ui_MainWindow
from raspisanie_dialog import RaspisanieDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()

        self.ui.pushButton_raspisanie.clicked.connect(self.open_dialog_raspisanie)

    def open_dialog_raspisanie(self):
        dialog = RaspisanieDialog(self, self.db)
        dialog.show()

app = QApplication()
window = MainWindow()
window.show()
app.exec()