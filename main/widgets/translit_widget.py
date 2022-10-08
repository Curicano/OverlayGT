from PyQt5 import QtCore, QtWidgets, QtGui
from translate import Translator
from image import res
from ui.widget_1 import Ui_TranslitWidget


class TranslitWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self.ui = Ui_TranslitWidget()
        self.ui.setupUi(self)
        self.rebuilder()
        self.connections()
        self.to_lang = "en"
        self.from_lang = "ru"
        self._old_pos = None

    def rebuilder(self):
        self.menu = QtWidgets.QMenu(self.ui.tE_1)
        self.menu_2 = QtWidgets.QMenu(self.ui.tE_2)
        self.sep = self.menu.addSeparator()
        self.menu.addActions([self.ui.action_1, self.ui.action_2, self.menu.addSeparator(), self.ui.action_3,
                             self.ui.action_4, self.ui.action_5, self.ui.action_6, self.menu.addSeparator(), self.ui.action_7])
        self.menu_2.addActions(
            [self.ui.action_4, self.menu_2.addSeparator(), self.ui.action_7])

    def translit(self):
        text = self.ui.tE_1.toPlainText()
        if self.ui.l_from_lang.text() == "Русский":
            self.from_lang = "ru"
            self.to_lang = "en"
        else:
            self.from_lang = "en"
            self.to_lang = "ru"

        def f(self, text, mode):
            t1 = Translator(from_lang=self.from_lang, to_lang=self.to_lang)
            t2 = t1.translate(text)
            match mode:
                case 0: self.ui.tE_2.setText(t2)
                case 1: self.ui.tE_2.setText(self.ui.tE_2.toPlainText() + t2)

        if text.__len__() > 500:
            f = [text[x:x+500] for x in range(0, len(text), 500)]
            for i in range(f.__len__()):
                f(self, f[1], 1)
        else:
            f(self, text, 0)

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

    def show_context_menu(self, point):
        self.menu.exec(self.ui.tE_1.mapToGlobal(point))

    def show_context_menu_2(self, point):
        self.menu_2.exec(self.ui.tE_2.mapToGlobal(point))

    def connections(self):
        self.ui.btn_swap_lang.clicked.connect(self.swap_lang)
        self.ui.btn_translite.clicked.connect(self.translit)
        self.ui.tE_1.customContextMenuRequested.connect(
            self.show_context_menu)
        self.ui.tE_2.customContextMenuRequested.connect(
            self.show_context_menu_2)
