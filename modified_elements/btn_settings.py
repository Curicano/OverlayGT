from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal


class MybtnSettings(QtWidgets.QPushButton):
    sh_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent=parent)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.MouseButton.RightButton:
            #print(self.parent().parent().parent().objectName())
            self.sh_signal.emit(self.parent().parent().parent().ui.VersionWidget)
        elif e.button() == QtCore.Qt.MouseButton.LeftButton:
            self.sh_signal.emit(self.parent().parent().parent().ui.SettingsWidget)
        return super().mousePressEvent(e)
