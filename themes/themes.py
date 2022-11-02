def select_theme(self, path, name):
    match name:
        case "White":
            color255 = "rgba(255, 255, 255, 255)"
            color200 = "rgba(255, 255, 255, 200)"
            color100 = "rgba(255, 255, 255, 100)"
        case "Red":
            color255 = "rgba(255, 0, 0, 255)"
            color200 = "rgba(255, 0, 0, 200)"
            color100 = "rgba(255, 0, 0, 100)"
        case "Green":
            color255 = "rgba(0, 255, 0, 255)"
            color200 = "rgba(0, 255, 0, 200)"
            color100 = "rgba(0, 255, 0, 100)"
        case "Blue":
            color255 = "rgba(0, 0, 255, 255)"
            color200 = "rgba(0, 0, 255, 200)"
            color100 = "rgba(0, 0, 255, 100)"
        case "Violet":
            color255 = "rgba(135, 0, 255, 255)"
            color200 = "rgba(135, 0, 255, 200)"
            color100 = "rgba(135, 0, 255, 100)"
        case "Yellow":
            color255 = "rgba(255, 255, 0, 255)"
            color200 = "rgba(255, 255, 0, 200)"
            color100 = "rgba(255, 255, 0, 100)"
        case "Blue Red":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 255), stop:1 rgba(255, 0, 0, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 200), stop:1 rgba(255, 0, 0, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 100), stop:1 rgba(255, 0, 0, 100))"
        case "Cold":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(155, 195, 250, 255), stop:1 rgba(215, 190, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(155, 195, 250, 200), stop:1 rgba(215, 190, 255, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(155, 195, 250, 100), stop:1 rgba(215, 190, 255, 100))"
        case "Fire Violet":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 255), stop:1 rgba(135, 0, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 200), stop:1 rgba(135, 0, 255, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 100), stop:1 rgba(135, 0, 255, 100))"
        case "Fire":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 255), stop:1 rgba(255, 170, 40, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 200), stop:1 rgba(255, 170, 40, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 150, 0, 100), stop:1 rgba(255, 170, 40, 100))"
        case "Fuxia Neon Violet":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 65, 100, 255), stop:1 rgba(190, 20, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 65, 100, 200), stop:1 rgba(190, 20, 255, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 65, 100, 100), stop:1 rgba(190, 20, 255, 100))"
        case "Fuxia Neon Yellow":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 90, 195, 255), stop:1 rgba(205, 255, 5, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 90, 195, 200), stop:1 rgba(205, 255, 5, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 90, 195, 100), stop:1 rgba(205, 255, 5, 100))"
        case "Gray":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(120, 120, 120, 255), stop:1 rgba(120, 120, 120, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(120, 120, 120, 200), stop:1 rgba(120, 120, 120, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(120, 120, 120, 100), stop:1 rgba(120, 120, 120, 100))"
        case "Green Violet":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 130, 0, 255), stop:1 rgba(135, 0, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 130, 0, 200), stop:1 rgba(135, 0, 255, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 130, 0, 100), stop:1 rgba(135, 0, 255, 100))"
        case "Ice Fire":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 255), stop:1 rgba(255, 170, 40, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 200), stop:1 rgba(255, 170, 40, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 100), stop:1 rgba(255, 170, 40, 100))"
        case "Ice Green":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 254, 255), stop:1 rgba(75, 180, 80, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 254, 200), stop:1 rgba(75, 180, 80, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 254, 100), stop:1 rgba(75, 180, 80, 100))"
        case "Ice Violet":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 255), stop:1 rgba(135, 0, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 200), stop:1 rgba(135, 0, 255, 255))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 100), stop:1 rgba(135, 0, 255, 255))"
        case "Ice":
            color255 = "rgba(70, 140, 255, 255)"
            color200 = "rgba(70, 140, 255, 200)"
            color100 = "rgba(70, 140, 255, 100)"
        case "Lineage":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(25, 125, 130, 255), stop:1 rgba(100, 255, 220, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(25, 125, 130, 200), stop:1 rgba(100, 255, 220, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(25, 125, 130, 100), stop:1 rgba(100, 255, 220, 100))"
        case "Neon Yellow Ice":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 210, 0, 255), stop:1 rgba(5, 220, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 210, 0, 200), stop:1 rgba(5, 220, 255, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 210, 0, 100), stop:1 rgba(5, 220, 255, 100))"
        case "Old Ice":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 255), stop:1 rgba(130, 180, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 255), stop:1 rgba(130, 180, 255, 255))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 140, 255, 255), stop:1 rgba(130, 180, 255, 255))"
        case "Orange Gray":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 85, 35, 255), stop:1 rgba(120, 120, 120, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 85, 35, 200), stop:1 rgba(120, 120, 120, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 85, 35, 100), stop:1 rgba(120, 120, 120, 100))"
        case "Orange":
            color255 = "rgba(255, 85, 35, 255)"
            color200 = "rgba(255, 85, 35, 200)"
            color100 = "rgba(255, 85, 35, 100)"
        case "Pink Gray":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 80, 140, 255), stop:1 rgba(120, 120, 120, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 80, 140, 200), stop:1 rgba(120, 120, 120, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 80, 140, 100), stop:1 rgba(120, 120, 120, 100))"
        case "Red Violet":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 65, 55, 255), stop:1 rgba(135, 0, 255, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 65, 55, 200), stop:1 rgba(135, 0, 255, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 65, 55, 100), stop:1 rgba(135, 0, 255, 100))"
        case "Violet Fire":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 255), stop:1 rgba(255, 150, 0, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 200), stop:1 rgba(255, 150, 0, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 100), stop:1 rgba(255, 150, 0, 100))"
        case "Violet Gray":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 255), stop:1 rgba(120, 120, 120, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 200), stop:1 rgba(120, 120, 120, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 100), stop:1 rgba(120, 120, 120, 100))"
        case "Violet Green":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 255), stop:1 rgba(40, 130, 0, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 200), stop:1 rgba(40, 130, 0, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 100), stop:1 rgba(40, 130, 0, 100))"
        case "Violet Ice":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 255), stop:1 rgba(80, 240, 195, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 200), stop:1 rgba(80, 240, 195, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 100), stop:1 rgba(80, 240, 195, 100))"
        case "Violet Red":
            color255 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 255), stop:1 rgba(255, 65, 55, 255))"
            color200 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 200), stop:1 rgba(255, 65, 55, 200))"
            color100 = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 0, 255, 100), stop:1 rgba(255, 65, 55, 100))"


    with open(f"{path}\\theme.qss", "r") as file:
        theme = file.read()
        theme = theme.replace("color255", color255)
        theme = theme.replace("color200", color200)
        theme = theme.replace("color100", color100)
        self.setStyleSheet(theme)