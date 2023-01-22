import sys
from webbrowser import open as open_web

from keyboard import register_hotkey, unregister_hotkey
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QRect, QPoint, QPropertyAnimation, QThread, QParallelAnimationGroup, QEasingCurve, QDateTime
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
from PyQt5.QtGui import QKeySequence, QKeyEvent

from config_rw import Config
from image import rc_res
from themes.theme_selector import ThemeSelector
from ui.ui_main_window import Ui_MainWindow
from widgets.splash_screen import SplashScreen
from widgets.tray import MyTray
from widgets.audio_widget import AudioWidget
from widgets.settings_widget import SettingsWidget
from widgets.translit_widget import TranslitWidget


class HotKey(QObject):
    hotKeyReleased = pyqtSignal()

    def __init__(self, parent=None) -> None:
        QObject.__init__(self, parent=parent)
        self.hotkey_2 = QShortcut(parent)

    def reg_hotkey_1(self, key: str) -> None:
        self.hotkey_1 = register_hotkey(
            key, self.hotKeyReleased.emit, suppress=True, trigger_on_release=True)

    def unreg_hotkey_1(self, key) -> None:
        unregister_hotkey(self.hotkey_1)
        self.reg_hotkey_1(key)

    def reg_hotkey_2(self, key: str) -> None:
        self.hotkey_2.setKey(QKeySequence().fromString(key))


