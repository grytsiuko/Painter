from PyQt5.QtGui import *
from PIL import ImageColor

from src.tools.tool import Tool


class Can(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        pix_map = QPixmap(self.root.scene.width(), self.root.scene.height())
        painter = QPainter(pix_map)
        self.root.scene.render(painter)
        painter.end()

        self.render = pix_map.toImage()
        self.matrix = img.load()

    def start(self, x, y):

        pass

    def proceed(self, x, y):

        pass

    def end(self, x, y):

        if x < 0 or y < 0 or x >= self.root.scene.width() or y >= self.root.scene.height():
            return
        if self.root.curr_color == self.render.pixelColor(x, y).name():
            return
        self.fill(x, y, self.render.pixelColor(x, y))

    def fill(self, start_x, start_y, target_color):

        queue = [(start_x, start_y)]
        curr = iter(queue)
        checked_pixels = [[False for col in range(self.render.width())] for row in range(self.render.height())]
        checked_pixels[start_y][start_x] = True

        while True:

            try:
                x, y = next(curr)
            except StopIteration:
                return

            if target_color.name() != self.render.pixelColor(x, y).name():
                continue

            self.matrix[x, y] = ImageColor.getrgb(self.root.curr_color)

            if x + 1 < self.render.width() and not checked_pixels[y][x + 1]:
                queue.append((x + 1, y))
                checked_pixels[y][x + 1] = True
            if x - 1 >= 0 and not checked_pixels[y][x - 1]:
                queue.append((x - 1, y))
                checked_pixels[y][x - 1] = True
            if y + 1 < self.render.height() and not checked_pixels[y + 1][x]:
                queue.append((x, y + 1))
                checked_pixels[y + 1][x] = True
            if y - 1 >= 0 and not checked_pixels[y - 1][x]:
                queue.append((x, y - 1))
                checked_pixels[y - 1][x] = True
