from PyQt5.QtGui import *

from src.tools.tool import Tool


class Pipette(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        pix_map = QPixmap(self.root.scene.width(), self.root.scene.height())
        painter = QPainter(pix_map)
        self.root.scene.render(painter)
        painter.end()

        self.render = pix_map.toImage()

    def execute(self, x, y):

        if x < 0 or y < 0 or x >= self.root.scene.width() or y >= self.root.scene.height():
            return

        color = self.render.pixelColor(x, y)
        self.root.curr_color = color.name()
        self.root.ui.color_button.setStyleSheet('background-color: ' + color.name() + ';')
