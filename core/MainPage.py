import os
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QMenu, QTabBar, QTabWidget, \
    QFileDialog, QGridLayout, QSplitter, QHBoxLayout, QFrame, QAction, QGroupBox, QVBoxLayout, QTableView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.localPath = QFileDialog.getExistingDirectory(self, 'Select the directory', '/')
        self.initUI()

    def initUI(self):
        self.menuBarInit()
        self.centralWidgetGridLayout()

        self.resize(1800, 950)
        self.center()
        self.setWindowTitle('Archivist')
        self.setWindowIcon(QIcon('./core/icon.png'))

    def menuBarInit(self):
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

    def centralWidgetGridLayout(self):
        self.testBottom1 = QPushButton('test1', self)
        self.testBottom2 = QPushButton('test2', self)

        self.grid = QGridLayout()
        self.grid.addWidget(self.testBottom1, 0, 0)
        self.grid.addWidget(self.testBottom2, 0, 1)

        self.layoutWidget = QWidget()
        self.layoutWidget.setLayout(self.grid)
        self.setCentralWidget(self.layoutWidget)


    def addLocalPath(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./backups/Archives.db')
        db.open()
        query = QSqlQuery()
        query.exec("INSERT INTO LIBINFO (LOCATIONS) values ('{}')".format(self.localPath))
        db.close()

    def createDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./backups/Archives.db')
        db.open()
        query = QSqlQuery()
        query.exec('''CREATE TABLE IF NOT EXISTS LIBINFO(
                LOCATIONS   TEXT    NOT NULL    UNIQUE 
            );''')

        query.exec('''CREATE TABLE IF NOT EXISTS PICTURES(
                PATH        TEXT    PRIMARY KEY NOT NULL UNIQUE ,
                FILENAME    TEXT    NOT NULL ,
                EXIF        TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL
            );''')

        query.exec('''CREATE TABLE IF NOT EXISTS PDFDOC(
                PATH        TEXT    PRIMARY KEY UNIQUE ,
                FILENAME    TEXT    NOT NULL ,
                ARRAGE      TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL
            );''')

        query.exec('''CREATE TABLE IF NOT EXISTS MUSIC(
                PATH        TEXT    PRIMARY KEY UNIQUE ,
                FILENAME    TEXT    NOT NULL ,
                METADATA    TEXT    NOT NULL ,
                THUMBNAIL   TEXT    NOT NULL ,
                ALBUM       TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL ,
                STYLE       TEXT    NOT NULL
            );''')
        db.close()

    def readDB(self):
        #当用户需要从外部导入Archives.db时调用
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