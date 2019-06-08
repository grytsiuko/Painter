from PIL import ImageDraw

from src.tools.tool import Tool


class Line(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.first_x = x
        self.first_y = y

    def execute(self, x, y):

        self.draw.rectangle((0, 0, self.root.scene.width(), self.root.scene.height()), fill=(0, 0, 0, 0))
        self.draw.line((self.first_x, self.first_y, x, y), fill=self.root.curr_color, width=self.root.curr_size)
