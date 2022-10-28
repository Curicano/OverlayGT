from os import remove
from os.path import splitext, abspath, join, dirname
import sys
import traceback
from webbrowser import open
from configparser import ConfigParser
from datetime import datetime
from winreg import HKEY_LOCAL_MACHINE, KEY_READ, OpenKeyEx, QueryValue

from pyAesCrypt import encryptFile, decryptFile
from pyautogui import press
from win32api import LoadKeyboardLayout
from keyboard import add_hotkey
from PyQt5 import QtCore, QtGui, QtWidgets, QtWinExtras

from image import res
from themes import themes
from ui.main_window import Ui_MainWindow
from widgets.splash_screen import SplashScreen

NAME = "OverlayGT"
VERSION = "v0.0.0.3"


class Crypter():
    def __init__(self):
        super().__init__()
        self.password = "0000"
        self.buffer = 512*1024

    def encrypt(self, file):
        ext = splitext(file)[0]
        encryptFile(
            file, ext.lower() + ".ccw", self.password, self.buffer)
        remove(file)

    def decrypt(self, file):
        ext = splitext(file)[0]
        decryptFile(
            file, ext.lower() + ".ini", self.password, self.buffer)
        remove(file)


class HotKey(QtCore.QObject):
    sh = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        LoadKeyboardLayout("00000419", 1)
        add_hotkey(
            "alt + ё", self.sh.emit, suppress=True, trigger_on_release=True)


