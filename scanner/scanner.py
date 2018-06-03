from scanner.token import Token, TokenEnum

import ipdb


class Scanner(object):

    def __init__(self, stream):
        self.stream = stream
        self.eof = self.stream.tell() 
        self.stream.seek(0, 0)
        self.tokens = {}

    def peek(self):
        pos = self.stream.tell()
        input = self.stream.read(1)
        self.stream.seek(pos)
        return input

    def peek_line(self):
        pos = self.stream.tell()
        line = self.stream.readline()
        self.stream.seek(pos)
        return line
    
    def get(self):
        return self.stream.read(1)

    def get_line(self):
        return self.stream.readline()

    def is_eof(self):
        return self.peek() == ''

    def add_token(self, token, value):
        if not token in self.tokens.keys():
            self.tokens[token] = []
        self.tokens[token].append(value)

    def is_linecomment(self):
        line = self.peek_line()

        if line.startswith("//"):
            return True
        
        return False

    def ignore_blockcomment(self):
        line = self.peek_line()

        if line.startswith("/*"):
            
            if line.endswith("*/") or line.endswith("*/\n"):
                self.get_line()
                return

            while not self.is_eof():
                line = self.get_line()
                
                if line.endswith("*/") or line.endswith("*/\n"):
                    return

    def igonre_linecomment(self):
        if self.is_linecomment():
            self.get_line()

    def scan(self):
        while not self.is_eof():
            
            self.igonre_linecomment()
            self.ignore_blockcomment()

            char = self.get()
            state = -1
            
            if char == " " or char == "\t" or char == "\n":
                continue

            if char.isnumeric() or char == "-":
                state = 0
            elif char.isalpha():
                state = 1
            elif char == "\"":
                state = 3

            if state == 0:
                sentence = ""
                is_float = False
                
                if char == "-":
                    sentence += char
                    char = self.get()

                while char.isnumeric() or char == ".":
                    if char == ".":
                        is_float = True

                    sentence += char
                    char = self.get()
                    
                if is_float:
                    self.add_token(TokenEnum.FLOAT, sentence)
                else:
                    self.add_token(TokenEnum.INTEGER, sentence)
            elif state == 1:
                sentence = ""
                while char.isalpha() or char.isnumeric():
                    sentence += char
                    char = self.get()
                if sentence == "INTEIRO" or sentence == "REAL":
                    self.add_token(TokenEnum.TYPE, sentence)
                elif sentence in ["PROGRAMA", "INTEIRO", "INICIO", "FIM", "VARIAVEIS", "REAL", "IMPRIMA", "LEIA"]:
                    self.add_token(TokenEnum.KEYWORD, sentence)
                else:
                    self.add_token(TokenEnum.IDENTIFIER, sentence)
            elif state == 2:
                sentence = char
                char = self.get()
                while char.isnumeric():
                    sentence += char
                    char = self.get()
                self.add_token(TokenEnum.INTEGER, sentence)
            elif state == 3:
                sentence = char
                char = self.get()
                
                while char != "\"":
                    sentence += char
                    char = self.get()

                sentence += self.get()
                self.add_token(TokenEnum.TEXT, sentence)

            if char == ",":
                self.add_token(TokenEnum.COMMA, char)
            elif char == ";":
                self.add_token(TokenEnum.SEMICOLON, char)
            elif char == ":":
                self.add_token(TokenEnum.COLON, char)
            elif char == "=":
                self.add_token(TokenEnum.ASSIGNMENT, char)
            elif char == "+" or char == "-" or char == "*" or char == "/":
                self.add_token(TokenEnum.ARITHMETIC, char)

        return self.tokens

    
