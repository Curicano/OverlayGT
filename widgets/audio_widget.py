import pyautogui as pg
from image import res
from PyQt5 import QtCore, QtGui, QtWidgets
from volume_control import V


class AudioWidget(QtWidgets.QFrame):
    state = 1
    _old_pos = None

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = parent.parent().ui
        self.volume_control = V()
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/img/img_7.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_1 = QtGui.QIcon()
        self.icon_1.addPixmap(QtGui.QPixmap(":/img/img_15.png"),
                              QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_2 = QtGui.QIcon()
        self.icon_2.addPixmap(QtGui.QPixmap(":/img/img_16.png"),
                              QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fonts = QtGui.QFont("Biennale Black", 10)
        self.animation = QtCore.QPropertyAnimation(self, b"size")
        self.animation.setStartValue(QtCore.QSize(320, 140))
        self.animation.setEndValue(QtCore.QSize(320, 420))
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuint)
        self.animation.setDirection(self.animation.Direction.Backward)
        self.animation.start()

    def startAnim(self):
        if self.state == 0:
            self.animation.setDirection(self.animation.Direction.Backward)
            self.animation.finished.connect(
                lambda: self.ui.btn_move.setIcon(self.icon_2))
            self.animation.start()
            self.state = 1
        else:
            self.animation.setDirection(self.animation.Direction.Forward)
            self.animation.finished.connect(
                lambda: self.ui.btn_move.setIcon(self.icon_1))
            self.animation.start()
            self.state = 0

    def showEvent(self, a0: QtGui.QShowEvent):
        self.volume_start()
        return super().showEvent(a0)

    def hideEvent(self, a0: QtGui.QHideEvent):
        self.clear_layout(self.ui.sAWC.layout())
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

    def volume_start(self):
        value = self.volume_control.get_volume_speakers()
        self.ui.hS.setValue(value)
        self.ui.l_num.setNum(value)
        self.ui.hS.valueChanged.connect(
            self.volume_control.set_volume_speakers)
        self.ui.btn_mute.clicked.connect(
            lambda: self.ui.hS.setValue(0))
        l = 0
        for session in self.volume_control.get_sessions():
            if session.Process and session.Process.name():
                f_session = QtWidgets.QFrame()
                f_session.setObjectName(f"frame({session.Process.name()})")
                gL = QtWidgets.QGridLayout(f_session)
                gL.setSpacing(5)
                gL.setContentsMargins(0, 0, 0, 0)
                gL.setObjectName(f"gridLayout({session.Process.name()})")

                value = self.volume_control.get_volume_session(
                    session.Process.name())
                l_num = QtWidgets.QLabel()
                l_num.setMinimumSize(20, 20)
                l_num.setMaximumSize(20, 20)
                l_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                l_num.setNum(value)
                l_num.setObjectName(str(session.Process.name()))
                hS = QtWidgets.QSlider()
                hS.setMinimumWidth(243)
                hS.setObjectName(str(session.Process.name()))
                hS.setOrientation(QtCore.Qt.Horizontal)
                hS.setMaximum(100)
                hS.setPageStep(10)
                hS.setValue(value)
                hS.valueChanged.connect(
                    lambda vol, name=hS.objectName(): self.volume_control.set_volume_sessions(vol, name))
                hS.valueChanged.connect(
                    lambda vol, name=hS.objectName(): self.setValue(vol, name))
                btn_mute = QtWidgets.QPushButton()
                btn_mute.setMinimumSize(20, 20)
                btn_mute.setMaximumSize(20, 20)
                btn_mute.setObjectName(str(session.Process.name()))
                btn_mute.setIcon(self.icon)
                btn_mute.setIconSize(QtCore.QSize(20, 20))
                btn_mute.clicked.connect(
                    lambda state, name=hS.objectName(): self.mute(name))
                l_title = QtWidgets.QLabel()
                l_title.setMinimumHeight(20)
                l_title.setMaximumHeight(20)
                l_title.setText((session.Process.name()).strip().replace(
                    ".exe", "").capitalize())
                l_title.setMinimumHeight(30)
                l_title.setFont(self.fonts)
                gL.addWidget(l_title, l, 1)
                gL.addWidget(hS, l+1, 1)
                gL.addWidget(l_num, l+1, 2)
                gL.addWidget(btn_mute, l+1, 0)
                self.ui.vL.addWidget(f_session)
                l += 2
        if self.ui.sAWC.findChildren(QtWidgets.QGridLayout) != []:
            space = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.ui.vL.addItem(space)

    def setValue(self, value, name):
        sliders = []
        labels = []
        for children in self.ui.sA.findChildren(QtWidgets.QLabel):
            if children.objectName():
                labels.append(children)
        for children1 in self.ui.sA.findChildren(QtWidgets.QSlider):
            sliders.append(children1)
        for slide in sliders:
            for label in labels:
                if slide.objectName() == label.objectName() == name:
                    label.setNum(value)

    def mute(self, name):
        sliders = []
        buttons = []
        for children in self.ui.sA.findChildren(QtWidgets.QPushButton):
            buttons.append(children)
        for children1 in self.ui.sA.findChildren(QtWidgets.QSlider):
            sliders.append(children1)
        for btn in buttons:
            for slide in sliders:
                if slide.objectName() == btn.objectName() == name:
                    slide.setValue(0)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())
