from src.tools.pencil import Pencil
from src.tools.brush import Brush
from src.tools.eraser import Eraser
from src.tools.pipette import Pipette
from src.tools.can import Can
from src.tools.line import Line
from src.tools.rect import Rect
from src.tools.oval import Oval
from src.tools.spray import Spray
from src.tools.text import Text


class ToolsFunctions:

    def __init__(self, root):

        self.root = root
        self.buttons = self.root.ui.buttonGroup.buttons()
        self.button_bg = '#eee'
        self.button_selected_bg = '#bbb'

    def restore_gui(self):

        for button in self.buttons:
            button.setStyleSheet('background-color: ' + self.button_bg + ';')

        self.disable_size(True)
        self.disable_filled(True)
        self.disable_font(True)
        self.disable_text(True)

    def disable_size(self, boolean):

        self.root.ui.size_label.setDisabled(boolean)
        self.root.ui.size_spin.setDisabled(boolean)
        self.root.ui.size_slider.setDisabled(boolean)

    def disable_filled(self, boolean):

        self.root.ui.filled_label.setDisabled(boolean)
        self.root.ui.filled_check.setDisabled(boolean)

    def disable_font(self, boolean):

        self.root.ui.font_label.setDisabled(boolean)
        self.root.ui.font_button.setDisabled(boolean)

    def disable_text(self, boolean):

        self.root.ui.text_label.setDisabled(boolean)
        self.root.ui.text_edit.setDisabled(boolean)

    def choose_pencil(self):

        self.root.curr_tool = Pencil(self.root)
        self.restore_gui()
        self.root.ui.pencil_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_brush(self):

        self.root.curr_tool = Brush(self.root)
        self.restore_gui()
        self.root.ui.brush_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_size(False)

    def choose_eraser(self):

        self.root.curr_tool = Eraser(self.root)
        self.restore_gui()
        self.root.ui.eraser_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_size(False)

    def choose_pipette(self):

        self.root.curr_tool = Pipette(self.root)
        self.restore_gui()
        self.root.ui.pipette_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_can(self):

        self.root.curr_tool = Can(self.root)
        self.restore_gui()
        self.root.ui.can_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_line(self):

        self.root.curr_tool = Line(self.root)
        self.restore_gui()
        self.root.ui.line_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_size(False)

    def choose_rect(self):

        self.root.curr_tool = Rect(self.root)
        self.restore_gui()
        self.root.ui.rect_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_filled(False)

    def choose_oval(self):

        self.root.curr_tool = Oval(self.root)
        self.restore_gui()
        self.root.ui.oval_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_filled(False)

    def choose_spray(self):

        self.root.curr_tool = Spray(self.root)
        self.restore_gui()
        self.root.ui.spray_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_size(False)

    def choose_text(self):

        self.root.curr_tool = Text(self.root)
        self.restore_gui()
        self.root.ui.text_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
        self.disable_font(False)
        self.disable_text(False)
