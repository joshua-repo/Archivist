from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1800, 1000)
        self.center()
        self.setWindowTitle('Archivist')
        self.setWindowIcon(QIcon('./core/icon.png'))
        self.show()
