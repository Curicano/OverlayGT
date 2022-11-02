from datetime import date
from PyQt5 import QtCore, QtWidgets


class Thread(QtCore.QThread):
    def __init__(self, parent):
        super().__init__()
        self.ui = parent

    def set_day(self):
        current_date = date.today()
        self.ui.l_date_1.setText(
            f"{current_date.day}.{current_date.month}.{current_date.year}")

    def run(self):
        self.set_day()


class TimeWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = parent.parent().ui
        self.timer = QtCore.QTimer()
        self.timer.setObjectName("Timer in TimeWidget")
        self.timer.timeout.connect(self.set_time)
        self.timer.start(100)
        self.thr = Thread(self.ui)
        #self.thr.start(self.thr.Priority.LowestPriority)

    def set_time(self):
        time = QtCore.QDateTime.currentDateTime()
        self.ui.l_time_1.setText(time.toString("hh : mm : ss"))
