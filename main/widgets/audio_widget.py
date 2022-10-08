from PyQt5 import QtCore, QtWidgets, QtGui
from ui.widget_0 import Ui_AudioWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from volume_control import V
from image import res

class AudioWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = Ui_AudioWidget()
        self.ui.setupUi(self)
        self.volume_control = V()
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/img/img_7.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fonts = QtGui.QFont("Biennale Black", 10)
        self._old_pos = None
    def showEvent(self, a0: QtGui.QShowEvent):
        self.volume_start()
        return super().showEvent(a0)

    def hideEvent(self, a0: QtGui.QHideEvent):
        self.remove_item()
        return super().hideEvent(a0)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None
            px, py = self.pos().x(), self.pos().y()
            sx, sy = self.size().width(), self.size().height()
            if px + sx > 1920:
                self.move(1920-sx, py)
            elif px < 0:
                self.move(0, self.pos().y())
            if py + sy > 1080:
                self.move(px, 1080-sy)
            elif py < 0:
                self.move(self.pos().x(), 0)

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return

        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    @pyqtSlot()
    def volume_start(self):
        value = self.volume_control.get_volume_speakers()
        self.ui.hS.setValue(value)
        self.ui.l_num.setNum(value)
        self.ui.hS.valueChanged.connect(
            self.volume_control.set_volume_speakers)
        self.ui.btn_mute.clicked.connect(
            lambda: self.ui.hS.setValue(0))
        gL = QtWidgets.QGridLayout(self.ui.sAWC)
        gL.setSpacing(5)
        gL.setContentsMargins(0, 0, 0, 0)
        l = 0

        for session in self.volume_control.get_sessions():
            if session.Process and session.Process.name():
                value = self.volume_control.get_volume_session(
                    session.Process.name())
                l2 = QtWidgets.QLabel()
                l2.setFixedSize(20, 20)
                l2.setNum(value)
                l2.setObjectName(str(session.Process.name()))
                hs = QtWidgets.QSlider()
                hs.setObjectName(str(session.Process.name()))
                hs.setOrientation(QtCore.Qt.Horizontal)
                hs.setMaximum(100)
                hs.setPageStep(2)
                hs.setValue(value)
                hs.valueChanged.connect(
                    lambda vol, name=hs.objectName(): self.volume_control.set_volume_sessions(vol, name))
                hs.valueChanged.connect(
                    lambda vol, name=hs.objectName(): self.test2(vol, name))
                btn = QtWidgets.QPushButton()
                btn.setObjectName(str(session.Process.name()))
                btn.setFixedSize(20, 20)
                btn.setIcon(self.icon)
                btn.setIconSize(QtCore.QSize(20, 20))
                btn.clicked.connect(
                    lambda vol, name=hs.objectName(): self.test(vol, name))
                l1 = QtWidgets.QLabel()
                l1.setText((session.Process.name()).strip().replace(
                    ".exe", "").capitalize())
                l1.setMinimumHeight(30)
                l1.setFont(self.fonts)
                space = QtWidgets.QSpacerItem(
                    20, 317, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                gL.addWidget(l1, l, 1)
                gL.addWidget(hs, l+1, 1)
                gL.addWidget(l2, l+1, 2)
                gL.addWidget(btn, l+1, 0)
                l += 2
        gL.addItem(space, l+2, 1)

    @pyqtSlot()
    def test2(self, value, name):
        slider = []
        label = []
        for children in self.ui.sA.findChildren(QtWidgets.QLabel):
            label.append(children)
        for children1 in self.ui.sA.findChildren(QtWidgets.QSlider):
            slider.append(children1)
        for i in range(label.__len__()):
            if label[i].objectName() == name:
                label[i].setNum(value)

    @pyqtSlot()
    def test(self, value, name):
        slider = []
        btn = []
        for children in self.ui.sA.findChildren(QtWidgets.QPushButton):
            btn.append(children)
        for children1 in self.ui.sA.findChildren(QtWidgets.QSlider):
            slider.append(children1)
        for i in range(slider.__len__()):
            if btn[i].objectName() == name:
                slider[i].setValue(0)

    @pyqtSlot()
    def remove_item(self):
        for children in self.ui.sAWC.findChildren((QtWidgets.QGridLayout, QtWidgets.QSlider, QtWidgets.QLabel, QtWidgets.QPushButton)):
            try:
                children.deleteLater()
            except:
                pass
