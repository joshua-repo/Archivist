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
        exitButtom = QPushButton('Exit', self)
        exitButtom.clicked.connect(QCoreApplication.instance().quit)
        exitButtom.resize(exitButtom.sizeHint())

        okButtom = QPushButton('OK', self)
        okButtom.clicked.connect(self.toMainPage)

        pathButtom = QPushButton('...', self)
        pathButtom.clicked.connect(self.openPath)

        loginButtom = QPushButton('login', self)
        registButtom = QPushButton('regist', self)

        welLabel = QLabel('Welcoming to Archivist!')
        impLabelLocal = QLabel('Import Library from a local path:')
        impLabelLogin = QLabel('Set up Archivist via login.')
        commentLabel = QLabel('W.I.P')

        self.pathEdit = QLineEdit()
        self.accountEdit = QLineEdit()
        self.passwordEdit = QLineEdit()

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(welLabel, 0, 0)
        grid.addWidget(impLabelLocal, 1, 0)
        grid.addWidget(self.pathEdit, 2, 0)
        grid.addWidget(pathButtom, 2, 1)
        grid.addWidget(impLabelLogin, 3, 0)
        grid.addWidget(commentLabel, 3, 1)
        grid.addWidget(self.accountEdit, 4, 0)
        grid.addWidget(self.passwordEdit, 5, 0)
        grid.addWidget(loginButtom, 5, 1)
        grid.addWidget(registButtom, 5, 2)
        grid.addWidget(okButtom, 6, 5)
        grid.addWidget(exitButtom, 6, 6)

        self.resize(700, 200)
        self.center()
        self.setWindowTitle('Set Up Archivist')
        self.setWindowIcon(QIcon('./core/icon.png'))

    def openPath(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Select the Library', '/', 'Archives(Archives.db)')
        #是不是要设计成只能命名为Archives.db呢？如果是那么又要怎么设计版本兼容？
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