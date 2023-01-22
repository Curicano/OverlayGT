from time import sleep
from PyQt5.QtWidgets import QFrame, QMenu, QAction
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QMovie
from translate import Translator
from image import rc_res
from ui.ui_translit_widget import Ui_TranslitWidget


class Thread(QThread):
    translate_ok = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.parent = parent

    def run(self):
        sleep(1)
        text = self.parent.ui.tE_1.toPlainText()
        if self.parent.ui.l_from_lang.text() == "Русский":
            self.from_lang = "ru"
            self.to_lang = "en"
        else:
            self.from_lang = "en"
            self.to_lang = "ru"

        if text.__len__() > 500:
            n = [text[x:x+500] for x in range(0, len(text), 500)]
            for i in range(n.__len__()):
                self.translate(n[i], self.from_lang, self.to_lang, mode=1)
        else:
            self.translate(text, self.from_lang, self.to_lang)

    def translate(self, text, from_l, to_l, mode=0):
        t1 = Translator(from_lang=from_l, to_lang=to_l)
        t2 = t1.translate(text)
        match mode:
            case 0: self.translate_ok.emit(t2)
            case 1: self.translate_ok.emit(self.parent.ui.tE_2.toPlainText() + t2)


class TranslitWidget(QFrame):
    _old_pos = None
    to_lang = "en"
    from_lang = "ru"

    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.ui = Ui_TranslitWidget()
        self.ui.setupUi(self)
        self.setupUi()
        self.thr = Thread(self)
        self.connections()

    def setupUi(self):
        self.menu = QMenu(self.ui.tE_1)
        self.menu_2 = QMenu(self.ui.tE_2)
        self.menu.addActions([self.ui.action_1, self.ui.action_2, self.menu.addSeparator(), self.ui.action_3,
                             self.ui.action_4, self.ui.action_5, self.ui.action_6, self.menu.addSeparator(), self.ui.action_7])
        self.menu_2.addActions(
            [self.ui.action_4, self.menu_2.addSeparator(), self.ui.action_7])
        # self.translating = QMovie(
        #     "D:\Storage X\About\kiree\Рабочий стол\ZKZx.gif", parent=self.ui.tE_2)
        # self.translating.setDevice(self.ui.tE_2)

    def translit(self):
        # self.translating.stop()
        self.thr.terminate()
        self.thr.start()
        # self.translating.start()

    def swap_lang(self):
        tE_1, tE_2 = self.ui.tE_1.toPlainText(), self.ui.tE_2.toPlainText()
        if self.ui.l_from_lang.text() == "Русский":
            self.ui.l_from_lang.setText("Английский")
            self.ui.l_to_lang.setText("Русский")
            self.ui.tE_1.setText(tE_2)
            self.ui.tE_2.setText(tE_1)
        else:
            self.ui.l_from_lang.setText("Русский")
            self.ui.l_to_lang.setText("Английский")
            self.ui.tE_1.setText(tE_2)
            self.ui.tE_2.setText(tE_1)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_pos = None
            px, py = self.pos().x(), self.pos().y()
            sx, sy = self.size().width(), self.size().height()
            if px < 0:
                self.move(0, self.pos().y())
            elif px + sx > 1920:
                self.move(1920-sx, py)
            if py < 0:
                self.move(self.pos().x(), 0)
            elif py + sy > 1080:
                self.move(px, 1080-sy)

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def showContextMenu_1(self, point):
        self.menu.exec(self.ui.tE_1.mapToGlobal(point))

    def showContextMenu_2(self, point):
        self.menu_2.exec(self.ui.tE_2.mapToGlobal(point))

    def show_hide(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def connections(self):
        self.thr.translate_ok.connect(lambda text: self.ui.tE_2.setText(text))
        self.ui.btn_swap_lang.clicked.connect(self.swap_lang)
        self.ui.tE_1.textChanged.connect(self.translit)
        self.ui.tE_1.customContextMenuRequested.connect(self.showContextMenu_1)
        self.ui.tE_2.customContextMenuRequested.connect(self.showContextMenu_2)
