from PyQt5.QtWidgets import QTabWidget, QWidget

class contentTabView(QTabWidget):
    def __init__(self, query):
        super().__init__()
        self.initUI(query)

    def initUI(self, query):
        self.picTab = QWidget()
        self.musicTab = QWidget()
        self.pdfTab = QWidget()

        self.addTab(self.picTab, "Picture")
        self.addTab(self.musicTab, "Music")
        self.addTab(self.pdfTab, "PDF")

    def picUI(self):
        pass

    def musicUI(self):
        pass

    def pdfUI(self):
        pass
