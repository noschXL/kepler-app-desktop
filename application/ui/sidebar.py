from PySide6 import QtWidgets

class SidebarWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.menus: list[list[str]] = [
            "Startseite",
            "Stundenplan",
            "Emails",
            "Dateien",
            "Messenger",
            "Aufgaben",
            "Essen",
        ]
        self.menubuttons = []

        self.layout = QtWidgets.QVBoxLayout(self)

        for menu in self.menus:
            # icons are set in the .qss file; these are the reasons for not using font icons:
            # https://tonsky.me/blog/centering/
            button = QtWidgets.QRadioButton("")
            button.setObjectName(menu)
            button.setFixedSize(50, 50)
            self.menubuttons.append(button)
            self.layout.addWidget(button)

        self.menubuttons[0].setChecked(True)


        



