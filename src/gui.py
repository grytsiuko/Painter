# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(800, 650)
        MainWindow.setMinimumSize(QtCore.QSize(800, 650))
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(211, 261))
        self.frame.setStyleSheet("background-color: #f6f6f6;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 171, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pencil_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.pencil_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pencil_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pencil_button.setIcon(icon)
        self.pencil_button.setIconSize(QtCore.QSize(36, 36))
        self.pencil_button.setObjectName("pencil_button")
        self.gridLayout.addWidget(self.pencil_button, 0, 0, 1, 1)
        self.oval_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.oval_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.oval_button.setAcceptDrops(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/layer-shape-ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oval_button.setIcon(icon1)
        self.oval_button.setIconSize(QtCore.QSize(36, 36))
        self.oval_button.setObjectName("oval_button")
        self.gridLayout.addWidget(self.oval_button, 2, 2, 1, 1)
        self.eraser_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.eraser_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eraser_button.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eraser_button.setIcon(icon2)
        self.eraser_button.setIconSize(QtCore.QSize(36, 36))
        self.eraser_button.setObjectName("eraser_button")
        self.gridLayout.addWidget(self.eraser_button, 0, 2, 1, 1)
        self.can_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.can_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/paint-can.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.can_button.setIcon(icon3)
        self.can_button.setIconSize(QtCore.QSize(36, 36))
        self.can_button.setObjectName("can_button")
        self.gridLayout.addWidget(self.can_button, 1, 2, 1, 1)
        self.line_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.line_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/layer-shape-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.line_button.setIcon(icon4)
        self.line_button.setIconSize(QtCore.QSize(36, 36))
        self.line_button.setObjectName("line_button")
        self.gridLayout.addWidget(self.line_button, 2, 0, 1, 1)
        self.brush_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.brush_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/paint-brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brush_button.setIcon(icon5)
        self.brush_button.setIconSize(QtCore.QSize(36, 36))
        self.brush_button.setObjectName("brush_button")
        self.gridLayout.addWidget(self.brush_button, 0, 1, 1, 1)
        self.spray_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.spray_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/spray.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spray_button.setIcon(icon6)
        self.spray_button.setIconSize(QtCore.QSize(36, 36))
        self.spray_button.setObjectName("spray_button")
        self.gridLayout.addWidget(self.spray_button, 1, 1, 1, 1)
        self.pipette_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.pipette_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pipette_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/pipette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pipette_button.setIcon(icon7)
        self.pipette_button.setIconSize(QtCore.QSize(36, 36))
        self.pipette_button.setObjectName("pipette_button")
        self.gridLayout.addWidget(self.pipette_button, 1, 0, 1, 1)
        self.rect_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.rect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/layer-shape.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rect_button.setIcon(icon8)
        self.rect_button.setIconSize(QtCore.QSize(36, 36))
        self.rect_button.setObjectName("rect_button")
        self.gridLayout.addWidget(self.rect_button, 2, 1, 1, 1)
        self.text_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.text_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.text_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.text_button.setIcon(icon9)
        self.text_button.setIconSize(QtCore.QSize(36, 36))
        self.text_button.setObjectName("text_button")
        self.gridLayout.addWidget(self.text_button, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(211, 211))
        self.frame_2.setStyleSheet("background-color: #f6f6f6;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.color_button = QtWidgets.QToolButton(self.frame_2)
        self.color_button.setGeometry(QtCore.QRect(70, 20, 71, 41))
        self.color_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.color_button.setAutoFillBackground(False)
        self.color_button.setStyleSheet("background-color: #000;\n"
"border-radius: 10px;")
        self.color_button.setText("")
        self.color_button.setObjectName("color_button")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 171, 104))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.size_slider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.size_slider.setObjectName("size_slider")
        self.gridLayout_2.addWidget(self.size_slider, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.size_spin = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.size_spin.setObjectName("size_spin")
        self.gridLayout_2.addWidget(self.size_spin, 0, 2, 1, 1)
        self.filled_check = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.filled_check.setText("")
        self.filled_check.setObjectName("filled_check")
        self.gridLayout_2.addWidget(self.filled_check, 2, 1, 1, 2)
        self.font_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.font_button.setObjectName("font_button")
        self.gridLayout_2.addWidget(self.font_button, 1, 1, 1, 2)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet("background-color: #ddd;")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionZoom_In)
        self.menuEdit.addAction(self.actionZoom_Out)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Painter"))
        self.pencil_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pencil</p></body></html>"))
        self.oval_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Oval</p></body></html>"))
        self.oval_button.setText(_translate("MainWindow", "..."))
        self.eraser_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Eraser</p></body></html>"))
        self.eraser_button.setText(_translate("MainWindow", "..."))
        self.can_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Can</p></body></html>"))
        self.can_button.setText(_translate("MainWindow", "..."))
        self.line_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Line</p></body></html>"))
        self.brush_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Brush</p></body></html>"))
        self.brush_button.setText(_translate("MainWindow", "..."))
        self.spray_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Spray</p></body></html>"))
        self.spray_button.setText(_translate("MainWindow", "..."))
        self.pipette_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pipette</p></body></html>"))
        self.rect_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Rectangle</p></body></html>"))
        self.rect_button.setText(_translate("MainWindow", "..."))
        self.text_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Text</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Size"))
        self.label_3.setText(_translate("MainWindow", "Font"))
        self.label_2.setText(_translate("MainWindow", "Filled"))
        self.font_button.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))


