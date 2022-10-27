from datetime import date
from PyQt5 import QtCore, QtWidgets, QtGui


class TimeWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = parent.parent().ui
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_time)
        self.timer.start(100)

    def set_time(self):
        time = QtCore.QDateTime.currentDateTime()
        self.ui.l_time_1.setText(time.toString("hh : mm : ss"))
        current_date = date.today()
        self.ui.l_date_1.setText(f"{current_date.day}.{current_date.month}.{current_date.year}")
