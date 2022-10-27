from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal


class MylTime(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent=parent)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_time)
        self.timer.start(1000)

    def set_time(self):
        time = QtCore.QDateTime.currentDateTime()
        self.setText(time.toString("hh : mm"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
