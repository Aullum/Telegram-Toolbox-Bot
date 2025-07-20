import base64

def encode_text(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def decode_text(b64: str) -> str:
    return base64.b64decode(b64.encode("utf-8")).decode("utf-8")

def encode_file(content: bytes) -> str:
    return base64.b64encode(content).decode("utf-8")

def decode_file(b64: str) -> bytes:
    return base64.b64decode(b64.encode("utf-8"))