class MyWindow(QMainWindow):
    state = False

    def __init__(self) -> None:
        self.config = Config()
        self.config.read()
        self.cfg = self.config.cfg
        self.ss = SplashScreen(
            self.cfg["DEFAULT"]["version"], self.cfg["settings"]["silent"])
        QMainWindow.__init__(self, flags=Qt.WindowType.WindowStaysOnTopHint |
                             Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tray = MyTray(
            self, self.cfg["DEFAULT"]["name"], self.cfg["DEFAULT"]["version"])
        self.tray.show()
        self.theme_selector = ThemeSelector()
        self.audio_widget = AudioWidget(self.ui.f_child)
        self.settings_widget = SettingsWidget(self.ui.f_child, self.ui)
        self.translit_widget = TranslitWidget(self.ui.f_child)
        self.hot_key = HotKey(self)
        self.hot_key.reg_hotkey_1(self.cfg["hotkeys"]["show_hide"])
        self.hot_key.reg_hotkey_2(self.cfg["hotkeys"]["mode_change"])
        self.connections()
        self.setupUi()
        self.animation()

    def animation(self) -> None:
        self.show_anim = QPropertyAnimation(self, b"windowOpacity")
        self.show_anim.setDuration(500)
        self.show_anim.setStartValue(0)
        self.show_anim.setEndValue(1)

        self.show_anim_2 = QPropertyAnimation(self, b"geometry")
        self.show_anim_2.setDuration(500)
        self.show_anim_2.setStartValue(QRect(0, 1080, 1920, 1080))
        self.show_anim_2.setEndValue(QRect(0, 0, 1920, 1080))
        self.show_anim_2.setDirection(1)
        self.show_anim_2.setEasingCurve(QEasingCurve.Type.InOutQuint)

        self.group_anim = QParallelAnimationGroup(self)
        self.group_anim.addAnimation(self.show_anim)
        self.group_anim.addAnimation(self.show_anim_2)

    def setupUi(self) -> None:
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.audio_widget.hide()
        self.translit_widget.hide()
        self.settings_widget.hide()
        self.ui.VersionWidget.hide()
        self.ui.VersionWidget.move(QPoint(1080, 55))
        self.ui.TimeWidget.hide()
        self.ui.TimeWidget.move(QPoint(870, 120))
        self.ui.l_stat.hide()
        self.ui.l_stat_1.hide()
        self.ui.l_stat_2.hide()
        self.ui.l_1.setText(
            f"{self.cfg['DEFAULT']['name']} {self.cfg['DEFAULT']['version']} (Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")

        for theme in self.theme_selector.getTheme():
            self.settings_widget.ui.comboB.addItem(theme)
        self.settings_widget.ui.comboB.setCurrentText(
            self.cfg["settings"]["theme"])
        self.settings_widget.ui.lE.setText(
            self.cfg["settings"]["background"])
        self.settings_widget.ui.hS.setValue(
            int(self.cfg["settings"]["blur"]))
        self.settings_widget.ui.checkB.setCheckState(
            int(self.cfg["settings"]["autostart"]))
        self.settings_widget.ui.checkB_2.setCheckState(
            int(self.cfg["settings"]["silent"]))
        self.settings_widget.ui.checkB_3.setCheckState(
            int(self.cfg["settings"]["stat_uptime"]))
        self.settings_widget.ui.checkB_4.setCheckState(
            int(self.cfg["settings"]["stat_ping"]))
        self.settings_widget.ui.checkB_5.setCheckState(
            int(self.cfg["settings"]["stat_download"]))
        self.settings_widget.ui.kSE_show_hide.setKeySequence(
            self.cfg["hotkeys"]["show_hide"])
        self.settings_widget.ui.kSE_mode_changer.setKeySequence(
            self.cfg["hotkeys"]["mode_change"])
        self.settings_widget.ui.l_cur_ver.setText(
            self.cfg["DEFAULT"]["version"])
        self.settings_widget.ui.l_last_check_upd.setText(
            self.cfg["info"]["last_check_upd"])
        self.audio_widget.move(
            int(self.cfg["audio_widget"]["posx"]), int(self.cfg["audio_widget"]["posy"]))
        self.settings_widget.move(
            int(self.cfg["settings_widget"]["posx"]), int(self.cfg["settings_widget"]["posy"]))
        self.translit_widget.move(
            int(self.cfg["translit_widget"]["posx"]), int(self.cfg["translit_widget"]["posy"]))

    def show(self) -> None:
        return super().showFullScreen(), super().setFocus()

    def hideEvent(self, a0) -> None:
        self.ui.StatsWidget.thr.terminate()
        return super().hideEvent(a0)

    def showEvent(self, a0) -> None:
        self.ui.StatsWidget.thr.start(QThread.Priority.LowestPriority)
        return super().showEvent(a0)

    def sh_self(self) -> None:
        if self.isHidden() == False:
            self.state = True
            self.group_anim.finished.connect(self.hide)
            self.group_anim.setDirection(self.group_anim.Direction(1))
        else:
            if self.state:
                self.group_anim.finished.disconnect(self.hide)
                self.state = False
            self.group_anim.setDirection(self.group_anim.Direction(0))
        self.group_anim.start()
        self.show()

    def save_settings(self) -> None:
        self.cfg["settings"] = {
            "theme": f"{self.settings_widget.ui.comboB.currentText()}",
            "background": f"{self.settings_widget.ui.lE.text()}",
            "blur": f"{self.settings_widget.ui.hS.value()}",
            "autostart": f"{self.settings_widget.ui.checkB.checkState()}",
            "silent": f"{self.settings_widget.ui.checkB_2.checkState()}",
            "stat_uptime": f"{self.settings_widget.ui.checkB_3.checkState()}",
            "stat_ping": f"{self.settings_widget.ui.checkB_4.checkState()}",
            "stat_download": f"{self.settings_widget.ui.checkB_5.checkState()}",
        }
        pos = self.audio_widget.pos()
        self.cfg["audio_widget"] = {"posx": f"{pos.x()}",
                                    "posy": f"{pos.y()}"}
        pos = self.settings_widget.pos()
        self.cfg["settings_widget"] = {"posx": f"{pos.x()}",
                                       "posy": f"{pos.y()}"}
        pos = self.translit_widget.pos()
        self.cfg["translit_widget"] = {"posx": f"{pos.x()}",
                                       "posy": f"{pos.y()}"}
        self.cfg["hotkeys"] = {"show_hide": f"{self.settings_widget.ui.kSE_show_hide.keySequence().toString()}",
                               "mode_change": f"{self.settings_widget.ui.kSE_mode_changer.keySequence().toString()}"}
        self.cfg["info"]["last_check_upd"] = self.settings_widget.ui.l_last_check_upd.text()
        self.config.write()

    def close(self) -> None:
        self.save_settings()
        sys.exit()

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.key() == Qt.Key.Key_F5:
            self.close()

    def sh(self, obj) -> None:
        if obj.isHidden() == False:
            obj.hide()
        else:
            obj.show()

    def checkUpdate(self) -> None:
        self.hide()
        open_web(
            "https://github.com/Curicano/OverlayGT/releases", new=0, autoraise=True)
        time = QDateTime.currentDateTime().toString()
        self.settings_widget.ui.l_last_check_upd.setText(time)

    def connections(self) -> None:
        self.ui.btn_hide.clicked.connect(self.sh_self)
        self.hot_key.hotKeyReleased.connect(self.sh_self)
        self.hot_key.hotkey_2.activated.connect(
            lambda: self.sh(self.ui.f_child))
        self.ui.btn_mixer.clicked.connect(self.audio_widget.show_hide)
        self.ui.btn_interpreter.clicked.connect(self.translit_widget.show_hide)
        self.ui.btn_settings.leftMouseButtonClicked.connect(
            self.settings_widget.show_hide)
        self.ui.btn_settings.rightMouseButtonClicked.connect(
            lambda: self.sh(self.ui.VersionWidget))
        self.ui.l_time.clicked.connect(lambda: self.sh(self.ui.TimeWidget))
        self.tray.a_oTriggered.connect(self.sh_self)
        self.tray.a_eTriggered.connect(self.close)
        self.tray.a_cuTriggered.connect(self.checkUpdate)
        self.ss.singal_show.connect(self.sh_self)
        self.settings_widget.ui.checkB_3.stateChanged.connect(
            lambda: self.sh(self.ui.l_stat))
        self.settings_widget.ui.checkB_4.stateChanged.connect(
            lambda: self.sh(self.ui.l_stat_1))
        self.settings_widget.ui.checkB_5.stateChanged.connect(
            lambda: self.sh(self.ui.l_stat_2))
        self.settings_widget.ui.comboB.currentTextChanged.connect(
            self.theme_selector.setTheme)
        self.theme_selector.themeChanged.connect(self.setStyleSheet)
        self.settings_widget.ui.btn_save.clicked.connect(self.save_settings)
        self.settings_widget.ui.btn_check_upd.clicked.connect(self.checkUpdate)
        self.settings_widget.ui.kSE_show_hide.editingFinished.connect(self.hot_key.reg_hotkey_1)
        self.settings_widget.ui.kSE_mode_changer.editingFinished.connect(self.hot_key.reg_hotkey_2)


if __name__ == "__main__":
    cfg = Config()
    cfg.read()
    for arg in sys.argv:
        match arg:
            case "-autostart":
                if cfg.cfg["settings"]["autostart"] == "0":
                    sys.exit()
            case "-HDPI":
                QApplication.setAttribute(
                    Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setCursorFlashTime(2000)
    ui = MyWindow()
    app.exec_()
