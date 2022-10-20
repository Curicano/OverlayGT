import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from ui.splash_screen import Ui_SplashScreen
counter = 0


class CircularProgress(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.value = 0
        self.width = 270
        self.height = 270
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = QtGui.QColor(255, 200, 200)
        self.max_value = 100
        self.font_family = "Biennal Black"
        self.font_size = 40
        self.siffix = "%"
        self.text_color = QtGui.QColor(255, 200, 200)
        self.resize(self.width, self.height)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

    def set_value(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, e):
        width = self.width - self.progress_width
        height = self.width - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        paint.setFont(QtGui.QFont(self.font_family, self.font_size))

        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(QtCore.Qt.RoundCap)
        paint.setPen(pen)
        paint.drawArc(int(margin), int(margin), int(width),
                      int(height), -90*16, int(-value * 16))
        rect = QtCore.QRect(0, 0, self.width, self.height)
        paint.setPen(QtCore.Qt.PenStyle.NoPen)
        paint.drawRect(rect)
        pen.setColor(QtGui.QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter,
                       f"{self.value}{self.siffix}")
        paint.end()


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.SplashScreen)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.progress = CircularProgress()
        self.progress.setParent(self.ui.centralwidget)
        self.progress.move(15, 15)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.update(parent))

    def showEvent(self, e):
        self.timer.start(15)

    def update(self, parent):
        global counter
        self.progress.set_value(counter)
        if counter >= 100:
            self.timer.stop()
            parent.sh_self()
            self.hide()
        counter += 1
