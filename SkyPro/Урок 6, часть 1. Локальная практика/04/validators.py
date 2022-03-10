from itertools import chain


def check_pin(pin: str) -> bool:
    if not pin.isdigit() or len(pin) != 4 or pin == '1234':
        return False
    if pin == len(pin) * pin[0]:
        return False
    return True


def check_pass(password: str) -> bool:
    if len(password) < 8:
        return False
    if not all(ch.isalnum() for ch in password):
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    if not any(ch.isalpha() for ch in password):
        return False
    return True


def check_mail(mail: str) -> bool:
    if not mail.count('@') or not mail.count('.'):
        return False
    return True


def check_name(name: str) -> bool:
    if not all(ord(ch) in chain(range(1040, 1104), [32, 1105, 1025]) for ch in name):
        return False
    return True
