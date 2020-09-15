import os
import component.StartPage
import component.MainPage

class Controller():

    curPath = os.getcwd()
    libPathDefault = 'core/Archives.db'

    def __init__(self):
        pass

    def isInitialized(self):
        if os.path.exists(self.libPathDefault):
            return True
        else:
            False

    def showStartPage(self):
        self.startPage = component.StartPage.StartPage()
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
        # 此时传入tuple为空，这是Archives.db被初始化后的情况
        # 此时传入的tuple为非空，它有一个为空的元素,这是没有选取任何路径的情况
        # 首先判断是否为空，若不为空则说明可能含有一个为空的元素
        # 若为空，则为初始化之后的情况
        if args:
            if args[0] == "":
                self.mainPage = component.MainPage.MainPage()
                self.mainPage.createDB()
                self.mainPage.show()
        else:
            self.mainPage = component.MainPage.MainPage()
            self.mainPage.readDB(args)
            self.mainPage.show()

    def __del__(self):
        print("Controller is dead.")