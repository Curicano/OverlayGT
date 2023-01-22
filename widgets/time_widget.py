from datetime import date
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QShowEvent, QHideEvent


class TimeWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.ui = parent.parent().ui
        self.timer = QTimer()
        self.connections()

    def set_time(self):
        time = QDateTime.currentDateTime()
        self.ui.l_time_1.setText(time.toString("hh : mm : ss"))

    def set_date(self):
        current_date = date.today()
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.DefaultLocaleLongDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.DefaultLocaleShortDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.ISODate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.ISODateWithMs)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.LocalDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.LocaleDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.RFC2822Date)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.SystemLocaleDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.TextDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.SystemLocaleLongDate)
        # print(current_dat)
        # current_dat = QDateTime.currentDateTime().toString(
        #     Qt.DateFormat.SystemLocaleShortDate)
        # print(current_dat)
        # print(current_dat.time())
        # print(current_dat.date())
        self.ui.l_date_1.setText(
            f"{current_date.day}.{current_date.month}.{current_date.year}")

    def connections(self):
        self.timer.timeout.connect(self.set_time)

    def showEvent(self, a0: QShowEvent) -> None:
        self.timer.start(100)
        self.set_date()
        return super().showEvent(a0)

    def hideEvent(self, a0: QHideEvent) -> None:
        self.timer.stop()
        return super().hideEvent(a0)
