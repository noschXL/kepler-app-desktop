import sys
import os
import darkdetect
from util.styleloader import load_stylesheet
from ui.theme import apply_colors

from ui.gui import MainWidget
from state import *

from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    path = os.path.dirname(os.path.abspath(__file__))

    theme = "light" if darkdetect.isLight() else "dark"

    style = os.path.join(path, "ui", "qss",f"{theme}.qss")
    stylesheet = load_stylesheet(style)
    stylesheet = apply_colors(stylesheet)
    app.setStyleSheet(stylesheet)

    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()
    widget.setWindowTitle("Kepler App")

    app.exec()

    for session in state.lernsaxSessions:
        session.logout()

    sys.exit()