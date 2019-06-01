from PyQt5 import QtWidgets
import sys

from src.window import Window


class Main:

    @staticmethod
    def run():

        app = QtWidgets.QApplication([])

        window = Window()
        window.show()

        sys.exit(app.exec())
