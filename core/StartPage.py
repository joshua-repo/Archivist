from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class StartPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitBtm = QPushButton('Exit', self)
        exitBtm.clicked.connect(QCoreApplication.instance().quit)
        exitBtm.resize(exitBtm.sizeHint())
        exitBtm.move(50,50)

        OKBtm = QPushButton('OK', self)
        OKBtm.move(100, 100)

        self.resize(700, 300)
        self.center()
        self.setWindowTitle('Set Up')
        self.setWindowIcon(QIcon('./core/icon.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# class StartPage():
#     def __init__(self, object): #传入的是一个TK对象
#         object.title('Archivist Set Up')
#         object.geometry('500x200')
#         tk.Label(object, text = 'Welcome to Archivist!').grid(row = 0, column = 2)
#         tk.Label(object, text = 'Import Archivist Library from:').grid(row = 1, column = 0)
#         tk.Label(object, text = 'Path:').grid(row = 2, column = 1)
#         tk.Entry(object).grid(row = 2, column = 2)
#         tk.Button(object, text = '...').grid(row = 2, column = 3)
#         tk.Label(object, text = 'Initialize a new Library at:').grid(row = 3, column = 0)
#         tk.Label(object, text='Path:').grid(row=4, column=1)
#         tk.Entry(object).grid(row=4, column=2)
#         tk.Button(object, text='...').grid(row=4, column=3)
#         tk.Button(object, text = 'OK').grid(row = 5, column = 4)
#         tk.Button(object, text = 'Exit').grid(row = 5, column = 5)
#
#
#     def SelectPath(self):
#         self.path_ = tk.askdirectory()
#         self.libPath.set(self.path_)