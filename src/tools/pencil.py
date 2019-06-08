from PIL import ImageDraw

from src.tools.tool import Tool


class Pencil(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.last_x = x
        self.last_y = y

    def execute(self, x, y):

        self.draw.line((self.last_x, self.last_y, x, y), fill=self.root.curr_color)
        self.last_x = x
        self.last_y = y
