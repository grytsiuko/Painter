import math
from random import random
from PIL import ImageColor


class Spray:

    def __init__(self, root):

        self.root = root
        self.matrix = None

    def start(self, img, x, y):

        self.matrix = img.load()
        self.draw_dots(x, y)

    def proceed(self, x, y):

        self.draw_dots(x, y)

    def end(self, x, y):

        self.draw_dots(x, y)

    def draw_dots(self, x, y):

        for i in range(2 * self.root.curr_size):
            phi = random() * 2 * math.pi
            radius = random() * self.root.curr_size
            dot_x = x + radius * math.cos(phi)
            dot_y = y + radius * math.sin(phi)
            if dot_x < 0 or dot_y < 0 or dot_x >= self.root.scene.width() or dot_y >= self.root.scene.height():
                continue
            self.matrix[dot_x, dot_y] = ImageColor.getrgb(self.root.curr_color)
