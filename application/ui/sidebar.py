from PySide6 import QtWidgets
from state import *

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
        self.button_group = QtWidgets.QButtonGroup(self)

        self.layout = QtWidgets.QVBoxLayout(self)

        for i, menu in enumerate(self.menus):
            # icons are set in the .qss file; these are the reasons for not using font icons:
            # https://tonsky.me/blog/centering/
            button = QtWidgets.QRadioButton("")
            button.setObjectName(menu)
            button.setFixedSize(50, 50)
            self.menubuttons.append(button)
            self.button_group.addButton(button, i)
            self.layout.addWidget(button)

        self.menubuttons[0].setChecked(True)

        self.button_group.buttonClicked.connect(self._update_stack)

    def _update_stack(self, button):
        index = self.button_group.id(button)
        state.menustack.set([index])


        



