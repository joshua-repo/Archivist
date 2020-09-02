import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import tools.Utilities
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QMenu, QTabBar, QTabWidget, QFileDialog
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        tagsMenu = menubar.addMenu('&Tags')

        #fileMenu
        addLibMenu = QMenu('Add a new path to library', self)
        addLocal = QAction('Local Path', self)
        addLocal.triggered.connect(self.addLocalPath)
        addURL = QAction('From Internet', self)
        addDisk = QAction('Whole Disk', self)
        addLibMenu.addAction(addLocal)
        addLibMenu.addAction(addURL)
        addLibMenu.addAction(addDisk)

        importLib = QAction('Import the library', self)
        exportLib = QAction('Export the library', self)

        fileMenu.addMenu(addLibMenu)
        fileMenu.addAction(importLib)
        fileMenu.addAction(exportLib)

        #editMenu
        addFileType = QAction('Add a new file type', self)

        editMenu.addAction(addFileType)

        #viewMenu
        iconSizeMenu = QMenu('Icon size', self)
        smallSize = QAction('Small size', self)
        middleSize = QAction('Middle size', self)
        largeSize = QAction('Large size', self)
        iconSizeMenu.addAction(smallSize)
        iconSizeMenu.addAction(middleSize)
        iconSizeMenu.addAction(largeSize)

        sortMenu = QMenu('Sort by', self)
        nameOrder = QAction('Name', self)
        sizeOrder = QAction('Size', self)
        typeOrder = QAction('Type', self)
        dataOrder = QAction('Data', self)
        tagsOrder = QAction('Tags', self)
        sortMenu.addAction(nameOrder)
        sortMenu.addAction(sizeOrder)
        sortMenu.addAction(typeOrder)
        sortMenu.addAction(dataOrder)
        sortMenu.addAction(tagsOrder)

        viewMenu.addMenu(iconSizeMenu)
        viewMenu.addMenu(sortMenu)

        #tagsMenu
        addTags = QAction('New Label', self)
        addRating = QAction('New Rating', self)

        tagsMenu.addAction(addTags)
        tagsMenu.addAction(addRating)

        self.tabWidget = QTabWidget()
        self.tabWidget.setMovable(True)

        self.resize(1800, 950)
        self.center()
        self.setWindowTitle('Archivist')
        self.setWindowIcon(QIcon('./core/icon.png'))

    def addLocalPath(self):
        self.localPath = QFileDialog.getExistingDirectory(self, 'Select the directory', '/')
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./backups/Archivies.db')
        db.open()
        query = QSqlQuery()
        query.exec()

    def createDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./backups/Archivies.db')
        db.open()
        query = QSqlQuery()
        query.exec('''CREATE TABLE IF NOT EXISTS METADATE(
                VERSION     TEXT    PRIMARY KEY NOT NULL ,
                LOCATIONS   TEXT    NOT NULL 
            );''')

        query.exec('''CREATE TABLE IF NOT EXISTS PICTURES(
                PATH        TEXT    PRIMARY KEY NOT NULL ,
                FILENAME    TEXT    NOT NULL ,
                EXIF        TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL
            );''')

        query.exec('''CREATE TABLE IF NOT EXISTS PDFDOC(
                PATH        TEXT    PRIMARY KEY ,
                FILENAME    TEXT    NOT NULL ,
                ARRAGE      TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL 
            );''')

        query.exec('''CREATE TABLE IF NOT EXISTS MUSIC(
                PATH        TEXT    PRIMARY KEY ,
                FILENAME    TEXT    NOT NULL ,
                METADATA    TEXT    NOT NULL ,
                THUMBNAIL   TEXT    NOT NULL ,
                ALBUM       TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL ,
                STYLE       TEXT    NOT NULL 
            );''')
        db.close()

    def readDB(self):
        #TODO 用导入的数据库直接替换现有的Archivies.db
        pass

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