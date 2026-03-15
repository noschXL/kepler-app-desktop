from PySide6 import QtCore, QtWidgets, QtGui
from ui.sidebar import SidebarWidget
from ui.pages.news import NewsPage
from ui.pages.loading import LoadingPage
from state import *

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar = SidebarWidget()

        self.stack = QtWidgets.QStackedWidget()
        self.stack.addWidget(LoadingPage())
        self.stack.addWidget(NewsPage("https://www.kepler-chemnitz.de/blog/"))
        self.stack.setCurrentIndex(state.menustack[-1])

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.stack)

        state.menustack.changed.connect(self._update_stack)

    def _update_stack(self):
        self.stack.setCurrentIndex(state.menustack[-1])