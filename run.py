from PyQt5 import QtWidgets
import sys

from src.components.root import Root


if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    root = Root()
    root.show()

    sys.exit(app.exec())
