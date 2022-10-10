import pyAesCrypt
from winreg import (HKEY_LOCAL_MACHINE, OpenKeyEx, QueryValue, KEY_READ)
from win32gui import EnumWindows, GetWindowText
from configparser import ConfigParser
import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtWinExtras
from image import res
from ui.main_window import Ui_Form
from volume_control import V
import webbrowser
from keyboard import add_hotkey
import win32api
VERSION = "0.0.0.1"
NAME = "OverlayGT"
s = 0


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
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
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
            self.sh(self)

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
        self.tray_icon.setToolTip(f"{NAME} v{VERSION}")
        self.tray_icon.show()

    def rebuilder(self):
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint |
                            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Tool)  # | QtCore.Qt.WindowType.Tool
        self.setWindowTitle(NAME)
        self.ui.AudioWidget.hide()
        self.ui.TranslitWidget.hide()
        self.ui.SettingsWidget.hide()
        self.ui.MusicWidget.hide()
        self.ui.SettingsWidget.ui.l.setText(
            f"Overlay GT {VERSION} (Python 3.10.7)")
        self.show_anim = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.show_anim.setDuration(500)
        self.show_anim.setStartValue(0)
        self.show_anim.setEndValue(1)

        self.show_anim_2 = QtCore.QPropertyAnimation(self, b"geometry")
        self.show_anim_2.setDuration(500)
        self.show_anim_2.setStartValue(QtCore.QRect(0, 1080, 1920, 1080))
        self.show_anim_2.setEndValue(QtCore.QRect(0, 0, 1920, 1080))
        self.show_anim_2.setDirection(1)
        self.show_anim_2.setEasingCurve(QtCore.QEasingCurve.InOutQuint)

        self.group_anim = QtCore.QParallelAnimationGroup(self)
        self.group_anim.addAnimation(self.show_anim)
        self.group_anim.addAnimation(self.show_anim_2)
        value = int(cfg["settings"]["theme"])
        self.ui.SettingsWidget.ui.cB.setCurrentIndex(value)
        self.select_theme(self.ui.SettingsWidget.ui.cB.currentText())
        value = cfg["settings"]["background_image"]
        self.ui.l_back_img.setPixmap(QtGui.QPixmap(value))
        self.ui.SettingsWidget.ui.lE.setText(value)
        value = int(cfg["settings"]["blur"])
        self.ui.SettingsWidget.ui.hS.setValue(value)
        self.ui.SettingsWidget.ui.l_num_2.setNum(value)
        self.set_blur_img(value)
        value = int(cfg["settings"]["autostart"])
        self.ui.SettingsWidget.ui.cBox.setCheckState(value)
        value = int(cfg["settings"]["launch_hidden"])
        self.ui.SettingsWidget.ui.cBox_1.setCheckState(value)
        value = int(cfg["settings"]["stat_time_startup"])
        match value:
            case 0:
                self.ui.StatsWidget.ui.l_stat.hide()
            case _:
                self.ui.StatsWidget.ui.l_stat.show()
        self.ui.SettingsWidget.ui.cBox_2.setCheckState(value)
        value = int(cfg["settings"]["stat_ping"])
        match value:
            case 0:
                self.ui.StatsWidget.ui.l_stat_1.hide()
            case _:
                self.ui.StatsWidget.ui.l_stat_1.show()
        self.ui.SettingsWidget.ui.cBox_3.setCheckState(value)
        value = int(cfg["settings"]["stat_download"])
        match value:
            case 0:
                self.ui.StatsWidget.ui.l_stat_2.hide()
            case _:
                self.ui.StatsWidget.ui.l_stat_2.show()
        self.ui.SettingsWidget.ui.cBox_4.setCheckState(value)
        self.ui.AudioWidget.move(
            int(cfg["audio_widget_pos"]["x"]), int(cfg["audio_widget_pos"]["y"]))
        self.ui.SettingsWidget.move(
            int(cfg["settings_widget_pos"]["x"]), int(cfg["settings_widget_pos"]["y"]))
        self.ui.TranslitWidget.move(
            int(cfg["translit_widget_pos"]["x"]), int(cfg["translit_widget_pos"]["y"]))
        del value

    def hide(self):
        self.ui.StatsWidget.thr.terminate()
        self.timer.stop()
        return super().hide()

    def show(self):
        self.ui.StatsWidget.thr.start(QtCore.QThread.Priority.LowestPriority)
        self.timer.start(100)
        return super().showFullScreen(), super().setFocus()

    def close(self):
        deen.decrypt(path + ".cw")
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
        with open(path + ".ini", "w+") as file:
            cfg.write(file)
        deen.encrypt(path + ".ini")
        sys.exit()

    def keyPressEvent(self, e):
        if int(e.key()) == (QtCore.Qt.Key.Key_Escape):
            self.sh(self)
        if int(e.modifiers()) == (QtCore.Qt.AltModifier):
            if e.key() == QtCore.Qt.Key_1:
                self.sh(self.ui.f_child)

    def sh(self, obj):
        global s
        if obj.isHidden() == False:
            if obj == self:
                self.group_anim.finished.connect(self.hide)
                s = 1
                self.group_anim.setDirection(self.group_anim.Direction(1))
                self.group_anim.start()
            else:
                obj.hide()
        else:
            if obj == self:
                self.group_anim.setDirection(self.group_anim.Direction(0))
                if s == 1:
                    self.group_anim.finished.disconnect(self.hide)
                    s = 0
                self.group_anim.start()
                self.show()
            else:
                obj.show()

    def show_time(self):
        time = QtCore.QDateTime.currentDateTime()
        self.ui.l_time.setText(time.toString("hh : mm"))

    def set_back_img(self, path):
        ext = os.path.splitext(path)
        if ext[1] == ".gif":
            self.ui.l_back_img.setMovie(QtGui.QMovie(path))
            self.ui.l_back_img.movie().start()
        else:
            self.ui.l_back_img.setPixmap(QtGui.QPixmap(path))

    def set_blur_img(self, value):
        self.blur_eff.setBlurRadius(value)
        self.ui.l_back_img.setGraphicsEffect(self.blur_eff)

    def check_upd(self):
        self.sh(self)
        webbrowser.open(
            "https://github.com/Curicano/OverlayGT-2.0", new=0, autoraise=True)

    def resource_path(self, relative_path):
        # Получаем абсолютный путь к ресурсам.
        try:
            # PyInstaller создает временную папку в _MEIPASS
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
        self.hot_key.sh.connect(lambda: self.sh(self))
        self.timer.timeout.connect(self.show_time)
        self.ui.btn_mixer.sh_signal.connect(lambda obj: self.sh(obj))
        self.ui.btn_interpreter.clicked.connect(
            lambda: self.sh(self.ui.TranslitWidget))
        self.ui.btn_settings.clicked.connect(
            lambda: self.sh(self.ui.SettingsWidget))
        self.ui.SettingsWidget.ui.lE.textChanged.connect(
            lambda path: self.set_back_img(path))
        self.ui.SettingsWidget.ui.hS.valueChanged.connect(self.set_blur_img)
        self.ui.SettingsWidget.ui.btn_check_upd.clicked.connect(self.check_upd)
        self.ui.SettingsWidget.ui.cBox_2.stateChanged.connect(
            lambda: self.sh(self.ui.StatsWidget.ui.l_stat))
        self.ui.SettingsWidget.ui.cBox_3.stateChanged.connect(
            lambda: self.sh(self.ui.StatsWidget.ui.l_stat_1))
        self.ui.SettingsWidget.ui.cBox_4.stateChanged.connect(
            lambda: self.sh(self.ui.StatsWidget.ui.l_stat_2))
        self.ui.SettingsWidget.ui.cB.currentTextChanged.connect(
            lambda name: self.select_theme(name))


