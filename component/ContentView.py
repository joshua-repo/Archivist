from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QTabWidget, QWidget, QListWidget, QListView, QMenu, QAbstractItemView

class contentView(QTabWidget):
    def __init__(self, query, TAGS, KEYWORDS):
        super().__init__()
        self.query = query
        self.TAGS = TAGS
        self.KEYWORDS = KEYWORDS
        self.initUI()
        self.updateAllPage()

    def initUI(self):
        self.allFileTab = QListView()
        self.allFileTab.clicked.connect(self.showInfo)
        self.allFileTab.setContextMenuPolicy(3)
        self.allFileTab.customContextMenuRequested[QPoint].connect(self.popMenu)

        self.pictureTab = QListView()
        self.pictureTab.setContextMenuPolicy(3)
        self.pictureTab.customContextMenuRequested[QPoint].connect(self.popMenu)

        self.addTab(self.allFileTab, "All")
        self.addTab(self.pictureTab, "Picture")

    def updateAllPage(self):
        self.query.exec("SELECT FILENAME FROM FileLibrary WHERE SUFFIX != ('{}')".format(""))
        #如果是目录，会被排除掉
        model = QSqlQueryModel()
        model.setQuery(self.query)
        self.allFileTab.setModel(model)

    def popMenu(self, point):
        qModelIndex = self.allFileTab.indexAt(point)
        self.item = qModelIndex.data()
        popMenu = QMenu()
        popMenu.addAction("Open File")
        popMenu.addAction("Open the Path")
        popMenu.addAction("Remove the File").triggered.connect(self.removeFile)

        setTag = QMenu("Tags")
        for tag in self.TAGS:
            setTag.addAction(tag).triggered.connect(self.setTag)

        setRating = QMenu("Rating")
        for rating in ["1 star", "2 star", "3 star", "4 star", "5 star"]:
            setRating.addAction(rating).triggered.connect(self.setRating)

        setKeyword = QMenu("Keyword")
        for keyword in self.KEYWORDS:
            setKeyword.addAction(keyword).triggered.connect(self.setKeyword)

        popMenu.addMenu(setTag)
        popMenu.addMenu(setRating)
        popMenu.addMenu(setKeyword)
        popMenu.exec(QCursor.pos())

    def showInfo(self, point):
        item = point.data()
        self.propertyView.showMetadata(item)

    def removeFile(self):
        pass

    def setTag(self):
        tag = self.sender().text()
        self.query.exec("UPDATE FileLibrary SET USERTAGS = '{}' WHERE FILENAME == '{}'".format(tag, self.item))

    def setRating(self):
        rating = self.sender().text()
        self.query.exec("UPDATE FileLibrary SET RATING = '{}' WHERE FILENAME == '{}'".format(rating, self.item))

    def setKeyword(self):
        keyword = self.sender().text()
        self.query.exec("UPDATE FileLibrary SET KEYWORDS = '{}' WHERE FILENAME == '{}'".format(keyword, self.item))

    def getPreviewView(self, previewView):
       self.previewView = previewView

    def getPropertyView(self, propertyView):
        self.propertyView = propertyView