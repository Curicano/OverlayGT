from themes import themes
import pyAesCrypt
from winreg import HKEY_LOCAL_MACHINE, OpenKeyEx, QueryValue, KEY_READ
from configparser import ConfigParser
import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtWinExtras
from image import res
from ui.main_window import Ui_MainWindow
from volume_control import V
import webbrowser
from keyboard import add_hotkey
import win32api
from widgets.splash_screen import SplashScreen
VERSION = "v0.0.0.3"
NAME = "OverlayGT"


class Crypter():
    def __init__(self):
        super().__init__()
        self.password = "0000"
        self.buffer = 512*1024

    def encrypt(self, file):
        ext = os.path.splitext(file)[0]
        pyAesCrypt.encryptFile(
            file, ext.lower() + ".cw", self.password, self.buffer)
        os.remove(file)

    def decrypt(self, file):
        ext = os.path.splitext(file)[0]
        pyAesCrypt.decryptFile(
            file, ext.lower() + ".ini", self.password, self.buffer)
        os.remove(file)


class HotKey(QtCore.QObject):
    sh = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        win32api.LoadKeyboardLayout("00000419", 1)
        add_hotkey(
            "alt + ё", self.sh.emit, suppress=True, trigger_on_release=True)


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.splash_screen = SplashScreen(self)
        self.volume_control = V()
        self.hot_key = HotKey()
        self.timer = QtCore.QTimer(self)
        self.blur_eff = QtWidgets.QGraphicsBlurEffect()
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/img/logo.ico"),
                            QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.path_to_themes = self.resource_path(
            "Git\\OverlayGT 2.0\\main\\themes")
        self.rebuilder()
        self.connections()
        self.timer.start(100)
        self.tray()
        if cfg["settings"]["launch_hidden"] == "0":
            self.sh(self.splash_screen)
        self.state = 0

    def tray(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.icon)
        self.quit_action = QtWidgets.QAction("Выйти", self)
        self.quit_action.triggered.connect(lambda: self.close())
        self.show_action = QtWidgets.QAction("Показать", self)
        self.show_action.triggered.connect(lambda: self.sh(self))
        self.check_upd_action = QtWidgets.QAction("Проверить обновления", self)
        self.check_upd_action.triggered.connect(self.check_upd)
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.addActions(
            [self.quit_action, self.show_action, self.check_upd_action])
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.setToolTip(f"{NAME} {VERSION}")
        self.tray_icon.show()

    def rebuilder(self):
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint |
                            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Tool)  # | QtCore.Qt.WindowType.Tool
        self.setWindowTitle(NAME)
        self.ui.AudioWidget.hide()
        self.ui.TranslitWidget.hide()
        self.ui.SettingsWidget.hide()
        self.ui.VersionWidget.hide()
        self.ui.l_1.setText(
            f"{NAME} {VERSION} (Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")
        name = ["White", "Red", "Green", "Blue", "Violet", "Yellow", "Blue Red", "Cold", "Fire Violet", "Fire", "Fuxia Neon Violet", "Fuxia Neon Yellow", "Gray", "Green Violet", "Ice Fire",
                "Ice Green", "Ice Violet", "Ice", "Lineage", "Neon Yellow Ice", "Old Ice", "Orange Gray", "Orange", "Pink Gray", "Red Violet", "Violet Fire", "Violet Green", "Violet Ice", "Violet Red"]
        for item in sorted(name):
            self.ui.SettingsWidget.ui.cB.addItem(item)
        self.show_anim = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.show_anim.setDuration(500)
        self.show_anim.setStartValue(0)
        self.show_anim.setEndValue(1)

        self.show_anim_2 = QtCore.QPropertyAnimation(self, b"geometry")
        self.show_anim_2.setDuration(500)
        self.show_anim_2.setStartValue(QtCore.QRect(0, 1080, 1920, 1080))
        self.show_anim_2.setEndValue(QtCore.QRect(0, 0, 1920, 1080))
        self.show_anim_2.setDirection(1)
        self.show_anim_2.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuint)

        self.group_anim = QtCore.QParallelAnimationGroup(self)
        self.group_anim.addAnimation(self.show_anim)
        self.group_anim.addAnimation(self.show_anim_2)

        self.ui.SettingsWidget.ui.cB.setCurrentText(cfg["settings"]["theme"])
        themes.select_theme(self, self.path_to_themes,
                            self.ui.SettingsWidget.ui.cB.currentText())
        self.ui.SettingsWidget.ui.lE.setText(
            cfg["settings"]["background_image"])
        self.ui.SettingsWidget.ui.hS.setValue(int(cfg["settings"]["blur"]))
        self.ui.SettingsWidget.ui.l_num_2.setNum(int(cfg["settings"]["blur"]))
        self.set_blur_img(int(cfg["settings"]["blur"]))
        self.ui.SettingsWidget.ui.cBox.setCheckState(
            int(cfg["settings"]["autostart"]))
        self.ui.SettingsWidget.ui.cBox_1.setCheckState(
            int(cfg["settings"]["launch_hidden"]))
        match int(cfg["settings"]["stat_time_startup"]):
            case 0:
                self.ui.StatsWidget.ui.l_stat.hide()
            case _:
                self.ui.StatsWidget.ui.l_stat.show()
        self.ui.SettingsWidget.ui.cBox_2.setCheckState(
            int(cfg["settings"]["stat_time_startup"]))
        match int(cfg["settings"]["stat_ping"]):
            case 0:
                self.ui.StatsWidget.ui.l_stat_1.hide()
            case _:
                self.ui.StatsWidget.ui.l_stat_1.show()
        self.ui.SettingsWidget.ui.cBox_3.setCheckState(
            int(cfg["settings"]["stat_ping"]))
        match int(cfg["settings"]["stat_download"]):
            case 0:
                self.ui.StatsWidget.ui.l_stat_2.hide()
            case _:
                self.ui.StatsWidget.ui.l_stat_2.show()
        self.ui.SettingsWidget.ui.cBox_4.setCheckState(
            int(cfg["settings"]["stat_download"]))
        self.ui.AudioWidget.move(
            int(cfg["audio_widget_pos"]["x"]), int(cfg["audio_widget_pos"]["y"]))
        self.ui.SettingsWidget.move(
            int(cfg["settings_widget_pos"]["x"]), int(cfg["settings_widget_pos"]["y"]))
        self.ui.TranslitWidget.move(
            int(cfg["translit_widget_pos"]["x"]), int(cfg["translit_widget_pos"]["y"]))

    def show(self):
        return super().showFullScreen(), super().setFocus()

    def hideEvent(self, a0):
        self.ui.StatsWidget.thr.terminate()
        self.timer.stop()
        return super().hideEvent(a0)

    def showEvent(self, a0):
        self.ui.StatsWidget.thr.start(QtCore.QThread.Priority.LowestPriority)
        self.timer.start(100)
        return super().showEvent(a0)

    def sh_self(self):
        if self.isHidden() == False:
            self.group_anim.finished.connect(self.hide)
            self.state = 1
            self.group_anim.setDirection(self.group_anim.Direction(1))
            self.group_anim.start()
        else:
            if self.state == 1:
                self.group_anim.finished.disconnect(self.hide)
                self.state = 0
            self.group_anim.setDirection(self.group_anim.Direction(0))
            self.group_anim.start()
            self.show()

    def save_settings(self):
        cfg["settings"] = {"theme": f"{self.ui.SettingsWidget.ui.cB.currentIndex()}",
                           "background_image": f"{self.ui.SettingsWidget.ui.lE.text()}",
                           "blur": f"{self.ui.SettingsWidget.ui.hS.value()}",
                           "autostart": f"{self.ui.SettingsWidget.ui.cBox.checkState()}",
                           "launch_hidden": f"{self.ui.SettingsWidget.ui.cBox_1.checkState()}",
                           "stat_time_startup": f"{self.ui.SettingsWidget.ui.cBox_2.checkState()}",
                           "stat_ping": f"{self.ui.SettingsWidget.ui.cBox_3.checkState()}",
                           "stat_download": f"{self.ui.SettingsWidget.ui.cBox_4.checkState()}"
                           }
        cfg["audio_widget_pos"] = {"x": f"{self.ui.AudioWidget.pos().x()}",
                                   "y": f"{self.ui.AudioWidget.pos().y()}"}
        cfg["settings_widget_pos"] = {"x": f"{self.ui.SettingsWidget.pos().x()}",
                                      "y": f"{self.ui.SettingsWidget.pos().y()}"}
        cfg["translit_widget_pos"] = {"x": f"{self.ui.TranslitWidget.pos().x()}",
                                      "y": f"{self.ui.TranslitWidget.pos().y()}"}
        deen.decrypt(path + ".cw")
        with open(path + ".ini", "w+") as file:
            cfg.write(file)
        deen.encrypt(path + ".ini")

    def close(self):
        sys.exit()

    def keyPressEvent(self, e):
        if int(e.key()) == (QtCore.Qt.Key.Key_Escape):
            self.sh_self()
        if int(e.modifiers()) == (QtCore.Qt.AltModifier):
            if e.key() == QtCore.Qt.Key_1:
                self.sh(self.ui.f_child)

    def sh(self, obj):
        if obj.isHidden() == False:
            obj.hide()
        else:
            obj.show()

    def show_time(self):
        time = QtCore.QDateTime.currentDateTime()
        self.ui.l_time.setText(time.toString("hh : mm"))

    def set_blur_img(self, value):
        self.blur_eff.setBlurRadius(value)
        self.ui.l_back_img.setGraphicsEffect(self.blur_eff)

    def check_upd(self):
        webbrowser.open(
            "https://github.com/Curicano/OverlayGT-2.0", new=0, autoraise=True)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def select_theme(self, name):
        with open(f"{self.path_to_themes}\\{name}.qss", "r") as file:
            theme = file.read()
            self.setStyleSheet(theme)
            file.close()

    def connections(self):
        self.hot_key.sh.connect(self.sh_self)
        self.timer.timeout.connect(self.show_time)
        self.ui.btn_mixer.clicked.connect(lambda: self.sh(self.ui.AudioWidget))
        self.ui.btn_interpreter.clicked.connect(
            lambda: self.sh(self.ui.TranslitWidget))
        self.ui.btn_settings.sh_signal.connect(
            lambda obj: self.sh(obj))
        self.ui.SettingsWidget.ui.hS.valueChanged.connect(self.set_blur_img)
        self.ui.SettingsWidget.ui.btn_check_upd.clicked.connect(lambda: [self.sh_self(), self.check_upd()])
        self.ui.SettingsWidget.ui.cBox_2.stateChanged.connect(
            lambda: self.sh(self.ui.StatsWidget.ui.l_stat))
        self.ui.SettingsWidget.ui.cBox_3.stateChanged.connect(
            lambda: self.sh(self.ui.StatsWidget.ui.l_stat_1))
        self.ui.SettingsWidget.ui.cBox_4.stateChanged.connect(
            lambda: self.sh(self.ui.StatsWidget.ui.l_stat_2))
        self.ui.SettingsWidget.ui.cB.currentTextChanged.connect(
            lambda name: themes.select_theme(self, self.path_to_themes, name))
        self.ui.SettingsWidget.ui.btn_save.clicked.connect(self.save_settings)


if __name__ == "__main__":
    Reg = OpenKeyEx(HKEY_LOCAL_MACHINE,
                    r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OverlayGT.exe', 0, KEY_READ)
    path = QueryValue(Reg, "")
    Reg.Close()
    path = f"{os.path.dirname(os.path.abspath(path))}\\settings"
    deen = Crypter()
    deen.decrypt(path + ".cw")
    cfg = ConfigParser()
    cfg.read(path + ".ini")
    deen.encrypt(path + ".ini")
    for arg in sys.argv:
        match arg:
            case "-autostart":
                if cfg["settings"]["autostart"] == "0":
                    sys.exit()
            case "-HDPI":
                QtWidgets.QApplication.setAttribute(
                    QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    myappid = "mycompany.myproduct.subproduct.version"
    QtWinExtras.QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    app.setCursorFlashTime(2000)
    ui = MyWidget()
    app.exec_()
