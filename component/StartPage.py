import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QDesktopWidget, QGridLayout, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class StartPage(QWidget):

    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.exitButtom = QPushButton('Exit', self)
        self.exitButtom.clicked.connect(QCoreApplication.instance().quit)

        self.okButtom = QPushButton('OK', self)
        self.okButtom.clicked.connect(self.toMainPage)

        self.pathButtom = QPushButton('...', self)
        self.pathButtom.clicked.connect(self.openPath)

        self.loginButtom = QPushButton('login', self)
        self.registButtom = QPushButton('regist', self)

        self.welLabel = QLabel('Welcoming to Archivist!')
        self.impLabelLocal = QLabel('Import Library from a local path:')
        self.impLabelLogin = QLabel('Set up Archivist via login.')
        self.commentLabel = QLabel('W.I.P')

        self.pathEdit = QLineEdit()
        self.accountEdit = QLineEdit()
        self.passwordEdit = QLineEdit()

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.welLabel, 0, 0)
        self.grid.addWidget(self.impLabelLocal, 1, 0)
        self.grid.addWidget(self.pathEdit, 2, 0)
        self.grid.addWidget(self.pathButtom, 2, 1)
        self.grid.addWidget(self.impLabelLogin, 3, 0)
        self.grid.addWidget(self.commentLabel, 3, 1)
        self.grid.addWidget(self.accountEdit, 4, 0)
        self.grid.addWidget(self.passwordEdit, 5, 0)
        self.grid.addWidget(self.loginButtom, 5, 1)
        self.grid.addWidget(self.registButtom, 5, 2)
        self.grid.addWidget(self.okButtom, 6, 5)
        self.grid.addWidget(self.exitButtom, 6, 6)

        self.resize(700, 200)
        self.center()
        self.setWindowTitle('Set Up Archivist')
        self.setWindowIcon(QIcon('./resource/icon.png'))

    def openPath(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Select the Library', '/', 'Archives(Archives.db)')
        if os.path.split(fileName)[-1] != 'Archives.db':
            QMessageBox.information(self, 'Error','Please choose the Archives.db')
        else:
            self.pathEdit.setText(fileName)

    def toMainPage(self):
        if self.pathEdit.text() == "":
            self.libPath = ""
            self.switchWindow.emit(self.libPath)
            self.close()
        else:
            self.libPath = self.pathEdit.text()
            self.switchWindow.emit(self.libPath)
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())