from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class StartPage(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitButtom = QPushButton('Exit', self)
        exitButtom.clicked.connect(QCoreApplication.instance().quit)
        exitButtom.resize(exitButtom.sizeHint())

        okButtom = QPushButton('OK', self)
        okButtom.clicked.connect(self.toMainPage)

        pathButtom = QPushButton('...', self)

        loginButtom = QPushButton('login', self)
        registButtom = QPushButton('regist', self)

        welLabel = QLabel('Welcoming to Archivist!')
        impLabelLocal = QLabel('Import Library from a local path:')
        impLabelLogin = QLabel('Set up Archivist via login.')
        commentLabel = QLabel('W.I.P')

        pathEdit = QLineEdit()
        accountEdit = QLineEdit()
        passwordEdit = QLineEdit()

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(welLabel, 0, 0)
        grid.addWidget(impLabelLocal, 1, 0)
        grid.addWidget(pathEdit, 2, 0)
        grid.addWidget(pathButtom, 2, 1)
        grid.addWidget(impLabelLogin, 3, 0)
        grid.addWidget(commentLabel, 3, 1)
        grid.addWidget(accountEdit, 4, 0)
        grid.addWidget(passwordEdit, 5, 0)
        grid.addWidget(loginButtom, 5, 1)
        grid.addWidget(registButtom, 5, 2)
        grid.addWidget(okButtom, 6, 5)
        grid.addWidget(exitButtom, 6, 6)


        self.resize(700, 200)
        self.center()
        self.setWindowTitle('Set Up Archivist')
        self.setWindowIcon(QIcon('./core/icon.png'))

    def toMainPage(self):
        self.switch_window.emit()
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
