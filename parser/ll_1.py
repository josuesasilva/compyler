from scanner.scanner import Scanner
from scanner.token import Token, TokenEnum
from parser.ast import *

class LL1(object):
    
    def __init__(self, tokens):
        self.ast = Portugol()
        self.tokens = tokens
        self.tokens.append(Token(TokenEnum.EOF, "$"))
        self.index = 0
        self.keywords = ["PROGRAMA", "INTEIRO", "INICIO", "FIM", "VARIAVEIS", "REAL", "IMPRIMA", "LEIA"]

    def get_token(self):
        return self.tokens[self.index].value

    def update_index(self):
        self.index += 1
    
    def parse(self):
        if self.portugol() and self.get_token() == TokenEnum.EOF:
            print("Done.\nSuccess!")
            return 0
        else:
            print("Done.\nError.")
            return 1

    def portugol(self):
        return True
    
    def statements(self):
        return

    def statement(self):
        pass

    def vartype(self):
        token = self.get_token()
        if token == 'INTEIRO':
            return True
        elif token == 'REAL':
            return True

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
        token = self.get_token()
        if token == "+":
            return True
        elif token == "-":
            return True
        elif token == "*":
            return True
        elif token == "/":
            return True

    def integer(self):
        pass

    def real(self):
        pass

    def text(self):
        pass

    def digit(self):
        return self.get_token().isnumeric() 

    def word(self):
        return self.get_token().isalpha() 

    