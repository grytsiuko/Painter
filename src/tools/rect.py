from PIL import ImageDraw


class Rect:

    def __init__(self, root):

        self.root = root
        self.first_x = None
        self.first_y = None
        self.draw = None

    def start(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.first_x = x
        self.first_y = y
        self.draw_rect(x, y)

    def proceed(self, x, y):

        self.draw_rect(x, y)

    def end(self, x, y):

        self.draw_rect(x, y)

    def draw_rect(self, x, y):

        self.draw.rectangle((0, 0, self.root.scene.width(), self.root.scene.height()), fill=(0, 0, 0, 0))

        if not self.root.curr_filled:
            self.draw.rectangle((self.first_x, self.first_y, x, y), outline=self.root.curr_color)
        else:
            self.draw.rectangle((self.first_x, self.first_y, x, y),
                                outline=self.root.curr_color, fill=self.root.curr_color)
