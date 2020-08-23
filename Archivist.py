import sys
from PyQt5.QtWidgets import QApplication
import core.FileOperator
import core.StartPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    startPage = core.StartPage.StartPage()
    sys.exit(app.exec_())

# fileOperator = core.FileOperator.FileOperator()
# fileOperator.SearchSelectedPath('.\\tests')
