from PIL import ImageDraw

from src.tools.tool import Tool


class Rect(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.first_x = x
        self.first_y = y

    def execute(self, x, y):

        self.draw.rectangle((0, 0, self.root.scene.width(), self.root.scene.height()), fill=(0, 0, 0, 0))

        if not self.root.curr_filled:
            self.draw.rectangle((self.first_x, self.first_y, x, y), outline=self.root.curr_color)
        else:
            self.draw.rectangle((self.first_x, self.first_y, x, y),
                                outline=self.root.curr_color, fill=self.root.curr_color)
