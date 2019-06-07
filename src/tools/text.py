import io
from PIL import ImageQt, Image
from PyQt5.QtCore import QBuffer
from PyQt5.QtGui import QPainter, QPixmap, QColor


class Text:

    def __init__(self, root):

        self.root = root
        self.img = None

    def start(self, img, x, y):

        self.img = img
        self.draw_text(x, y)

    def proceed(self, x, y):

        self.draw_text(x, y)

    def end(self, x, y):

        self.draw_text(x, y)

    def draw_text(self, x, y):

        img_qt = ImageQt.ImageQt(self.img)
        pix_map = QPixmap.fromImage(img_qt)
        painter = QPainter(pix_map)
        painter.setFont(self.root.curr_font)
        painter.setPen(QColor(self.root.curr_color))
        painter.drawText(x, y, self.root.ui.text_edit.text())
        painter.end()

        q_img = pix_map.toImage()
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        q_img.save(buffer, "PNG")
        self.root.scene.new_layer_img = Image.open(io.BytesIO(buffer.data()))
