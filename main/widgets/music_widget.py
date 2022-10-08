from PyQt5 import QtCore, QtWidgets, QtGui
from ui.widget_4 import Ui_MusicWidget
from image import res
import pyautogui as pg


class MusicWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = Ui_MusicWidget()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        self.ui.btn_prev.clicked.connect(lambda: pg.press("prevtrack"))
        self.ui.btn_next.clicked.connect(lambda: pg.press("nexttrack"))
        self.ui.btn_pp.clicked.connect(lambda: pg.press("playpause"))
