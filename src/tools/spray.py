import math
from random import random
from PIL import ImageColor

from src.tools.tool import Tool


class Spray(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        self.matrix = img.load()

    def execute(self, x, y):

        for i in range(2 * self.root.curr_size):
            phi = random() * 2 * math.pi
            radius = random() * self.root.curr_size
            dot_x = x + radius * math.cos(phi)
            dot_y = y + radius * math.sin(phi)
            if dot_x < 0 or dot_y < 0 or dot_x >= self.root.scene.width() or dot_y >= self.root.scene.height():
                continue
            self.matrix[dot_x, dot_y] = ImageColor.getrgb(self.root.curr_color)
