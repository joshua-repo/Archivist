import sys
#import qdarkstyle
from PyQt5.QtWidgets import QApplication
import core.Controller
import core.FileOperator
import core.StartPage
import core.MainPage


def main():
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    controller = core.Controller.Controller()
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
