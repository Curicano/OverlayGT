from PyQt5.QtCore import QPoint, Qt, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, QTimer
from PyQt5.QtWidgets import QStackedWidget



class SlidingStackedWidget(QStackedWidget):
    LEFT2RIGHT, RIGHT2LEFT, TOP2BOTTOM, BOTTOM2TOP, AUTOMATIC = range(5)
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)
        self._pnow = QPoint(0, 0)
        # Скорость анимации
        self._speed = 2000
        # Текущий индекс
        self._now = 0
        # Текущий индекс автоматического режима
        self._current = 0
        # Следующий индекс
        self._next = 0
        # Включить
        self._active = 0
        # Анимация (по умолчанию - пейзаж)
        self._orientation = Qt.Orientation.Horizontal
        # Тип кривой анимации
        self._easing = QEasingCurve.Type.OutExpo
        self._initAnimation()

    def slideInIdx(self, idx, direction=4):
        """ Слайд к указанному серийному номеру
        :param idx:               Серийный номер
        :type idx:                int
        :param direction:         Направление, по умолчанию автоматически  AUTOMATIC=4
        :type direction:          int
        """
        if idx > self.count() - 1:
            direction = self.TOP2BOTTOM if self._orientation == Qt.Orientation.Vertical else self.RIGHT2LEFT
            idx = idx % self.count()
        elif idx < 0:
            direction = self.BOTTOM2TOP if self._orientation == Qt.Orientation.Vertical else self.LEFT2RIGHT
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx), direction)

    def slideInWgt(self, widget, direction):
        """ Слайд к указанному виджету
        :param widget:        QWidget, QLabel, etc...
        :type widget:         QWidget Base Class
        :param direction:     направление
        :type direction:      int
        """
        if self._active:
            return
        self._active = 1
        _now = self.currentIndex()
        _next = self.indexOf(widget)
        if _now == next:
            self._active = 0
            return

        w_now = self.widget(_now)
        w_next = self.widget(_next)

        # Направление
        if _now < _next:
            directionhint = self.TOP2BOTTOM if self._orientation == Qt.Orientation.Vertical else self.RIGHT2LEFT
        else:
            directionhint = self.BOTTOM2TOP if self._orientation == Qt.Orientation.Vertical else self.LEFT2RIGHT
        if direction == self.AUTOMATIC:
            direction = directionhint

        # Вычислить смещение
        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()
        w_next.setGeometry(0, 0, offsetX, offsetY)

        if direction == self.BOTTOM2TOP:
            offsetX = 0
            offsetY = -offsetY
        elif direction == self.TOP2BOTTOM:
            offsetX = 0
        elif direction == self.RIGHT2LEFT:
            offsetX = -offsetX
            offsetY = 0
        elif direction == self.LEFT2RIGHT:
            offsetY = 0

        # Переместите следующий виджет с областью отображения
        pnext = w_next.pos()
        pnow = w_now.pos()
        self._pnow = pnow

        # Перемещение в указанное место и отображение
        w_next.move(pnext.x() - offsetX, pnext.y() - offsetY)
        w_next.show()
        w_next.raise_()

        self._animnow.setTargetObject(w_now)
        self._animnow.setDuration(self._speed)
        self._animnow.setEasingCurve(self._easing)
        self._animnow.setStartValue(QPoint(pnow.x(), pnow.y()))
        self._animnow.setEndValue(
            QPoint(offsetX + pnow.x(), offsetY + pnow.y()))

        self._animnext.setTargetObject(w_next)
        self._animnext.setDuration(self._speed)
        self._animnext.setEasingCurve(self._easing)
        self._animnext.setStartValue(
            QPoint(-offsetX + pnext.x(), offsetY + pnext.y()))
        self._animnext.setEndValue(QPoint(pnext.x(), pnext.y()))

        self._next = _next
        self._now = _now
        self._active = 1
        self._animgroup.start()

    def _initAnimation(self):
        # Текущая анимация страницы
        self._animnow = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # Анимация следующей страницы
        self._animnext = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # Группа параллельной анимации
        self._animgroup = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot)
        self._animgroup.addAnimation(self._animnow)
        self._animgroup.addAnimation(self._animnext)

    def setCurrentIndex(self, index):
        # Переопределить переключатель анимации
        self.slideInIdx(index)

    def setCurrentWidget(self, widget):
        # Переопределить переключатель анимации
        super(SlidingStackedWidget, self).setCurrentWidget(widget)
        self.setCurrentIndex(self.indexOf(widget))

    def animationDoneSlot(self):
        """ Функция обработки конца анимации """
        # Поскольку метод setCurrentIndex перезаписан,
        # здесь используется метод самого родительского класса.
        QStackedWidget.setCurrentIndex(self, self._next)
        w = self.widget(self._now)
        w.hide()
        w.move(self._pnow)
        self._active = 0


    def autoStart(self, msec=5000):
        if not hasattr(self, '_autoTimer'):
            self._autoTimer = QTimer(self, timeout=self._autoStart)
        self._autoTimer.stop()
        self._autoTimer.start(msec)

    def autoStop(self):
        """ Остановить автовоспроизведение"""
        if hasattr(self, '_autoTimer'):
            self._autoTimer.stop()

    def _autoStart(self):
        if self._current == self.count():
            self._current = 0
        self._current += 1
        self.setCurrentIndex(self._current)
