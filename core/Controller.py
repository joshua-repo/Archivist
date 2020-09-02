import os
import sys
import core.FileOperator
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
        self.startPage.switchWindow.connect(self.showMainPage) #将switch_window这个信号和showMainPage这个函数连接
        self.startPage.show()

    # def showMainPage(self):
    #     #这个是给Controller下isInitialized调用的
    #     #如果已经初始化完毕，那么将会在Controller里调用一个无参数的showMainPage
    #     self.mainPage = core.MainPage.MainPage()
    #     self.mainPage.show()

    # def showMainPage(self, libPath): #接受一个参数的函数，带有libPath
    #     self.mainPage = core.MainPage.MainPage()
    #     self.mainPage.initializeLib(libPath)
    #     self.mainPage.show()

    def showMainPage(self, *args): #Python的多态是这么实现的
        if args[0] == "": #此时传入的路径是空的，初始化数据库
            self.mainPage = core.MainPage.MainPage()
            self.mainPage.createDB()
            self.mainPage.show()
        else:
            self.mainPage = core.MainPage.MainPage()
            self.mainPage.readDB()
            self.mainPage.show()


    def __del__(self):
        print("Controller is dead.")