from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QDateTime, Qt, QTimer


class MylTime(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.set_time)
        self.timer.start(1000)

    def set_time(self):
        time = QDateTime.currentDateTime()
        self.setText(time.toString("hh : mm"))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
