from enum import Enum

class TokenEnum(Enum):
    IDENTIFIER = 1
    TYPE = 2
    INTEGER = 3
    COLON = 4
    SEMICOLON = 5
    COMMA = 6
    ASSIGNMENT = 7
    KEYWORD = 8

class Token(object):

    def __init__(self, token, value):
        self.token = token
        self.value = value

    def __str__(self):
        return "%s -> %s", self.token, self.value
