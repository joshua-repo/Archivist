from PyQt5 import QtCore
from PyQt5.QtWidgets import QTabWidget, QListWidget, QListWidgetItem

class filterTabView(QTabWidget):
    def __init__(self, query, contentView, TAGS, KEYWORDS):
        super().__init__()
        self.query = query
        self.TAGS = TAGS
        self.KEYWORDS = KEYWORDS
        self.initUI()

    def initUI(self):
        self.tagsTab = QListWidget()
        for tag in self.TAGS:
            item = QListWidgetItem(tag)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tagsTab.addItem(item)

        self.ratingTab = QListWidget()
        for word in ['1 star', '2 star', '3 star', '4 star', '5 star']:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ratingTab.addItem(item)

        self.keywordTab = QListWidget()
        for keyword in self.KEYWORDS:
            item = QListWidgetItem(keyword)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.keywordTab.addItem(item)

        self.addTab(self.tagsTab, "Tags")
        self.addTab(self.ratingTab, "Rating")
        self.addTab(self.keywordTab, "Keyword")
