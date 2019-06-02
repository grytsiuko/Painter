from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.gui import Ui_MainWindow
from src.action_functions import ActionFunctions
from src.settings_functions import SettingsFunctions


class Root(QMainWindow):

    def __init__(self):

        super(Root, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set up settings
        self.file_name = None
        self.scene = None
        self.curr_color = '#000'
        self.curr_font = QFont('Arial', 12)
        self.min_size = 1
        self.max_size = 100
        self.curr_size = 10
        self.curr_filled = False

        # actions
        self.action_functions = ActionFunctions(self)
        self.ui.actionNew.triggered.connect(self.action_functions.new_file)
        self.ui.actionOpen.triggered.connect(self.action_functions.open_file)
        self.ui.actionClose.triggered.connect(self.action_functions.close_file)
        self.ui.actionSave.triggered.connect(self.action_functions.save_file)
        self.ui.actionSave_As.triggered.connect(self.action_functions.save_as_file)
        self.ui.actionZoom_In.triggered.connect(self.action_functions.zoom_in)
        self.ui.actionZoom_Out.triggered.connect(self.action_functions.zoom_out)

        # settings
        self.settings_functions = SettingsFunctions(self)
        self.ui.color_button.clicked.connect(self.settings_functions.pick_color)
        self.ui.font_button.clicked.connect(self.settings_functions.pick_font)
        self.ui.size_slider.valueChanged.connect(self.settings_functions.size_slider_changed)
        self.ui.size_spin.valueChanged.connect(self.settings_functions.size_spin_changed)
        self.ui.filled_check.stateChanged.connect(self.settings_functions.filled_changed)
