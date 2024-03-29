from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.components.scene import Scene
from src.components.new_file_dialog import NewFileDialog
from src.components.exit_dialog import ExitDialog


class ActionFunctions:

    def __init__(self, root):

        self.root = root
        self.file_dialog_options = QFileDialog.Options()
        self.file_dialog_options |= QFileDialog.DontUseNativeDialog
        self.zoom_rate = 1.25

    def new_file(self):

        if not self.close_file():
            return

        dialog = NewFileDialog()
        code = dialog.exec()

        if code == 0:
            return

        self.root.scene = Scene(self.root)
        self.root.ui.graphicsView.setScene(self.root.scene)

        white_sheet = QPixmap(dialog.ui.width_spin.value(), dialog.ui.height_spin.value())
        white_sheet.fill()
        bg = QGraphicsPixmapItem(white_sheet)
        self.root.scene.addItem(bg)

    def open_file(self):

        if not self.close_file():
            return

        new_file_name, _ = QFileDialog.getOpenFileName(self.root, "Open File", "",
                                                       "Images (*.jpg *.jpeg *.png)",
                                                       options=self.file_dialog_options)
        if not new_file_name:
            return

        self.root.file_name = new_file_name
        self.root.scene = Scene(self.root)
        self.root.ui.graphicsView.setScene(self.root.scene)

        img = QPixmap(new_file_name)
        white_sheet = QPixmap(img.width(), img.height())
        white_sheet.fill()

        bg = QGraphicsPixmapItem(white_sheet)
        insertion = QGraphicsPixmapItem(img)
        self.root.scene.addItem(bg)
        self.root.scene.addItem(insertion)

    def close_file(self):

        if not self.root.saved:

            dialog = ExitDialog()
            code = dialog.exec()

            if code == 0:
                return False

        self.root.file_name = None
        self.root.scene = None
        self.root.ui.graphicsView.setScene(None)
        self.root.ui.graphicsView.scale(1 / self.root.curr_zoom, 1 / self.root.curr_zoom)
        self.root.curr_zoom = 1
        self.root.layers_undone = list()
        self.root.layers = list()
        self.root.file_name = None
        self.root.saved = True
        return True

    def save_as_file(self):

        if self.root.scene is None:
            return
        new_file_name, _ = QFileDialog.getSaveFileName(self.root, "Save File", "",
                                                       "Images (*.jpg *.jpeg *.png)",
                                                       options=self.file_dialog_options)
        if new_file_name:
            if new_file_name[-4:] != '.png' and new_file_name[-4:] != '.jpg' \
                    and new_file_name[-5:] != '.jpeg':
                new_file_name += '.png'
            self.root.file_name = new_file_name
            self.save_file()

    def save_file(self):

        if self.root.file_name is None:
            self.save_as_file()
        else:
            img = QPixmap(self.root.scene.width(), self.root.scene.height())
            painter = QPainter(img)
            self.root.scene.render(painter)
            painter.end()
            img.save(self.root.file_name)
            self.root.saved = True

    def zoom_in(self):

        if self.root.scene.width() * self.root.curr_zoom * self.zoom_rate > 10000 or \
                self.root.scene.height() * self.root.curr_zoom * self.zoom_rate > 10000:
            return
        self.root.ui.graphicsView.scale(self.zoom_rate, self.zoom_rate)
        self.root.curr_zoom *= self.zoom_rate

    def zoom_out(self):

        if self.root.scene.width() * self.root.curr_zoom / self.zoom_rate < 1 or \
                self.root.scene.height() * self.root.curr_zoom / self.zoom_rate < 1:
            return
        self.root.ui.graphicsView.scale(1 / self.zoom_rate, 1 / self.zoom_rate)
        self.root.curr_zoom /= self.zoom_rate

    def undo(self):

        if len(self.root.layers):
            layer = self.root.layers.pop(-1)
            self.root.scene.removeItem(layer)
            self.root.layers_undone.append(layer)
            self.root.saved = False

    def redo(self):

        if len(self.root.layers_undone):
            layer = self.root.layers_undone.pop(-1)
            self.root.scene.addItem(layer)
            self.root.layers.append(layer)
            self.root.saved = False
