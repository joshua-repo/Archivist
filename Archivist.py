import sys
from PyQt5.QtWidgets import QApplication
import core.Controller


def main():
    app = QApplication(sys.argv)
    controller = core.Controller.Controller()
    if controller.isInitialized():
        controller.showMainPage()
    else:
        controller.showStartPage()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()