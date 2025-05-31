#Melissa Louise Bangloy 1468444
#https://github.com/melissa0987/password-generator

import random
import string

DEFAULT_LENGTH = 16


class Config:
    def __init__(self, length=DEFAULT_LENGTH, lower=True, upper=True, digits=True, symbols=True, validate=False):
        self.length = length
        self.lower = lower
        self.upper = upper
        self.digits = digits
        self.symbols = symbols
        self.validate = validate


def get_chars(config):
    chars = ""
    if config.lower:
        chars += string.ascii_lowercase  # abc...
    if config.upper:
        chars += string.ascii_uppercase  # ABC...
    if config.digits:
        chars += string.digits  # 0123456789
    if config.symbols:
        chars += string.punctuation  # !@#$%^&...

    if not chars:
        return None

    return chars


def gen_password(chars, length): 
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


def validate_password(password, config):
    if not config.validate:
        return True  # No need to validate

    if config.lower and not any(c.islower() for c in password):
        return False
    if config.upper and not any(c.isupper() for c in password):
        return False
    if config.digits and not any(c.isdigit() for c in password):
        return False
    if config.symbols and not any(c in string.punctuation for c in password):
        return False

    return True
