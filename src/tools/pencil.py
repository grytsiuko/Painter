from PIL import ImageDraw


class Pencil:

    def __init__(self, root):

        self.root = root
        self.last_x = None
        self.last_y = None
        self.draw = None

    def start(self, img, x, y):

        self.draw = ImageDraw.Draw(img)
        self.last_x = x
        self.last_y = y
        self.draw_line(x, y)

    def proceed(self, img, x, y):

        self.draw_line(x, y)

    def end(self, img, x, y):

        self.draw_line(x, y)

    def draw_line(self, x, y):

        self.draw.line((self.last_x, self.last_y, x, y), fill=self.root.curr_color)
        self.last_x = x
        self.last_y = y
