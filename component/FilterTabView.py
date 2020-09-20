from PyQt5.QtWidgets import QTabWidget, QListWidget

class filterTabView(QTabWidget):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.initUI()

    def initUI(self):
        self.tagsTab = QListWidget()
        self.ratingTab = QListWidget()
        self.keywordTab = QListWidget()

        self.addTab(self.tagsTab, "Tags")
        self.addTab(self.ratingTab, "Rating")
        self.addTab(self.keywordTab, "Keyword")
