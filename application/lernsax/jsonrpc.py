import requests

url = "https://www.lernsax.de/jsonrpc.php"

def send_rpc(method: str, params: dict[str,str]) -> dict[str,str]:
    payload = {
        "method" : method,
        "params" : params,
        "jsonrpc" : "2.0",
        "id" : "1",
    }

    response = requests.post(url, json=payload).json()

    return response

if __name__ == "__main__":
    print(send_rpc("get_nonce", {}))
