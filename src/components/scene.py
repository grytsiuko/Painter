from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL.Image import *
from PIL.ImageQt import *


class Scene(QGraphicsScene):

    def __init__(self, root):

        super().__init__()
        self.root = root
        self.pressed = False
        self.new_layer_img = None
        self.new_layer_item = None

    def refresh_new_layer(self):

        img_qt = ImageQt(self.new_layer_img)
        pix_map = QPixmap.fromImage(img_qt)
        self.new_layer_item.setPixmap(pix_map)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.pressed = True

            self.new_layer_img = Image.new('RGBA', (int(self.root.scene.width()), int(self.root.scene.height())))
            self.new_layer_item = QGraphicsPixmapItem()
            self.root.scene.addItem(self.new_layer_item)

            pos = event.scenePos()
            self.root.curr_tool.start(self.new_layer_img, int(pos.x()), int(pos.y()))
            self.refresh_new_layer()

    def mouseMoveEvent(self, event):

        if self.pressed:

            pos = event.scenePos()
            self.root.curr_tool.proceed(int(pos.x()), int(pos.y()))
            self.refresh_new_layer()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.pressed = False
            pos = event.scenePos()
            self.root.curr_tool.end(int(pos.x()), int(pos.y()))
            self.refresh_new_layer()
