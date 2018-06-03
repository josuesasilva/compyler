from scanner.scanner import Scanner
from scanner.token import Token, TokenEnum

class LL1(object):
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens.append(Token(TokenEnum.EOF, "$"))
        self.index = 0
        self.keywords = ["PROGRAMA", "INTEIRO", "INICIO", "FIM", "VARIAVEIS", "REAL", "IMPRIMA", "LEIA"]
    
    def parse(self):
        pass

    def portugol(self):
        pass
    
    def statements(self):
        pass

    def statement(self):
        pass

    def vartype(self):
        pass

    def identifiers(self):
        pass

    def identifier(self):
        pass

    def instructions(self):
        pass

    def instruction(self):
        pass
    
    def assign(self):
        pass

    def read(self):
        pass

    def write(self):
        pass

    def expression(self):
        pass
    
    def opcode(self):
        pass

    def integer(self):
        pass

    def real(self):
        pass

    def text(self):
        pass

    def digit(self):
        pass

    def word(self):
        pass

    