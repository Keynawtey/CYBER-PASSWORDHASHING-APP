import bcrypt

password = "spongy406"


def hash_password(password):
    bytes=password.encode("utf-8")
    salt= bcrypt.gensalt()
    hash= bcrypt.hashpw(bytes, salt)
    return hash