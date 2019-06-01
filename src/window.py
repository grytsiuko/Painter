from PyQt5.QtWidgets import *

from src.gui import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curr_color = '#000'
        self.ui.color_button.setStyleSheet('background-color: ' + self.curr_color + ';')

        self.ui.color_button.clicked.connect(self.pick_color)

    def pick_color(self):

        color = QColorDialog.getColor()
        if color.isValid():
            self.curr_color = color.name()
            self.ui.color_button.setStyleSheet('background-color: ' + self.curr_color + ';')
