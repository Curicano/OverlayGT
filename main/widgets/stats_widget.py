from time import gmtime, strftime
from PyQt5 import QtCore, QtWidgets
from uptime import uptime
from ui.widget_3 import Ui_StatsWidget
from image import res
from pyspeedtest import SpeedTest


class Thread(QtCore.QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.speed = SpeedTest("ping-test.ru")

    def run(self):
        while True:
            try:
                st1 = str(round(self.speed.ping()))
                self.parent.ui.l_stat_1.setText("ping: " + st1)
            except:
                self.parent.ui.l_stat_1.setText("Нет подключения.")
            try:
                st2 = str(round(self.speed.download()/1000, 2))
                self.parent.ui.l_stat_2.setText("download: " + st2 + " mb")
            except:
                self.parent.ui.l_stat_2.setText("Нет подключения.")
            self.parent.ui.l_stat.setText(str(str(round(
                uptime()/86400)) + " : " + strftime("%H : %M : %S", gmtime(round(uptime())))))





class StatsWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = Ui_StatsWidget()
        self.ui.setupUi(self)
        self.thr = Thread(self)
        self.thr.start(QtCore.QThread.Priority.LowestPriority)
