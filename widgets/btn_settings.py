from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QMouseEvent


class MybtnSettings(QPushButton):
    rightMouseButtonClicked = pyqtSignal()
    leftMouseButtonClicked = pyqtSignal()

    def __init__(self, parent=None):
        QPushButton.__init__(self, parent=parent)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.MouseButton.RightButton:
            self.rightMouseButtonClicked.emit()
        elif e.button() == Qt.MouseButton.LeftButton:
            self.leftMouseButtonClicked.emit()
        return super().mousePressEvent(e)
