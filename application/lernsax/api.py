from lernsax.jsonrpc import send_rpc
import hashlib

SALT = "ithinkthisisagoodenoughsalt"

def login(username: str, password: str):
    """logs in a user and returns the session"""
    nonce_response = send_rpc("get_nonce", {})

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

            session = send_rpc("login", params)

            return session
        else:
            raise ValueError("invalid response, return was not OK")
        
    raise ValueError("no response from lernsax.de/api.php, no connection?")


if __name__ == "__main__":
    user = input("username: ")
    pas = input("pass: ")
    print(login(user, pas))
