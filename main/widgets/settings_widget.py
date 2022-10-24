import os
from pydoc import ispath
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
        self.blur_eff = QtWidgets.QGraphicsBlurEffect()
        self.connections()
        self._old_pos = None
        self.extensions = (".png", ".jpg", ".jpeg")
        self.stackedWidget = self.p.ui.stackedWidget

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

    def clear_stack_widget(self):
        for children in self.stackedWidget.findChildren(QtWidgets.QLabel):
            children.deleteLater()


    def selectFile(self):
        i0 = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Выберите файл", directory=None, filter="Image (*.png *.jpg);; GIF (*.gif)")[0]
        if not i0:
            return
        self.clear_stack_widget()
        self.setBackground(path=i0, mode="File")
        self.ui.lE.setText(i0)

    def selectFolder(self):
        i0 = QtWidgets.QFileDialog.getExistingDirectory(
            parent=self, caption="Выберите папку", directory=None)
        if not i0:
            return
        self.clear_stack_widget()
        self.setBackground(path=i0, mode="Folder")
        self.ui.lE.setText(i0)

    def set_blur_img(self, value):
        self.blur_eff.setBlurRadius(value)
        self.stackedWidget.setGraphicsEffect(self.blur_eff)

    def setBackground(self, path: str, mode: str):
        self.stackedWidget.autoStop()
        label = QtWidgets.QLabel(self.stackedWidget)
        label.setObjectName(path)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(label)
        match mode:
            case "File":
                ext = os.path.splitext(path)[1]
                match ext:
                    case ".gif":
                        label.setMovie(QtGui.QMovie(path))
                        label.movie().start()
                    case ".png" | ".jpg":
                        label.setPixmap(QtGui.QPixmap(path).scaled(
                                self.stackedWidget.size(),
                                QtCore.Qt.AspectRatioMode.IgnoreAspectRatio,
                                QtCore.Qt.TransformationMode.SmoothTransformation))
                    case _:
                        pass
            case "Folder":
                try:
                    for name in os.listdir(path):
                        filename, file_ext = os.path.splitext(name)
                        if not file_ext in self.extensions:
                            continue
                        label = QtWidgets.QLabel(self.stackedWidget)
                        label.setObjectName(name)
                        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        #label.setMinimumSize(240, 160)
                        label.setPixmap(
                            QtGui.QPixmap(f"{path}/{name}").scaled(
                                self.stackedWidget.size(),
                                QtCore.Qt.AspectRatioMode.IgnoreAspectRatio,
                                QtCore.Qt.TransformationMode.SmoothTransformation))
                        label.setSizePolicy(
                            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                        self.stackedWidget.addWidget(label)
                        self.stackedWidget.autoStart()
                except Exception as ex:
                    print(ex)
            case _:
                if os.path.isfile(path) == True:
                    self.setBackground(path=path, mode="File")
    def check_path(self, text):
        if os.path.isfile(text) == True:
            self.setBackground(text, "File")
        else:
            self.setBackground(text, "Folder")

    def connections(self):
        self.ui.tB.clicked.connect(self.show_context_menu)
        self.action_1.triggered.connect(self.selectFile)
        self.action_2.triggered.connect(self.selectFolder)
        self.ui.lE.textChanged.connect(self.check_path)
        self.ui.hS.valueChanged.connect(self.set_blur_img)
