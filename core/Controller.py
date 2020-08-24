import os
import sys
from PyQt5 import QtCore, QtWidgets
import core.StartPage
import core.MainPage

class Controller():

    curPath = os.getcwd()
    libPathDefault = 'backups/Archives.db'

    def __init__(self):
        pass

    def isInitialized(self):
        if os.path.exists(self.libPathDefault):
            return True
        else:
            False


    def showStartPage(self):
        self.startPage = core.StartPage.StartPage()
        self.startPage.switch_window.connect(self.showMainPage)
        self.startPage.show()

    def showMainPage(self):
        self.mainPage = core.MainPage.MainPage()
        self.mainPage.show()
