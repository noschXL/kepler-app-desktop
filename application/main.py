import sys
import os
import darkdetect
from util.styleloader import load_stylesheet

from ui.gui import MainWidget

from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    path = os.path.dirname(os.path.abspath(__file__))

    theme = "light" if darkdetect.isLight() else "dark"

    style = os.path.join(path, "ui", f"{theme}.qss")
    app.setStyleSheet(load_stylesheet(style))

    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())