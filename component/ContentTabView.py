from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QTabWidget, QWidget, QListWidget, QListView, QMenu, QAbstractItemView


class contentTabView(QTabWidget):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.initUI()
        self.updateAllPage()

    def initUI(self):
        self.allFileTab = QListView()
        self.allFileTab.setContextMenuPolicy(3)
        self.allFileTab.customContextMenuRequested[QPoint].connect(self.popMenu)

        self.pictureTab = QListView()
        self.updatePicturePage()
        self.pictureTab.setContextMenuPolicy(3)
        self.pictureTab.customContextMenuRequested[QPoint].connect(self.popMenu)

        self.addTab(self.allFileTab, "All")
        self.addTab(self.pictureTab, "Picture")

    def updateAllPage(self):
        self.query.exec("SELECT FILENAME FROM FileLibrary")
        model = QSqlQueryModel()
        model.setQuery(self.query)
        self.allFileTab.setModel(model)

    def updatePicturePage(self):
        self.query.exec("SELECT FILENAME FROM FileLibrary WHERE FILETYPE = PICTURE")
        model = QSqlQueryModel()
        model.setQuery(self.query)
        self.pictureTab.setModel(model)

    def popMenu(self, point):
        qModelIndex = self.allFileTab.indexAt(point)
        item = qModelIndex.data()
        print(item)
        popMenu = QMenu()
        popMenu.addAction("Open file")
        popMenu.addAction("Open the path")
        setTag = QMenu("Tags")
        setRating = QMenu("Rating")
        setRating.addAction("1 star")
        setRating.addAction("2 star")
        setRating.addAction("3 star")
        setRating.addAction("4 star")
        setRating.addAction("5 star")
        setKeyword = QMenu("Keyword")
        popMenu.addMenu(setTag)
        popMenu.addMenu(setRating)
        popMenu.addMenu(setKeyword)
        popMenu.exec(QCursor.pos())