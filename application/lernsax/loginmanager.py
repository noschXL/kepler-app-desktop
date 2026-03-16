import keyring
from state import *

def saveLogin(username, password):
    keyring.set_password("KeplerApp", username, password)
    state.settings.setValue("username", username)

def getLogin(username):
    return keyring.get_password("KeplerApp", username)