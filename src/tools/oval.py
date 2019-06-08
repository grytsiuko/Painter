from PIL import ImageDraw

from src.tools.tool import Tool


class Oval(Tool):

    def __init__(self, root):

        super().__init__(root)

    def configure(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.first_x = x
        self.first_y = y

    def execute(self, x, y):

        self.draw.rectangle((0, 0, self.root.scene.width(), self.root.scene.height()), fill=(0, 0, 0, 0))

        self.draw.rectangle((0, 0, self.root.scene.width(), self.root.scene.height()), fill=(0, 0, 0, 0))

        left = min(x, self.first_x)
        right = max(x, self.first_x)
        top = min(y, self.first_y)
        bottom = max(y, self.first_y)

        if not self.root.curr_filled:
            self.draw.ellipse((left, top, right, bottom), outline=self.root.curr_color)
        else:
            self.draw.ellipse((left, top, right, bottom),
                              outline=self.root.curr_color, fill=self.root.curr_color)
