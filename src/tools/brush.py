from PIL import ImageDraw


class Brush:

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

        left = x - self.root.curr_size / 2
        right = left + self.root.curr_size - 1
        top = y - self.root.curr_size / 2
        bottom = top + self.root.curr_size - 1

        self.draw.ellipse((left, top, right, bottom), fill=self.root.curr_color)
        self.draw.line((self.last_x, self.last_y, x, y), fill=self.root.curr_color, width=self.root.curr_size)

        self.last_x = x
        self.last_y = y
