from scanner.token import Token, TokenEnum

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
    
    def get(self):
        return self.stream.read(1)

    def is_eof(self):
        return self.peek() == ''

    def add_token(self, token, value):
        if not token in self.tokens.keys():
            self.tokens[token] = []
        self.tokens[token].append(value)

    def scan(self):
        while not self.is_eof():
            char = self.get()
            state = -1
            
            if char == " " or char == "\t" or char == "\n":
                continue

            if char.isnumeric():
                state = 0
            elif char.isalpha():
                state = 1
            elif char == "-":
                state = 2

            if state == 0:
                sentence = ""
                while char.isnumeric():
                    sentence += char
                    char = self.get()
                self.add_token(TokenEnum.INTEGER, sentence)
            elif state == 1:
                sentence = ""
                while char.isalpha() or char.isnumeric():
                    sentence += char
                    char = self.get()
                if sentence == "INTEIRO":
                    self.add_token(TokenEnum.TYPE, sentence)
                elif sentence == "LER" or sentence == "IMPRIMIR":
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

            if char == ",":
                self.add_token(TokenEnum.COMMA, char)
            elif char == ";":
                self.add_token(TokenEnum.SEMICOLON, char)
            elif char == ":":
                self.add_token(TokenEnum.COLON, char)
            elif char == "=":
                self.add_token(TokenEnum.ASSIGNMENT, char)

        return self.tokens

    
