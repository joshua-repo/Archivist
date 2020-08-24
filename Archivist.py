import sys
from PyQt5.QtWidgets import QApplication
import core.Controller
import core.FileOperator
import core.StartPage
import core.MainPage


def main():
    app = QApplication(sys.argv)
    controller = core.Controller.Controller()
#    controller.showStartPage()
    if controller.isInitialized():
        controller.showMainPage()
    else:
        controller.showStartPage()
    sys.exit(app.exec_())

def fileOperatorTest():
    fileOperator = core.FileOperator.FileOperator()
    fileOperator.SearchSelectedPath('./tests')

if __name__ == '__main__':
    main()
    #fileOperatorTest()
