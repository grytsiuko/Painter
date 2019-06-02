from PyQt5.QtWidgets import *

from src.gui.gui_new_file_dialog import Ui_Dialog


class NewFileDialog(QDialog):

    def __init__(self):

        super(NewFileDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.width_spin.setMinimum(1)
        self.ui.height_spin.setMinimum(1)
        self.ui.width_spin.setMaximum(2000)
        self.ui.height_spin.setMaximum(2000)
        self.ui.width_spin.setValue(640)
        self.ui.height_spin.setValue(400)
