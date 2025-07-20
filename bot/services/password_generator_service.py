import string
import secrets

def generate_secure_password(length: int, charsets: dict) -> str:
    pool = ""
    if charsets.get("letters"):
        pool += string.ascii_lowercase
    if charsets.get("uppercase"):
        pool += string.ascii_uppercase
    if charsets.get("digits"):
        pool += string.digits
    if charsets.get("symbols"):
        pool += string.punctuation

    if not pool:
        raise ValueError("No character sets selected.")

    return ''.join(secrets.choice(pool) for _ in range(length))
