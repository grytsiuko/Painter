from PyQt5.QtWidgets import *

from src.gui.gui_exit_dialog import Ui_Dialog


class ExitDialog(QDialog):

    def __init__(self):

        super(ExitDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
