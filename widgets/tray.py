from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSignal


class MyTray(QSystemTrayIcon):
    a_oTriggered = pyqtSignal()
    a_eTriggered = pyqtSignal()
    a_cuTriggered = pyqtSignal()


    def __init__(self, parent=None, name: str = ..., version: str = ...):
        QSystemTrayIcon.__init__(self, parent=parent)
        self.parent = parent
        i = QIcon()
        i.addPixmap(QPixmap("logo.ico"))
        self.setIcon(QIcon(i))

        self.menu = QMenu()

        self.action_open = QAction("Открыть", self)
        self.menu.addAction(self.action_open)

        self.action_check_update = QAction("Проверить обновления", self)
        self.menu.addAction(self.action_check_update)

        self.action_exit = QAction("Выйти", self)
        self.menu.addAction(self.action_exit)

        self.setContextMenu(self.menu)

        self.setToolTip(f"{name} {version}")

        self.connections()


    def connections(self):
        self.action_open.triggered.connect(self.a_oTriggered.emit)
        self.action_check_update.triggered.connect(self.a_cuTriggered.emit)
        self.action_exit.triggered.connect(self.a_eTriggered.emit)
