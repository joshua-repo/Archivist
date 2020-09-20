import os

import core.FileOperator
import component.ContentTabView
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QListView, QFileDialog, QTabWidget, QAbstractItemView, QMenu, QMessageBox, QAction

class locationView(QTabWidget):
    def __init__(self, query, linkToMainView):
        super().__init__()
        self.query = query
        self.linkToMainView = linkToMainView
        self.initUI()

    def initUI(self):
        self.localLocation = QListView()
        self.updateLocationView()
        self.localLocation.setContextMenuPolicy(3)
        self.localLocation.customContextMenuRequested[QPoint].connect(self.localLcationPopMenu)

        self.netLocation = QListView()

        self.addTab(self.localLocation, "Local")
        self.addTab(self.netLocation, "Net")

    def updateLocationView(self):
        self.query.exec("SELECT * FROM HostedDirectory")
        model = QSqlQueryModel()
        model.setQuery(self.query)
        self.localLocation.setModel(model)

    def addLocalPath(self):
        localPath = QFileDialog.getExistingDirectory(self, 'Select the Directory', '/')
        self.query.exec("INSERT INTO HostedDirectory (LOCATION) VALUES ('{}')".format(localPath))
        core.FileOperator.searchPath(localPath, self.query)
        self.updateLocationView()
        self.linkToMainView.updateAllPage()

    def addLocalFile(self):
        localFile = QFileDialog.getOpenFileName(self, 'Select the File', '/')
        PATH = localFile[0]
        FILENAME = os.path.split(localFile[0])[-1]
        SUFFIX = os.path.splitext(localFile[0])[-1]
        ROOT = ""
        FILETYPE = ""
        USERTAGS = ""
        RATING = ""
        KEYWORD = ""
        self.query.exec("INSERT INTO FileLibrary ("
                        "PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAGS, RATING, KEYWORD"
                        ") VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAGS, RATING, KEYWORD
        ))
        self.linkToMainView.updateAllPage()

    def localLcationPopMenu(self, point):
        qModelIndex = self.localLocation.indexAt(point)
        self.localLacationitem = qModelIndex.data()
        print(self.localLacationitem)
        if self.localLacationitem == None:
            popMenu = QMenu()
            popMenu.addAction("Add a Local Path").triggered.connect(self.addLocalPath)
            popMenu.addAction("Add a Local File").triggered.connect(self.addLocalFile)
            popMenu.exec(QCursor.pos())
        else:
            popMenu = QMenu()
            popMenu.addAction("Remove the Path").triggered.connect(self.removePath)
            popMenu.exec(QCursor.pos())

    def removePath(self):
        reply = QMessageBox.question(self, "Remove Path", "Do you wish to remove this path?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.query.exec("DELETE FROM HostedDirectory WHERE LOCATION = ('{}')".format(self.localLacationitem))
            self.updateLocationView()
            self.query.exec("DELETE FROM FileLibrary WHERE ROOT = ('{}')".format(self.localLacationitem))
            self.linkToMainView.updateAllPage()
        if reply == QMessageBox.No:
            pass
