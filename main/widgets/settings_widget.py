import os
import random
from PyQt5 import QtCore, QtWidgets, QtGui
from ui.widget_2 import Ui_SettingsWidget
from image import res


class SettingsWidget(QtWidgets.QFrame):

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)
        self.p = self.parent().parent()
        self.menu = QtWidgets.QMenu(self)
        self.action_1 = QtWidgets.QAction("Добавить файл")
        self.action_2 = QtWidgets.QAction("Добавить папку")
        self.menu.addActions([self.action_1, self.action_2])
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

    def show_context_menu(self, point):
        self.menu.exec(self.ui.tB.mapToGlobal(QtCore.QPoint(10, 10)))

    def setPixmap(self, path, mode=None):
        self.p.ui.l_back_img.setPixmap(QtGui.QPixmap(path))
        if mode == 1:
            try:
                self.p.ui.l_back_img.setPixmap(QtGui.QPixmap(f"{path}\{random.choice(os.listdir(path))}"))
            except:
                pass

    def setMovie(self, movie):
        self.p.ui.l_back_img.setMovie(QtGui.QMovie(movie))
        self.p.ui.l_back_img.movie().start()

    def setBackground(self, text):
        ext = os.path.splitext(text)[1]
        match ext:
            case ".gif":
                self.setMovie(text)
            case ".png" | ".jpg":
                self.setPixmap(text)
            case "":
                self.setPixmap(text, 1)
            case _:
                pass

    def selectFile(self):
        i0 = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Выберите файл", directory=None, filter="Image (*.png *.jpg);; GIF (*.gif)")[0]
        if not i0:
            return
        self.ui.lE.setText(i0)

    def selectFolder(self):
        i0 = QtWidgets.QFileDialog.getExistingDirectory(
            parent=self, caption="Выберите папку", directory=None)
        if not i0:
            return
        self.ui.lE.setText(i0)

    def connections(self):
        self.ui.tB.clicked.connect(self.show_context_menu)
        self.ui.lE.textChanged.connect(self.setBackground)
        self.action_1.triggered.connect(self.selectFile)
        self.action_2.triggered.connect(self.selectFolder)
