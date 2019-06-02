from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SettingsFunctions:

    def __init__(self, root):

        self.root = root
        self.root.ui.color_button.setStyleSheet('background-color: ' + self.root.curr_color + ';')
        self.set_font_button_text()
        self.root.ui.filled_check.setChecked(self.root.curr_filled)
        self.root.ui.size_slider.setMinimum(self.root.min_size)
        self.root.ui.size_slider.setMaximum(self.root.max_size)
        self.root.ui.size_slider.setValue(self.root.curr_size)
        self.root.ui.size_spin.setMinimum(self.root.min_size)
        self.root.ui.size_spin.setMaximum(self.root.max_size)
        self.root.ui.size_spin.setValue(self.root.curr_size)

    def pick_color(self):

        color = QColorDialog.getColor()
        if color.isValid():
            self.root.curr_color = color.name()
            self.root.ui.color_button.setStyleSheet('background-color: ' + self.root.curr_color + ';')

    def set_font_button_text(self):

        button_font = QFont(self.root.curr_font)
        button_font.setPointSize(11)
        self.root.ui.font_button.setText(str(self.root.curr_font.pointSize()) +
                                         ' ' + self.root.curr_font.family()[0:10])
        self.root.ui.font_button.setFont(button_font)

    def pick_font(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.root.curr_font = font
            self.set_font_button_text()

    def size_slider_changed(self):

        self.root.curr_size = self.root.ui.size_slider.value()
        self.root.ui.size_spin.setValue(self.root.curr_size)

    def size_spin_changed(self):

        self.root.curr_size = self.root.ui.size_spin.value()
        self.root.ui.size_slider.setValue(self.root.curr_size)

    def filled_changed(self):

        self.root.curr_filled = bool(self.root.ui.filled_check.checkState())
