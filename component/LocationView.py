import os

import core.FileOperator
import component.ContentView
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QListView, QFileDialog, QTabWidget, QAbstractItemView, QMenu, QMessageBox, QAction

class locationView(QTabWidget):
    def __init__(self, query, contentView):
        super().__init__()
        self.query = query
        self.contentView = contentView
        self.initUI()

    def initUI(self):
        self.localLocationTab = QListView()
        self.updateLocationView()
        self.localLocationTab.setContextMenuPolicy(3)
        self.localLocationTab.customContextMenuRequested[QPoint].connect(self.localLcationPopMenu)

        self.netLocation = QListView()

        self.addTab(self.localLocationTab, "Local")
        self.addTab(self.netLocation, "Net")

    def updateLocationView(self):
        self.query.exec("SELECT * FROM HostedDirectory")
        model = QSqlQueryModel()
        model.setQuery(self.query)
        self.localLocationTab.setModel(model)

    def addLocalPath(self):
        localPath = QFileDialog.getExistingDirectory(self, 'Select the Directory', '/')
        if localPath == '':
            pass
        else:
            self.query.exec("INSERT INTO HostedDirectory (LOCATION) VALUES ('{}')".format(localPath))
            core.FileOperator.searchPath(localPath, self.query)
            self.updateLocationView()
            self.contentView.updateAllPage()

    def addLocalFile(self):
        localFile = QFileDialog.getOpenFileName(self, 'Select the File', '/')
        if localFile == '':
            pass
        else:
            PATH = localFile[0]
            FILENAME = os.path.split(localFile[0])[-1]
            SUFFIX = os.path.splitext(localFile[0])[-1]
            ROOT = ""
            FILETYPE = ""
            USERTAGS = ""
            RATING = ""
            KEYWORD = ""
            self.query.exec("INSERT INTO FileLibrary ("
                            "PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAGS, RATING, KEYWORDS"
                            ") VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAGS, RATING, KEYWORD
            ))
            self.contentView.updateAllPage()

    def localLcationPopMenu(self, point):
        qModelIndex = self.localLocationTab.indexAt(point)
        self.localLacationitem = qModelIndex.data()
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
            self.contentView.updateAllPage()
        if reply == QMessageBox.No:
            pass
