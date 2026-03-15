from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui

class LoadingPage(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QtWidgets.QLabel(text="loading.")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.texts = ["loading.", "loading..", "loading..."]
        self.currenttext = 0
        layout.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)

        self.animtimer = QtCore.QTimer()
        self.animtimer.timeout.connect(self._update_label)
        self.animtimer.start(500)

    def _update_label(self):
        self.currenttext += 1
        self.currenttext %= len(self.texts)
        self.label.setText(self.texts[self.currenttext])