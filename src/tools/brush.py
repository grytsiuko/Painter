from PIL import ImageDraw

from src.tools.tool import Tool


class Brush(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.last_x = x
        self.last_y = y

    def execute(self, x, y):

        left = x - self.root.curr_size / 2
        right = left + self.root.curr_size - 1
        top = y - self.root.curr_size / 2
        bottom = top + self.root.curr_size - 1

        self.draw.ellipse((left, top, right, bottom), fill=self.root.curr_color)
        self.draw.line((self.last_x, self.last_y, x, y), fill=self.root.curr_color, width=self.root.curr_size)

        self.last_x = x
        self.last_y = y
