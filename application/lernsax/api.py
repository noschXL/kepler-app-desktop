from lernsax.jsonrpc import send_rpc


def login(username: str, password: str) -> str:
    """logs in a user and returns the session"""
    nonce_response = send_rpc("get_nonce", {})

    result = nonce_response.get("result")
    if result is not None:
        returnvalue = result.get("return")
        if returnvalue == "OK":
            nonce = returnvalue.get("nonce")
            sessionid = nonce.get("id")
            noncekey = nonce.get("key")
        
        
    raise ValueError(" nonce['return'] != 'OK' ")
