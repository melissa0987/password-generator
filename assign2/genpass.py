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
    if config.validate:  # If validation is ON
        if config.lower:
            if not any(c in string.ascii_lowercase for c in password):
                return False
        if config.upper:
            if not any(c in string.ascii_uppercase for c in password):
                return False
        if config.digits:
            if not any(c in string.digits for c in password):
                return False
        if config.symbols:
            if not any(c in string.punctuation for c in password):
                return False
    return True
