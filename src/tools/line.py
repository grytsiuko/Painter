from PIL import ImageDraw


class Line:

    def __init__(self, root):

        self.root = root
        self.first_x = None
        self.first_y = None
        self.draw = None

    def start(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.first_x = x
        self.first_y = y
        self.draw_line(x, y)

    def proceed(self, x, y):

        self.draw_line(x, y)

    def end(self, x, y):

        self.draw_line(x, y)

    def draw_line(self, x, y):

        self.draw.rectangle((0, 0, self.root.scene.width(), self.root.scene.height()), fill=(0, 0, 0, 0))
        self.draw.line((self.first_x, self.first_y, x, y), fill=self.root.curr_color, width=self.root.curr_size)
