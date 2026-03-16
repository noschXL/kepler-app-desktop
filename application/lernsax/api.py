from lernsax.jsonrpc import send_rpc
import hashlib
import requests

from lernsax.apiconstants import *

SALT = "ithinkthisisagoodenoughsalt"

def login(username: str, password: str):
    """logs in a user and returns the session"""
    session = requests.Session()
    nonce_response = send_rpc(session, "get_nonce", {})

    result = nonce_response.get("result")
    if type(result) == dict:
        returnvalue = result.get("return")
        if returnvalue == "OK":
            nonce = result.get("nonce")
            nonceid = nonce.get("id")
            noncekey = nonce.get("key")
            token = password.encode()
            hashed_password = hashlib.sha256(noncekey.encode() + SALT.encode() + token).hexdigest()

            params = {
                "login" : username,
                "nonce_id" : nonceid,
                "salt" : SALT,
                "hash" : hashed_password,
                "algorithm" : "sha256",
                "application" : "kepler_app_desktop",
                "password" : password,
            }

            

            response = send_rpc(session, "login", params)

            print(response)

            if type(response) == dict:
                returnvalue = result.get("return")
                if returnvalue == "OK":
                    return session

            raise ValueError("couldnt log in, wrong user/password")
        else:
            raise ConnectionError("invalid response, return was not OK")
        
    raise ConnectionError("no response from lernsax.de/api.php, no connection?")

class LernsaxSession():
    def __init__(self, username: str, password: str):
        self._session_id = 0
        self.session = login(username, password)

    def logout(self):
        send_rpc(self.session, "logout", {})

    def set_focus(self, obj):
        send_rpc(self.session, "set_focus", {"object": obj})