from PyQt5 import QtCore, QtWidgets, QtGui
from widgets.music_widget import MusicWidget
from widgets.audio_widget import AudioWidget
from PyQt5.QtCore import pyqtSignal


class MybtnMixer(QtWidgets.QPushButton):
    sh_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent=parent)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.MouseButton.RightButton:
            self.sh_signal.emit(self.parent().parent().parent().ui.MusicWidget)
        elif e.button() == QtCore.Qt.MouseButton.LeftButton:
            self.sh_signal.emit(self.parent().parent().parent().ui.AudioWidget)
        return super().mousePressEvent(e)
