from random import randint


def are_you_feeling_lucky():
    punk = randint(1, 100)
    if punk == 13:
        return True
    else:
        return False