if __name__ == "__main__":
    def check_clone():
        winlist = []
        toplist = []

        def enum_callback(hwnd, results):
            winlist.append((GetWindowText(hwnd)))

        EnumWindows(enum_callback, toplist)
        t = [(title) for title in winlist if f"{NAME}" in title]
        del winlist, toplist
        if t == [f"{NAME}"]:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setWindowIcon(QtGui.QIcon(":/img/img_12.svg"))
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.setText("Приложение уже запущено")
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            error.exec_()
            sys.exit(0)

    def start():
        try:
            myappid = "mycompany.myproduct.subproduct.version"
            QtWinExtras.QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
        except ImportError as ex:
            print(ex)
        ui = MyWidget()
        global app
        app.exec_()

    def prestart(type: int):
        global app
        app = QtWidgets.QApplication(sys.argv)
        app.setCursorFlashTime(2000)
        match type:
            case 0:
                start()
            case 1:
                # check_clone()
                start()
    Reg = OpenKeyEx(HKEY_LOCAL_MACHINE,
                    r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OverlayGT 2.0.exe', 0, KEY_READ)
    path = QueryValue(Reg, "")
    path = f"{os.path.dirname(os.path.abspath(path))}\\settings"
    #path = r"D:\Storage X\About\Programirovanie\Python\Git\OverlayGT 2.0\main\settings"
    deen = Crypter()
    deen.decrypt(path + ".cw")
    cfg = ConfigParser()
    cfg.read(path + ".ini")
    deen.encrypt(path + ".ini")
    for arg in reversed(sys.argv):
        match arg:
            case "-autostart":
                if cfg["settings"]["autostart"] == "0":
                    sys.exit()
                else:
                    prestart(0)
                    break
            case "-HDPI":
                QtWidgets.QApplication.setAttribute(
                    QtCore.Qt.AA_EnableHighDpiScaling)
            case _:
                prestart(1)
                break
