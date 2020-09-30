import os

import component.LocationView
import component.ContentView
import component.FilterView
import component.PropertyView
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QMessageBox, QDesktopWidget, QMainWindow, QMenu, QFileDialog, QGridLayout, QAction, \
    QTableView, QListView, QLabel, QLineEdit, QListWidget
from PyQt5.QtGui import QIcon, QCursor

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initDB()
        self.initUI()

    def initDB(self):
        # 建立一个全局的连接
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./core/Archives.db')
        self.db.open()
        self.query = QSqlQuery()
        self.TAGS = ['Black', 'Blue', 'Brown', 'Green', 'Red', 'Yellow']
        self.KEYWORDS = ['To-Do', 'Favorite', 'Important', 'Wasted']

    def initUI(self):
        self.menuBarInit()
        self.centralWidgetGridLayout()

        self.resize(1000, 650)
        self.center()
        self.setWindowTitle('Archivist')
        self.setWindowIcon(QIcon('./resource/icon.png'))
        
    def menuBarInit(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')

        #fileMenu
        addLibMenu = QMenu('Add a new path to library', self)
        addLocal = QAction('Local Path', self)
        addLocal.triggered.connect(self.addLocalPath)
        addURL = QAction('From Netdisk', self)
        addDisk = QAction('Whole Disk', self)
        addLibMenu.addAction(addLocal)
        addLibMenu.addAction(addURL)
        addLibMenu.addAction(addDisk)

        addFile = QAction('Add a new file to library', self)
        addFile.triggered.connect(self.addLocalFile)
        addNewType = QAction('Add a new file type', self)
        addNewType.triggered.connect(self.addNewFileType)

        importLib = QAction('Import the library', self)
        importLib.triggered.connect(self.importLibrary)
        exportLib = QAction('Export the library', self)
        exportLib.triggered.connect(self.exportLibrary)

        fileMenu.addMenu(addLibMenu)
        fileMenu.addAction(addFile)
        fileMenu.addAction(addNewType)
        fileMenu.addAction(importLib)
        fileMenu.addAction(exportLib)

        #editMenu
        addNewTag = QAction('Add a Tag', self)
        addNewKeword = QAction("Add a Keyword", self)
        addNewTab = QAction("Add a New Tab", self)
        selectAll = QAction('Select All', self)
        preference = QAction('Preference', self)

        editMenu.addAction(addNewTag)
        editMenu.addAction(addNewKeword)
        editMenu.addAction(selectAll)
        editMenu.addAction(preference)

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
        ratingOrder = QAction('Rating', self)
        keywordsOrder = QAction('Keywords', self)
        sortMenu.addAction(nameOrder)
        sortMenu.addAction(sizeOrder)
        sortMenu.addAction(typeOrder)
        sortMenu.addAction(dataOrder)
        sortMenu.addAction(tagsOrder)
        sortMenu.addAction(ratingOrder)
        sortMenu.addAction(keywordsOrder)

        viewMenu.addMenu(iconSizeMenu)
        viewMenu.addMenu(sortMenu)
        
    def centralWidgetGridLayout(self):
        #contentView
        self.contentView = component.ContentView.contentView(self.query, self.TAGS, self.KEYWORDS)

        #locationView
        self.locationView = component.LocationView.locationView(self.query, self.contentView)

        #filterView
        self.filterView = component.FilterView.filterTabView(self.query, self.contentView, self.TAGS, self.KEYWORDS)

        #previewView
        self.previewView = QTableView()

        #infomationView
        self.propertyView = component.PropertyView.propertyView(self.query)

        self.contentView.getPreviewView(self.previewView)
        self.contentView.getPropertyView(self.propertyView)

        grid = QGridLayout()
        grid.addWidget(self.locationView, 0, 0)
        grid.addWidget(self.filterView, 1, 0)
        # addWidget(self, QWidget, row, column, rowSpan, columnSpan) 可以被这样重载
        # rowSpan, columnSpan 代表跨行，跨列
        # 参数-1代表直接将view延伸至底部
        grid.addWidget(self.contentView, 0, 1, -1, 1)
        grid.addWidget(self.previewView, 0, 2)
        grid.addWidget(self.propertyView, 1, 2)

        #设置缩放因子，让中间页面更大一些
        grid.setColumnStretch(1, 1)

        layoutWidget = QWidget()
        layoutWidget.setLayout(grid)
        self.setCentralWidget(layoutWidget)



    def addLocalPath(self):
        self.locationView.addLocalPath()

    def addLocalFile(self):
        self.locationView.addLocalFile()

    def addNewFileType(self):
        pass

    def importLibrary(self):
        pass

    def exportLibrary(self):
        pass

    def createDB(self):
        self.query.exec('''CREATE TABLE IF NOT EXISTS TagInfo(
            TAG     TEXT    PRIMARY KEY NOT NULL UNIQUE 
        );''')

        self.query.exec('''CREATE TABLE IF NOT EXISTS KeywordInfo(
            KEYWORDS TEXT    PRIMARY KEY NOT NULL UNIQUE 
        );''')

        for word in self.TAGS:
            self.query.exec("INSERT INTO TagInfo VALUES ('{}')".format(word))

        for word in self.KEYWORDS:
            self.query.exec("INSERT INTO KeywordInfo VALUES ('{}')".format(word))

        self.query.exec('''CREATE TABLE IF NOT EXISTS HostedDirectory(
            LOCATION    TEXT    NOT NULL    UNIQUE
            );''')

        self.query.exec('''CREATE TABLE IF NOT EXISTS FileLibrary(
            PATH        TEXT    PRIMARY KEY NOT NULL UNIQUE ,
            FILENAME    TEXT    NOT NULL ,
            SUFFIX      TEXT    NOT NULL ,
            ROOT        TEXT    NOT NULL ,
            FILETYPE    TEXT    NOT NULL ,
            USERTAGS    TEXT    NOT NULL ,
            RATING      TEXT    NOT NULL ,
            KEYWORDS     TEXT    NOT NULL 
            );''')

    def readDB(self, libpath):
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

    def __del__(self):
        self.db.close()
