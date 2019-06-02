from PyQt5 import QtWidgets
import PyQt5
import os
import sys

from src.components.root import Root


if __name__ == '__main__':

    # for Windows
    pyqt = os.path.dirname(PyQt5.__file__)
    QtWidgets.QApplication.addLibraryPath(os.path.join(pyqt, "Qt", "plugins"))

    app = QtWidgets.QApplication([])

    root = Root()
    root.show()

    sys.exit(app.exec())
