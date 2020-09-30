from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import QTabWidget, QListWidget, QListWidgetItem

class filterTabView(QTabWidget):
    def __init__(self, query, contentView, TAGS, KEYWORDS):
        super().__init__()
        self.query = query
        self.TAGS = TAGS
        self.KEYWORDS = KEYWORDS
        self.contentView = contentView
        self.initList()
        self.initUI()

    def initUI(self):
        self.tagsTab = QListWidget()
        for tag in self.TAGS:
            item = QListWidgetItem(tag)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tagsTab.addItem(item)
        self.tagsTab.clicked.connect(self.tagsSelect)

        self.ratingTab = QListWidget()
        for word in ['1 star', '2 star', '3 star', '4 star', '5 star']:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ratingTab.addItem(item)
        self.ratingTab.clicked.connect(self.ratingSelect)

        self.keywordTab = QListWidget()
        for keyword in self.KEYWORDS:
            item = QListWidgetItem(keyword)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.keywordTab.addItem(item)
        self.keywordTab.clicked.connect(self.keywordSelect)

        self.addTab(self.tagsTab, "Tags")
        self.addTab(self.ratingTab, "Rating")
        self.addTab(self.keywordTab, "Keyword")

    def initList(self):
        self.tagsList = []
        self.ratingsList = []
        self.keywordsList = []

    def tagsSelect(self, point):
        item = point.data()
        if self.tagsTab.itemFromIndex(point).checkState() == 2:
            if item in self.tagsList:
                pass
            else:
                self.tagsList.append(item)
        if self.tagsTab.itemFromIndex(point).checkState() == 0:
            if item in self.tagsList:
                self.tagsList.remove(item)
        self.contentView.updateAllPage(self.tagsList, self.ratingsList, self.keywordsList)

    def ratingSelect(self, point):
        item = point.data()
        if self.ratingTab.itemFromIndex(point).checkState() == 2:
            if item in self.ratingsList:
                pass
            else:
                self.ratingsList.append(item)
        if self.ratingTab.itemFromIndex(point).checkState() == 0:
            if item in self.ratingsList:
                self.ratingsList.remove(item)
        self.contentView.updateAllPage(self.tagsList, self.ratingsList, self.keywordsList)

    def keywordSelect(self, point):
        item = point.data()
        if self.keywordTab.itemFromIndex(point).checkState() == 2:
            if item in self.keywordsList:
                pass
            else:
                self.keywordsList.append(item)
        if self.keywordTab.itemFromIndex(point).checkState() == 0:
            if item in self.keywordsList:
                self.keywordsList.remove(item)
        self.contentView.updateAllPage(self.tagsList, self.ratingsList, self.keywordsList)