

class Tool:

    def __init__(self, root):

        self.root = root
        self.first_x = None
        self.first_y = None
        self.last_x = None
        self.last_y = None
        self.draw = None
        self.render = None
        self.matrix = None
        self.img = None

    def configure(self, img, x, y):

        pass

    def start(self, x, y):

        self.execute(x, y)

    def proceed(self, x, y):

        self.execute(x, y)

    def end(self, x, y):

        self.execute(x, y)

    def execute(self, x, y):

        pass
