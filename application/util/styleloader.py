def load_stylesheet(filename: str) -> str:
    content = ""
    with open(filename) as f:
        content = f.read()

    return content