from PySide6 import QtWidgets, QtGui
from lernsax.loginmanager import saveLogin
from lernsax.api import LernsaxSession
from state import *

class LoginPage(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        self.userInput = QtWidgets.QLineEdit(placeholderText="username : vornamenachname@jkgc.lernsax.de")
        self.passwordInput = QtWidgets.QLineEdit(placeholderText="password", )
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.rememberCheckbox = QtWidgets.QCheckBox("remember me?")
        self.submitButton = QtWidgets.QPushButton("Submit")

        headinglabel = QtWidgets.QLabel(text="Lernsax Login")
        font = QtGui.QFont()
        font.setPointSize(22)
        headinglabel.setFont(font)

        layout.addWidget(headinglabel)
        layout.addWidget(self.userInput)
        layout.addWidget(self.passwordInput)
        layout.addWidget(self.rememberCheckbox)
        layout.addWidget(self.submitButton)

        self.submitButton.pressed.connect(self._login)

    def _login(self):
        username = self.userInput.text()
        password = self.passwordInput.text()
        remember = self.rememberCheckbox.isChecked()

        if not username or not password:
            print("please enter username and password")
            return

        if remember:
            saveLogin(username, password)

        try:
            session = LernsaxSession(username, password)
        except ValueError:
            print("wrong creds")
            return
        except ConnectionError:
            print("couldnt connect to lernsax")
            return

        state.lernsaxSessions.append(session)
        state.currentsession = -1

        print("logged in")