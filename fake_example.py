import hashlib

import users_table


def create_user(username, password):
    encoded = password.encode("utf-8")
    hashed = hashlib.sha256(encoded).hexdigest()
    users_table.add_user(username, hashed)


def login(username, password):
    encoded = password.encode("utf-8")
    hashed = hashlib.sha256(encoded).hexdigest()

    return users_table.get_user(username) and \
        hashed == users_table.get_user(username)["hashed"]
