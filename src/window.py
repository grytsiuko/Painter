from PyQt5.QtWidgets import *

from src.gui import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curr_color = '#000'
        self.ui.color_button.setStyleSheet('background-color: ' + self.curr_color + ';')

        self.curr_size = 10
        self.min_size = 1
        self.max_size = 100
        self.ui.size_slider.setMinimum(self.min_size)
        self.ui.size_slider.setMaximum(self.max_size)
        self.ui.size_slider.setValue(self.curr_size)
        self.ui.size_spin.setMinimum(self.min_size)
        self.ui.size_spin.setMaximum(self.max_size)
        self.ui.size_spin.setValue(self.curr_size)

        self.ui.color_button.clicked.connect(self.pick_color)

        self.ui.size_slider.valueChanged.connect(self.size_slider_changed)
        self.ui.size_spin.valueChanged.connect(self.size_spin_changed)

    def pick_color(self):

        color = QColorDialog.getColor()
        if color.isValid():
            self.curr_color = color.name()
            self.ui.color_button.setStyleSheet('background-color: ' + self.curr_color + ';')

    def size_slider_changed(self):

        self.curr_size = self.ui.size_slider.value()
        self.ui.size_spin.setValue(self.curr_size)

    def size_spin_changed(self):

        self.curr_size = self.ui.size_spin.value()
        self.ui.size_slider.setValue(self.curr_size)
