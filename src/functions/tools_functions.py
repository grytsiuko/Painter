from src.tools.pencil import Pencil
from src.tools.brush import Brush
from src.tools.eraser import Eraser
from src.tools.pipette import Pipette
from src.tools.can import Can
from src.tools.line import Line


class ToolsFunctions:

    def __init__(self, root):

        self.root = root
        self.buttons = self.root.ui.buttonGroup.buttons()
        self.button_bg = '#eee'
        self.button_selected_bg = '#bbb'

    def restore_buttons(self):

        for button in self.buttons:
            button.setStyleSheet('background-color: ' + self.button_bg + ';')

    def choose_pencil(self):

        self.root.curr_tool = Pencil(self.root)
        self.restore_buttons()
        self.root.ui.pencil_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_brush(self):

        self.root.curr_tool = Brush(self.root)
        self.restore_buttons()
        self.root.ui.brush_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_eraser(self):

        self.root.curr_tool = Eraser(self.root)
        self.restore_buttons()
        self.root.ui.eraser_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_pipette(self):

        self.root.curr_tool = Pipette(self.root)
        self.restore_buttons()
        self.root.ui.pipette_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_can(self):

        self.root.curr_tool = Can(self.root)
        self.restore_buttons()
        self.root.ui.can_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')

    def choose_line(self):

        self.root.curr_tool = Line(self.root)
        self.restore_buttons()
        self.root.ui.line_button.setStyleSheet('background-color: ' + self.button_selected_bg + ';')
