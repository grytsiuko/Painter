from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Scene(QGraphicsScene):

    def __init__(self, root):

        super().__init__()
        self.root = root
        self.pressed = False
        self.pressed_down = None
        self.pressed_up = None

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.pressed_down = event.scenePos()
            self.pressed = True

    def mouseMoveEvent(self, event):

        if event.button() == Qt.LeftButton:
            if self.pressed:
                pass

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            if self.pressed:
                self.pressed_up = event.scenePos()
                self.pressed = False