class MyWidget(QtWidgets.QMainWindow):
    state = 0

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tray()
        self.hot_key = HotKey()
        self.path_to_resource = self.resource_path("themes")
        self.connections()
        self.rebuilder()
        self.create_menu()
        self.splash_screen = SplashScreen(self)
        if cfg["settings"]["launch_hidden"] == "0":
            self.sh(self.splash_screen)

    def create_menu(self):
        self.menu = QtWidgets.QMenu(self.ui.tE_1)
        self.menu_2 = QtWidgets.QMenu(self.ui.tE_2)
        self.menu.addActions([self.ui.action_1, self.ui.action_2, self.menu.addSeparator(), self.ui.action_3,
                             self.ui.action_4, self.ui.action_5, self.ui.action_6, self.menu.addSeparator(), self.ui.action_7])
        self.menu_2.addActions(
            [self.ui.action_4, self.menu_2.addSeparator(), self.ui.action_7])

    def show_context_menu(self, point):
        self.menu.exec(self.ui.tE_1.mapToGlobal(point))

    def show_context_menu_2(self, point):
        self.menu_2.exec(self.ui.tE_2.mapToGlobal(point))

    def tray(self):
        tray_icon = QtWidgets.QSystemTrayIcon(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        tray_icon.setIcon(icon)
        quit_action = QtWidgets.QAction("Выйти", self)
        quit_action.triggered.connect(self.close)
        show_action = QtWidgets.QAction("Показать", self)
        show_action.triggered.connect(self.sh_self)
        check_upd_action = QtWidgets.QAction(
            "Проверить обновления", self)
        check_upd_action.triggered.connect(self.check_upd)
        tray_menu = QtWidgets.QMenu()
        tray_menu.addActions(
            [quit_action, show_action, check_upd_action])
        tray_icon.setContextMenu(tray_menu)
        tray_icon.setToolTip(
            f"{NAME} {VERSION}")
        tray_icon.show()

    def rebuilder(self):
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint |
                            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Tool)
        self.ui.AudioWidget.hide()
        self.ui.TranslitWidget.hide()
        self.ui.SettingsWidget.hide()
        self.ui.VersionWidget.hide()
        self.ui.VersionWidget.move(QtCore.QPoint(1080, 55))
        self.ui.TimeWidget.hide()
        self.ui.TimeWidget.move(QtCore.QPoint(870, 120))
        self.ui.l_stat.hide()
        self.ui.l_stat_1.hide()
        self.ui.l_stat_2.hide()
        self.ui.l_1.setText(
            f"{NAME} {VERSION} (Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")
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

        self.ui.cB.setCurrentText(cfg["settings"]["theme"])
        self.ui.lE.setText(
            cfg["settings"]["background_image"])
        self.ui.hS_2.setValue(int(cfg["settings"]["blur"]))
        self.ui.cBox.setCheckState(
            int(cfg["settings"]["autostart"]))
        self.ui.cBox_1.setCheckState(
            int(cfg["settings"]["launch_hidden"]))
        self.ui.cBox_2.setCheckState(
            int(cfg["settings"]["stat_time_startup"]))
        self.ui.cBox_3.setCheckState(
            int(cfg["settings"]["stat_ping"]))
        self.ui.cBox_4.setCheckState(
            int(cfg["settings"]["stat_download"]))
        self.ui.AudioWidget.move(
            int(cfg["audio_widget"]["posx"]), int(cfg["audio_widget"]["posy"]))
        self.ui.SettingsWidget.move(
            int(cfg["settings_widget"]["posx"]), int(cfg["settings_widget"]["posy"]))
        self.ui.TranslitWidget.move(
            int(cfg["translit_widget"]["posx"]), int(cfg["translit_widget"]["posy"]))

    def show(self):
        return super().showFullScreen(), super().setFocus()

    def hideEvent(self, a0):
        self.ui.StatsWidget.thr.terminate()
        return super().hideEvent(a0)

    def showEvent(self, a0):
        self.ui.StatsWidget.thr.start(QtCore.QThread.Priority.LowestPriority)
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
        cfg["settings"] = {"theme": f"{self.ui.cB.currentText()}",
                           "background_image": f"{self.ui.lE.text()}",
                           "blur": f"{self.ui.hS_2.value()}",
                           "autostart": f"{self.ui.cBox.checkState()}",
                           "launch_hidden": f"{self.ui.cBox_1.checkState()}",
                           "stat_time_startup": f"{self.ui.cBox_2.checkState()}",
                           "stat_ping": f"{self.ui.cBox_3.checkState()}",
                           "stat_download": f"{self.ui.cBox_4.checkState()}"
                           }
        cfg["audio_widget"] = {"posx": f"{self.ui.AudioWidget.pos().x()}",
                               "posy": f"{self.ui.AudioWidget.pos().y()}"}
        cfg["settings_widget"] = {"posx": f"{self.ui.SettingsWidget.pos().x()}",
                                  "posy": f"{self.ui.SettingsWidget.pos().y()}"}
        cfg["translit_widget"] = {"posx": f"{self.ui.TranslitWidget.pos().x()}",
                                  "posy": f"{self.ui.TranslitWidget.pos().y()}"}
        deen.decrypt(path + "settings.ccw")
        with open(path + "settings.ini", "w+") as file:
            cfg.write(file)
        deen.encrypt(path + "settings.ini")

    def close(self):
        self.save_settings()
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

    def check_upd(self):
        open(
            "https://github.com/Curicano/OverlayGT-2.0", new=0, autoraise=True)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = abspath(".")
        return join(base_path, relative_path)

    def connections(self):
        self.hot_key.sh.connect(self.sh_self)
        self.ui.btn_mixer.clicked.connect(lambda: self.sh(self.ui.AudioWidget))
        self.ui.btn_interpreter.clicked.connect(
            lambda: self.sh(self.ui.TranslitWidget))
        self.ui.btn_settings.sh_signal.connect(
            lambda obj: self.sh(obj))
        self.ui.btn_check_upd.clicked.connect(
            lambda: [self.sh_self(), self.check_upd()])
        self.ui.cBox_2.stateChanged.connect(
            lambda: self.sh(self.ui.l_stat))
        self.ui.cBox_3.stateChanged.connect(
            lambda: self.sh(self.ui.l_stat_1))
        self.ui.cBox_4.stateChanged.connect(
            lambda: self.sh(self.ui.l_stat_2))
        self.ui.cB.currentTextChanged.connect(
            lambda name: themes.select_theme(self, self.path_to_resource, name))
        self.ui.btn_save.clicked.connect(self.save_settings)
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_prev.clicked.connect(lambda: press("prevtrack"))
        self.ui.btn_next.clicked.connect(lambda: press("nexttrack"))
        self.ui.btn_pp.clicked.connect(lambda: press("playpause"))
        self.ui.btn_move.clicked.connect(self.ui.AudioWidget.startAnim)
        self.ui.btn_swap_lang.clicked.connect(self.ui.TranslitWidget.swap_lang)
        self.ui.tE_1.textChanged.connect(self.ui.TranslitWidget.translit)
        self.ui.btn_translite.clicked.connect(self.ui.TranslitWidget.translit)
        self.ui.tE_1.customContextMenuRequested.connect(
            self.show_context_menu)
        self.ui.tE_2.customContextMenuRequested.connect(
            self.show_context_menu_2)
        self.ui.lE.textChanged.connect(self.ui.SettingsWidget.check_path)
        self.ui.hS_2.valueChanged.connect(self.ui.SettingsWidget.set_blur_img)
        self.ui.hS_2.valueChanged.connect(self.ui.l_num_2.setNum)
        self.ui.tB.clicked.connect(self.ui.SettingsWidget.show_context_menu)
        self.ui.l_time.clicked.connect(lambda: self.sh(self.ui.TimeWidget))


def my_excepthook(t, v, tb):
    with open(path + 'log.txt', 'a') as f:
        f.write("\n---===Error===---\n")
        f.write("Time = %s\n" % datetime.now())
        traceback.print_exception(t, v, tb, file=f)


if __name__ == "__main__":
    sys.excepthook = my_excepthook
    Reg = OpenKeyEx(HKEY_LOCAL_MACHINE,
                    r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OverlayGT.exe', 0, KEY_READ)
    path = QueryValue(Reg, "")
    Reg.Close()
    path = f"{dirname(abspath(path))}\\"
    deen = Crypter()
    deen.decrypt(path + "settings.ccw")
    cfg = ConfigParser()
    cfg.read(path + "settings.ini")
    deen.encrypt(path + "settings.ini")
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
