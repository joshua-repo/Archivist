from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt

import component.ContentTabView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QMessageBox, QDesktopWidget, QMainWindow, QMenu, QFileDialog, QGridLayout, QAction, \
    QTableView, QListView, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QCursor


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initDB()
        self.initUI()
        self.displayLocation()

    def initDB(self):
        # 建立一个全局的连接
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./core/Archives.db')
        self.db.open()
        self.query = QSqlQuery()

    def initUI(self):
        self.menuBarInit()
        self.centralWidgetGridLayout()

        self.resize(1800, 950)
        self.center()
        self.setWindowTitle('Archivist')
        self.setWindowIcon(QIcon('./resource/icon.png'))

    def displayLocation(self):
        # 刷新location显示页面
        self.query.prepare("SELECT * FROM LIBINFO")
        self.query.exec()
        model = QSqlQueryModel()
        model.setQuery(self.query)
        self.locationView.setModel(model)

    def menuBarInit(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')

        #fileMenu
        addLibMenu = QMenu('Add a new path to library', self)
        addLocal = QAction('Local Path', self)
        addLocal.triggered.connect(self.addLocalPath)
        addURL = QAction('From Internet', self)
        addDisk = QAction('Whole Disk', self)
        addLibMenu.addAction(addLocal)
        addLibMenu.addAction(addURL)
        addLibMenu.addAction(addDisk)

        addFile = QAction('Add a new file to library', self)
        addFile.triggered.connect(self.addLocalFile)
        addNewType = QAction('Add a new file type', self)
        addNewType.triggered.connect(self.addNewFileType)

        #searchFile = QAction('Search File', self)

        importLib = QAction('Import the library', self)
        exportLib = QAction('Export the library', self)

        fileMenu.addMenu(addLibMenu)
        fileMenu.addAction(addFile)
        fileMenu.addAction(addNewType)
        #fileMenu.addAction(searchFile)
        fileMenu.addAction(importLib)
        fileMenu.addAction(exportLib)

        #editMenu
        addNewTagMenu = QMenu('Add A New Tag', self)
        addNewTag = QAction('Tag', self)
        addNewRating = QAction('Rating', self)
        addNewKeyword = QAction('Keyword', self)
        addNewTagMenu.addAction(addNewTag)
        addNewTagMenu.addAction(addNewRating)
        addNewTagMenu.addAction(addNewKeyword)
        selectAll = QAction('Select All', self)
        preference = QAction('Preference', self)

        editMenu.addMenu(addNewTagMenu)
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
        self.locationLabel = QLabel('Locations')
        self.filterLabel = QLabel('Filter')
        self.metadataLabel = QLabel('Metadata')
        self.previewLabel = QLabel('Preview')

        self.locationView = QListView()
        self.locationView.doubleClicked.connect(self.removePath)
        self.filterView = QTableView()
        self.mainView = component.ContentTabView.contentTabView(self.query)
        self.previewView = QTableView()
        self.metadateView = QListView()

        self.grid = QGridLayout()
        self.grid.addWidget(self.locationLabel, 0, 0)
        self.grid.addWidget(self.locationView, 1, 0)
        self.grid.addWidget(self.filterLabel, 2, 0)
        self.grid.addWidget(self.filterView, 3, 0)
        # addWidget(self, QWidget, row, column, rowSpan, columnSpan) 可以被这样重载
        # rowSpan, columnSpan 代表跨行，跨列
        # 参数-1代表直接将view延伸至底部
        self.grid.addWidget(self.mainView, 0, 1, -1, 1)
        self.grid.addWidget(self.previewLabel, 0, 2)
        self.grid.addWidget(self.previewView, 1, 2, 1, 2)
        self.grid.addWidget(self.metadataLabel, 2, 2)
        self.grid.addWidget(self.metadateView, 3, 2)

        #设置缩放因子，让中间页面更大一些
        self.grid.setColumnStretch(1, 1)

        self.layoutWidget = QWidget()
        self.layoutWidget.setLayout(self.grid)
        self.setCentralWidget(self.layoutWidget)

    def displayMetadata(self):
        pass

    def addLocalPath(self):
        localPath = QFileDialog.getExistingDirectory(self, 'Select the directory', '/')
        self.query.exec("INSERT INTO HostedDirectory (LOCATIONS) VALUES ('{}')".format(localPath))
        self.displayLocation()


    def addLocalFile(self):
        localFile = QFileDialog.getOpenFileName(self, 'Select the file', '/')
        self.query.exec("INSERT INTO SingalFiles (LOCATIONS) VALUES ('{}')".format(localFile))

    def addNewFileType(self):
        pass

    def removePath(self, qModelIndex):
        reply = QMessageBox.question(self, 'Remove Path', 'Do you wish to remove this path?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.query.exec("DELETE FROM LIBINFO WHERE LOCATIONS = ('{}')".format(qModelIndex.data()))
            self.displayLocation()
        else:
            pass

    def createDB(self):
        self.query.exec('''CREATE TABLE IF NOT EXISTS HostedDirectory(
                LOCATIONS   TEXT    NOT NULL    UNIQUE
            );''')

        self.query.exec('''CREATE TABLE IF NOT EXISTS SingalFiles(
                LOCATIONS   TEXT    NOT NULL    UNIQUE 
        );''')

        self.query.exec('''CREATE TABLE IF NOT EXISTS Pictures(
                PATH        TEXT    PRIMARY KEY NOT NULL UNIQUE ,
                FILENAME    TEXT    NOT NULL ,
                EXIF        TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL ,
                RATING      TEXT    NOT NULL ,
                KEYWORD     TEXT    NOT NULL 
            );''')

        self.query.exec('''CREATE TABLE IF NOT EXISTS PDFDocs(
                PATH        TEXT    PRIMARY KEY UNIQUE ,
                FILENAME    TEXT    NOT NULL ,
                ARRAGE      TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL
            );''')

        self.query.exec('''CREATE TABLE IF NOT EXISTS Music(
                PATH        TEXT    PRIMARY KEY UNIQUE ,
                FILENAME    TEXT    NOT NULL ,
                METADATA    TEXT    NOT NULL ,
                THUMBNAIL   TEXT    NOT NULL ,
                ALBUM       TEXT    NOT NULL ,
                STYLE       TEXT    NOT NULL ,
                USERTAGS    TEXT    NOT NULL ,
                RATING      TEXT    NOT NULL ,
                KEYWORD     TEXT    NOT NULL 
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
