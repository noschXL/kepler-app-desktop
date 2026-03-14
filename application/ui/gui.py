import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from ui.sidebar import SidebarWidget

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar = SidebarWidget()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.sidebar)