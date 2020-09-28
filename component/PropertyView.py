from PyQt5.QtWidgets import QTabWidget, QTreeWidget, QTreeWidgetItem, QListView, QTreeView, QWidget, QGridLayout, \
    QScrollArea, QVBoxLayout

class propertyView(QWidget):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.propertyTree = QTreeWidget()
        self.propertyTree.setColumnCount(2)
        self.propertyTree.setHeaderLabels(['Property', 'Value'])
        self.metadata = QTreeWidgetItem(self.propertyTree)
        self.metadata.setText(0, "Metadata")
        self.attribute = QTreeWidgetItem(self.propertyTree)
        self.attribute.setText(0, "Attribute")

        self.tagsCategory = QTreeWidgetItem()
        self.tagsCategory.setText(0, "Tags")
        self.metadata.addChild(self.tagsCategory)
        self.ratingCategory = QTreeWidgetItem()
        self.ratingCategory.setText(0, "Rating")
        self.metadata.addChild(self.ratingCategory)
        self.keywordCategory = QTreeWidgetItem()
        self.keywordCategory.setText(0, "Keyword")
        self.metadata.addChild(self.keywordCategory)

        vbox.addWidget(self.propertyTree)
        self.setLayout(vbox)
        self.show()

    def showMetadata(self, item):
        self.query.exec("SELECT USERTAGS, RATING, KEYWORDS FROM FileLibrary WHERE FILENAME == '{}'".format(item))
        while self.query.next():
            self.tagsCategory.setText(1, self.query.value(0))
            self.ratingCategory.setText(1, self.query.value(1))
            self.keywordCategory.setText(1, self.query.value(2))