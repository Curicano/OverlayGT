from pyautogui import press
from image import rc_res
from volume_control import V
from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QSlider, QPushButton, QSizePolicy, QSpacerItem
from PyQt5.QtCore import QPropertyAnimation, QSize, QEasingCurve, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont, QShowEvent, QHideEvent
from ui.ui_audio_widget import Ui_AudioWidget


class AudioWidget(QFrame):
    state = 1
    _old_pos = None

    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.ui = Ui_AudioWidget()
        self.ui.setupUi(self)
        self.setupUi()
        self.connections()
        self.volume_control = V()

    def setupUi(self):
        self.icon_m_c = QIcon()
        self.icon_m_c.addPixmap(QPixmap(":/img/img_15.png"),
                                QIcon.Normal, QIcon.Off)
        self.icon_m_o = QIcon()
        self.icon_m_o.addPixmap(QPixmap(":/img/img_16.png"),
                                QIcon.Normal, QIcon.Off)
        self.icon_v_66_100 = QIcon()
        self.icon_v_66_100.addPixmap(QPixmap(":/img/img_2.png"),
                                     QIcon.Normal, QIcon.Off)
        self.icon_v_33_65 = QIcon()
        self.icon_v_33_65.addPixmap(QPixmap(":/img/img_17.png"),
                                    QIcon.Normal, QIcon.Off)
        self.icon_v_1_32 = QIcon()
        self.icon_v_1_32.addPixmap(QPixmap(":/img/img_18.png"),
                                   QIcon.Normal, QIcon.Off)
        self.icon_v_0_1 = QIcon()
        self.icon_v_0_1.addPixmap(QPixmap(":/img/img_7.png"),
                                  QIcon.Normal, QIcon.Off)
        self.fonts = QFont("Biennale Black", 10)
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setStartValue(QSize(320, 140))
        self.animation.setEndValue(QSize(320, 420))
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuint)
        self.animation.setDirection(self.animation.Direction.Backward)
        self.animation.start()

    def startAnim(self):
        if self.state == 0:
            self.animation.setDirection(self.animation.Direction.Backward)
            self.ui.btn_move.setIcon(self.icon_m_c)
            self.state = 1
        else:
            self.animation.setDirection(self.animation.Direction.Forward)
            self.ui.btn_move.setIcon(self.icon_m_o)
            self.state = 0
        self.animation.start()

    def showEvent(self, a0: QShowEvent):
        self.volume_start()
        return super().showEvent(a0)

    def hideEvent(self, a0: QHideEvent):
        self.clear_layout(self.ui.sAWC.layout())
        return super().hideEvent(a0)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
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
        self.ui.hS.valueChanged.connect(self.setValueSpeakers)
        if value > 65:
            self.ui.btn_mute.setIcon(self.icon_v_66_100)
        elif value < 66 and value > 32:
            self.ui.btn_mute.setIcon(self.icon_v_33_65)
        elif value < 33 and value > 0:
            self.ui.btn_mute.setIcon(self.icon_v_1_32)
        else:
            self.ui.btn_mute.setIcon(self.icon_v_0_1)
        self.ui.btn_mute.clicked.connect(self.mute_speakers)
        l = 0
        for session in self.volume_control.get_sessions():
            if session.Process and session.Process.name():
                f_session = QFrame()
                gL = QGridLayout(f_session)
                gL.setSpacing(5)
                gL.setContentsMargins(0, 0, 0, 0)

                value = self.volume_control.get_volume_session(
                    session.Process.name())
                l_num = QLabel()
                l_num.setMinimumSize(20, 20)
                l_num.setMaximumSize(20, 20)
                l_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
                l_num.setNum(value)
                l_num.setObjectName(str(session.Process.name()))
                hS = QSlider()
                hS.setMinimumWidth(243)
                hS.setObjectName(str(session.Process.name()))
                hS.setOrientation(Qt.Horizontal)
                hS.setMaximum(100)
                hS.setPageStep(10)
                hS.setValue(value)
                hS.valueChanged.connect(
                    lambda vol, name=hS.objectName(): self.volume_control.set_volume_sessions(vol, name))
                hS.valueChanged.connect(
                    lambda vol, name=hS.objectName(): self.setValueSessions(vol, name))
                btn_mute = QPushButton()
                btn_mute.setMinimumSize(20, 20)
                btn_mute.setMaximumSize(20, 20)
                btn_mute.setObjectName(str(session.Process.name()))
                if value > 65:
                    btn_mute.setIcon(self.icon_v_66_100)
                elif value < 66 and value > 32:
                    btn_mute.setIcon(self.icon_v_33_65)
                elif value < 33 and value > 0:
                    btn_mute.setIcon(self.icon_v_1_32)
                else:
                    btn_mute.setIcon(self.icon_v_0_1)
                btn_mute.setIconSize(QSize(20, 20))
                btn_mute.clicked.connect(
                    lambda state, name=hS.objectName(): self.mute_sessions(name))
                l_title = QLabel()
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
        if self.ui.sAWC.findChildren(QGridLayout) != []:
            space = QSpacerItem(
                20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.ui.vL.addItem(space)

    def setValueSessions(self, value, name):
        sliders = [i for i in self.ui.sA.findChildren(QSlider)]
        labels = [i for i in self.ui.sA.findChildren(
            QLabel) if i.objectName()]
        buttons = [i for i in self.ui.sA.findChildren(QPushButton)]
        for slide in sliders:
            for label in labels:
                if slide.objectName() == label.objectName() == name:
                    label.setNum(value)
            for btn in buttons:
                if slide.objectName() == btn.objectName() == name:
                    if value > 65:
                        btn.setIcon(self.icon_v_66_100)
                    elif value < 66 and value > 32:
                        btn.setIcon(self.icon_v_33_65)
                    elif value < 33 and value > 0:
                        btn.setIcon(self.icon_v_1_32)
                    else:
                        btn.setIcon(self.icon_v_0_1)

    def setValueSpeakers(self, value):
        self.ui.l_num.setNum(value)
        self.volume_control.set_volume_speakers(value)
        if value > 65:
            self.ui.btn_mute.setIcon(self.icon_v_66_100)
        elif value < 66 and value > 32:
            self.ui.btn_mute.setIcon(self.icon_v_33_65)
        elif value < 33 and value > 0:
            self.ui.btn_mute.setIcon(self.icon_v_1_32)
        else:
            self.ui.btn_mute.setIcon(self.icon_v_0_1)

    def mute_sessions(self, name):
        sliders = [i for i in self.ui.sA.findChildren(QSlider)]
        buttons = [i for i in self.ui.sA.findChildren(QPushButton)]
        for btn in buttons:
            for slide in sliders:
                if slide.objectName() == btn.objectName() == name:
                    slide.setValue(0)
                    btn.setIcon(self.icon_v_0_1)

    def mute_speakers(self):
        self.ui.hS.setValue(0)
        self.ui.btn_mute.setIcon(self.icon_v_0_1)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())

    def show_hide(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def connections(self):
        self.ui.btn_prev.clicked.connect(lambda: press("prevtrack"))
        self.ui.btn_next.clicked.connect(lambda: press("nexttrack"))
        self.ui.btn_pp.clicked.connect(lambda: press("playpause"))
        self.ui.btn_move.clicked.connect(self.startAnim)
