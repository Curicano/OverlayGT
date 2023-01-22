from PyQt5.QtCore import QObject, pyqtSignal
from os.path import abspath, join
from json import loads


class ThemeSelector(QObject):
    themeChanged = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        QObject.__init__(self, parent=parent)
        self.parent = parent
        self.resource_path = self.getResourcePath()
        self.style_sheet = f"{self.resource_path}\\theme.qss"
        self.colors = f"{self.resource_path}\\colors.json"

    def getResourcePath(self) -> str:
        try:
            from sys import _MEIPASS
            base_path = _MEIPASS
        except Exception:
            base_path = abspath(".")
        return join(base_path, "themes")

    def getTheme(self):
        with open(self.colors, "r") as file:
            theme_json = file.read()
        theme = loads(theme_json)
        return theme

    def getThemeColors(self, tn) -> dict:
        with open(self.colors, "r") as file:
            theme_colors_json = file.read()
        theme_colors = loads(theme_colors_json)
        return theme_colors[tn]

    def setTheme(self, tn: str) -> str:
        """tn - theme name"""
        theme_colors = self.getThemeColors(tn)
        with open(self.style_sheet, "r") as file:
            theme = file.read()
            theme = theme.replace("color255", theme_colors["color255"])
            theme = theme.replace("color200", theme_colors["color200"])
            theme = theme.replace("color100", theme_colors["color100"])
        self.themeChanged.emit(theme)
