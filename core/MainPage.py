from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QMenu
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1800, 950)
        self.center()
        self.setWindowTitle('Archivist')
        self.setWindowIcon(QIcon('./core/icon.png'))

        exitAct = QAction('&Exit',self)
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        tagMenu = menubar.addMenu('&Tags')
        netMenu = menubar.addMenu('&NetDisk')
        exitMenu = menubar.addMenu('&Exit')

        importLib = QAction('Import the library', self)
        exportLib = QAction('Export the library', self)

        addLibMenu = QMenu('Add a new path to library', self)
        addLocal = QAction('Local Path', self)
        addURL = QAction('From URL', self)
        addLibMenu.addAction(addLocal)
        addLibMenu.addAction(addURL)

        fileMenu.addMenu(addLibMenu)
        fileMenu.addAction(importLib)
        fileMenu.addAction(exportLib)

        exitMenu.addAction(exitAct)

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