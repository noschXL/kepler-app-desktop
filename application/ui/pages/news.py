import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from state import *


class NewsPage(QWidget):
    def __init__(self, url: str, js: str = "", parent=None):
        super().__init__(parent)

        self._js = js

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        self.browser.loadFinished.connect(self._on_load_finished)
        self.shouldPopStack = True
        self.load(url)

    def load(self, url: str):
        self.browser.load(QUrl(url))
        state.menustack.append(MENU_LOADING)

    def _on_load_finished(self, ok: bool):
        if self._js:
            self.browser.page().runJavaScript(self._js)

        if self.shouldPopStack:
            state.menustack.pop()
            self.shouldPopStack = False
