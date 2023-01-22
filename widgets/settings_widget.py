from os.path import splitext, isfile, isdir
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QFrame, QAction, QLabel, QFileDialog, QMenu, QGraphicsBlurEffect
from PyQt5.QtGui import QPixmap, QMovie
from ui.ui_settings_widget import Ui_SettingsWidget


class SettingsWidget(QFrame):
    extensions = (".png", ".jpg", ".jpeg")
    _old_pos = None

    def __init__(self, parent=None, parent_ui=None) -> None:
        QFrame.__init__(self, parent=parent)
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)
        self.parent_ui = parent_ui
        self.menu = QMenu(self)
        self.action_1 = QAction("Добавить файл")
        # self.action_2 = QAction("Добавить папку")
        self.action_3 = QAction("Очистить")
        # self.menu.addActions([self.action_1, self.action_2, self.action_3])
        self.menu.addActions([self.action_1, self.action_3])
        self.blur_eff = QGraphicsBlurEffect()
        self.connections()
        self.slideshow = self.parent_ui.stackedWidget
        self.background_image = self.parent_ui.label

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event) -> None:
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

    def mouseMoveEvent(self, event) -> None:
        if not self._old_pos:
            return

        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def show_context_menu(self, point) -> None:
        self.menu.exec(self.ui.tB.mapToGlobal(QPoint(10, 10)))

    def clear_stack_widget(self) -> None:
        for children in self.slideshow.findChildren(QLabel):
            children.deleteLater()

    def selectFile(self) -> None:
        i0 = QFileDialog.getOpenFileName(
            parent=self, caption="Выберите файл", directory=None, filter="Image (*.png *.jpg);; GIF (*.gif)")[0]
        if not i0:
            return
        self.ui.lE.setText(i0)

    # def selectFolder(self):
    #     i0 = QFileDialog.getExistingDirectory(
    #         parent=self, caption="Выберите папку", directory=None)
    #     if not i0:
    #         return
    #     self.ui.lE.setText(i0)

    def setBackgroundFromFile(self, img: str = "") -> None:
        ext = splitext(img)[1]
        match ext:
            case ".gif":
                self.background_image.setMovie(QMovie(img))
                self.background_image.movie().start()
            case ".png" | ".jpg":
                self.background_image.setPixmap(QPixmap(img).scaled(
                    self.background_image.size(),
                    Qt.AspectRatioMode.IgnoreAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
            case _:
                self.background_image.setPixmap(QPixmap())

    # def setBackgroundFromFolder(self, path):
    #     try:
    #         for name in os.listdir(path):
    #             ext = os.path.splitext(name)[1]
    #             if not ext in self.extensions:
    #                 continue
    #             label = QLabel(self.slideshow)
    #             label.setObjectName(name)
    #             label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    #             label.setPixmap(
    #                 QPixmap(f"{path}/{name}").scaled(
    #                     self.slideshow.size(),
    #                     Qt.AspectRatioMode.IgnoreAspectRatio,
    #                     Qt.TransformationMode.SmoothTransformation))
    #             label.setSizePolicy(
    #                 QSizePolicy.Expanding, QSizePolicy.Expanding)
    #             self.slideshow.addWidget(label)
    #             self.slideshow.autoStart()
    #     except Exception as ex:
    #         print(ex)

    def clearBackground(self) -> None:
        self.setBackgroundFromFile()
        self.clear_stack_widget()

    def check_path(self, path) -> None:
        if isfile(path):
            self.setBackgroundFromFile(path)
        # elif os.path.isdir(path):
        #     self.setBackgroundFromFolder(path)
        elif not path:
            self.clearBackground()

    def setBlurImage(self, value) -> None:
        self.blur_eff.setBlurRadius(value)
        self.slideshow.setGraphicsEffect(self.blur_eff)
        self.background_image.setGraphicsEffect(self.blur_eff)
        self.ui.l_num.setNum(value)

    def show_hide(self) -> None:
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def connections(self) -> None:
        self.action_1.triggered.connect(self.selectFile)
        # self.action_2.triggered.connect(self.selectFolder)
        self.ui.hS.valueChanged.connect(self.setBlurImage)
        self.ui.tB.clicked.connect(self.show_context_menu)
        self.ui.lE.textChanged.connect(self.check_path)
        self.action_3.triggered.connect(self.ui.lE.clear)
        self.ui.btn_create_new_theme.clicked.connect
