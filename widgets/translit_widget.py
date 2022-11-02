from time import sleep
from PyQt5 import QtCore, QtWidgets, QtGui
from translate import Translator
from image import res


class Thread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent=parent)
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
            case 0: self.signal.emit(t2)
            case 1: self.signal.emit(self.parent.ui.tE_2.toPlainText() + t2)


class TranslitWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = parent.parent().ui
        self.thr = Thread(self)
        self.connections()
        self.to_lang = "en"
        self.from_lang = "ru"
        self._old_pos = None

    def translit(self):
        self.thr.terminate()
        self.thr.start()

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

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
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

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def connections(self):
        self.thr.signal.connect(lambda text: self.ui.tE_2.setText(text))
