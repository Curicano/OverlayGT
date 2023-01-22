from PyQt5.QtWidgets import QMainWindow, QWidget, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QRect, QTimer, pyqtSignal
from PyQt5.QtGui import QColor, QPainter, QFont, QPen
from ui.ui_splash_screen import Ui_SplashScreen
counter = 0


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.value = 0
        self.width = 270
        self.height = 270
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = QColor(255, 200, 200)
        self.max_value = 100
        self.font_family = "Biennal Black"
        self.font_size = 40
        self.siffix = "%"
        self.text_color = QColor(255, 200, 200)
        self.resize(self.width, self.height)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

    def set_value(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, e):
        width = self.width - self.progress_width
        height = self.width - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))

        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)
        paint.setPen(pen)
        paint.drawArc(int(margin), int(margin), int(width),
                      int(height), -90*16, int(-value * 16))
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.PenStyle.NoPen)
        paint.drawRect(rect)
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignmentFlag.AlignCenter,
                       f"{self.value}{self.siffix}")
        paint.end()


class SplashScreen(QMainWindow):
    singal_show = pyqtSignal()

    def __init__(self, ver: str, mode: str):
        QMainWindow.__init__(
            self, flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.SplashScreen)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.mode = mode
        self.ui.l_version.setText(ver)

        self.progress = CircularProgress()
        self.progress.setParent(self.ui.centralwidget)
        self.progress.move(15, 15)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 255, 255, 255))
        self.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(15)

        self.show()

    def update(self):
        global counter
        self.progress.set_value(counter)
        if counter == 33:
            self.ui.l_loading.setText("Loading.")
        elif counter == 66:
            self.ui.l_loading.setText("Loading..")
        elif counter == 99:
            self.ui.l_loading.setText("Loading...")
        elif counter >= 100:
            self.timer.stop()
            if self.mode == "0":
                self.singal_show.emit()
            self.close()
        counter += 1
