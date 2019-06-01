from PyQt5 import QtWidgets
import sys

from src.root import Root


class Main:

    @staticmethod
    def run():

        app = QtWidgets.QApplication([])

        root = Root()
        root.show()

        sys.exit(app.exec())
