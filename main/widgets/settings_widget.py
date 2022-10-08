from PyQt5 import QtCore, QtWidgets, QtGui
from ui.widget_2 import Ui_SettingsWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from image import res


class SettingsWidget(QtWidgets.QFrame):

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)
        self.connections()
        self._old_pos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None
            px, py = self.pos().x(), self.pos().y()
            sx, sy = self.size().width(), self.size().height()
            if px < 0:
                self.move(0, self.pos().y())
            elif px + sx > 1920:
                self.move(1920-sx, py)
            if py < 0:
                self.move(self.pos().x(), 0)
            elif py + sy > 1080:
                self.move(px, 1080-sy)

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return

        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    @pyqtSlot()
    def select_back(self):
        i0 = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл", None, "*.png;;*.jpg;;*.bmp;;*.svg;;*.gif")[0]
        if not i0:
            return
        else:
            self.ui.lE.setText(i0)

    def connections(self):
        self.ui.tB.clicked.connect(self.select_back)
