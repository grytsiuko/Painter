from PyQt5.QtGui import *


class Pipette:

    def __init__(self, root):

        self.root = root
        self.render = None

    def start(self, img, x, y):

        pix_map = QPixmap(self.root.scene.width(), self.root.scene.height())
        painter = QPainter(pix_map)
        self.root.scene.render(painter)
        painter.end()

        self.render = pix_map.toImage()
        self.check_pixel(x, y)

    def proceed(self, x, y):

        self.check_pixel(x, y)

    def end(self, x, y):

        self.check_pixel(x, y)

    def check_pixel(self, x, y):

        if x < 0 or y < 0 or x >= self.root.scene.width() or y >= self.root.scene.height():
            return

        color = self.render.pixelColor(x, y)
        self.root.curr_color = color.name()
        self.root.ui.color_button.setStyleSheet('background-color: ' + color.name() + ';')
