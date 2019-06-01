from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.gui import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = None

        self.curr_color = '#000'
        self.ui.color_button.setStyleSheet('background-color: ' + self.curr_color + ';')

        self.curr_font = QFont('Arial', 12)
        self.set_font_button_text()

        self.curr_size = 10
        self.min_size = 1
        self.max_size = 100
        self.ui.size_slider.setMinimum(self.min_size)
        self.ui.size_slider.setMaximum(self.max_size)
        self.ui.size_slider.setValue(self.curr_size)
        self.ui.size_spin.setMinimum(self.min_size)
        self.ui.size_spin.setMaximum(self.max_size)
        self.ui.size_spin.setValue(self.curr_size)

        self.curr_filled = False
        self.ui.filled_check.setChecked(self.curr_filled)

        # actions
        self.ui.actionOpen.triggered.connect(self.open_file)

        # settings
        self.ui.color_button.clicked.connect(self.pick_color)
        self.ui.font_button.clicked.connect(self.pick_font)
        self.ui.size_slider.valueChanged.connect(self.size_slider_changed)
        self.ui.size_spin.valueChanged.connect(self.size_spin_changed)
        self.ui.filled_check.stateChanged.connect(self.filled_changed)

    def close_file(self):

        pass

    def open_file(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                   "Images (*.jpg *.jpeg *.png)",
                                                   options=options)
        if file_name:
            self.close_file()
            self.scene = QGraphicsScene()
            self.ui.graphicsView.setScene(self.scene)
            img = QGraphicsPixmapItem(QPixmap(file_name))
            self.scene.addItem(img)

    def pick_color(self):

        color = QColorDialog.getColor()
        if color.isValid():
            self.curr_color = color.name()
            self.ui.color_button.setStyleSheet('background-color: ' + self.curr_color + ';')

    def set_font_button_text(self):

        button_font = QFont(self.curr_font)
        button_font.setPointSize(11)
        self.ui.font_button.setText(str(self.curr_font.pointSize()) +
                                    ' ' + self.curr_font.family()[0:10])
        self.ui.font_button.setFont(button_font)

    def pick_font(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.curr_font = font
            self.set_font_button_text()

    def size_slider_changed(self):

        self.curr_size = self.ui.size_slider.value()
        self.ui.size_spin.setValue(self.curr_size)

    def size_spin_changed(self):

        self.curr_size = self.ui.size_spin.value()
        self.ui.size_slider.setValue(self.curr_size)

    def filled_changed(self):

        self.curr_filled = bool(self.ui.filled_check.checkState())
