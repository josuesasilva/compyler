import re
from scanner.scanner import Scanner
from scanner.token import Token, TokenEnum
from parser.ast import *

class LL1(object):
    
    def __init__(self, tokens):
        self.ast = None
        self.tokens = tokens
        self.tokens.append(Token(TokenEnum.EOF, "$"))
        self.index = 0
        self.keywords = ["PROGRAMA", "INTEIRO", "INICIO", "FIM", "VARIAVEIS", "REAL", "IMPRIMA", "LEIA"]

    def get_token(self):
        return self.tokens[self.index].value

    def get_token_type(self):
        return self.tokens[self.index].token

    def update_index(self):
        print(self.get_token())
        self.index += 1
    
    def parse(self):
        if self.portugol() and self.get_token_type() == TokenEnum.EOF:
            print("Done.\nSuccess!")
            return 0
        else:
            print("Done.\nError.")
            return 1

    def portugol(self):
        portugol = Portugol()

        if self.get_token() == "PROGRAMA":
            
            self.update_index()
            portugol.identifiers = Identifiers()

            if self.identifiers(portugol.identifiers):
             
                if self.get_token() == ";":
                    self.update_index()
                else:
                    print("Error: missing ; at", self.index)
                    return False
                    
            else:
                print("Error: invalid identifier at", self.index)
                return False    

        else:
            print("Error: missing statement PRROGRAMA at", self.index)
            return False

        if self.get_token() == "VARIAVEIS":
            
            self.update_index()
            portugol.statements = Statements()

            if not self.statements(portugol.statements):
                print("Error: invalid statement at", self.index)
                return False

        else:
            print("Error: statement VARIAVEIS at", self.index)
            return False

        if self.get_token() == "INICIO":
            
            self.update_index()
            portugol.instructions = Instructions()

            if self.instructions(portugol.instructions):
               
                if self.get_token() == "FIM":
                    self.update_index()
                    return True
                else:
                    print("Error: missing statement FIM at", self.index)
                    return False

            else:
                print("Error: invalid instruction at", self.index)
                return False 

        else:
            print("Error: missing or invalid instructions at", self.index)
            return False
    
    def statements(self, statements):
        stat_r = StatementR()
        stat_r.statement = Statement()

        if self.statement(stat_r.statement):

            if self.statement_r(stat_r.statements):
                statements = stat_r
                return True

            return True

        stat = Statement()

        if self.statement(stat):
            statements = stat
            return True

        return False

    def statement_r(self, statements):
        stat_r = StatementR()
        stat_r.statement = Statement()

        if self.statement(stat_r.statement):
            if self.statement_r(stat_r.statements):
                statements = stat_r
                return True

        stat = Statement()

        if self.statement(stat):
            statements = stat
            return True

        return False

    def statement(self, statement):
        if self.check_type():
            statement.vartype = self.get_token()
            self.update_index()

            if self.get_token() == ":":
                self.update_index()

                if self.identifiers(statement.identifiers):
                    if self.get_token() == ";":
                        self.update_index()
                        return True
                    else:
                        print("Error: expect \";\" at", self.index)    
                        return False
                else:
                    print("Error: invalid identifier at", self.index)
                    return False
            else:
                print("Error: expect \":\" at", self.index)
                return False

        return False 

    def vartype(self):
        token = self.get_token()
        if token == 'INTEIRO':
            return True
        elif token == 'REAL':
            return True

    def identifiers(self, identifiers):
        ident_r = IdentifierR()
        ident_r.identifier = Identifier()

        if self.identifier(ident_r.identifier):
            
            if self.identifier_r(ident_r.identifiers):
                identifiers = ident_r
                return True
            
            return True

        ident = Identifier()

        if self.identifier(ident):
            identifiers = ident
            return True

        return False

    def identifier(self, identifier):
        if self.get_token_type() == TokenEnum.IDENTIFIER and self.get_token not in self.keywords:
            identifier.value = self.get_token()
            self.update_index()
            return True

        return False

    def identifier_r(self, identifiers):

        if self.get_token() == ",":
            self.update_index()

            ident_r = IdentifierR()
            ident_r.identifier = Identifier()

            if self.identifier(ident_r.identifier):
                if self.identifier_r(ident_r.identifiers):
                    identifiers = ident_r
                    return True

        if self.get_token() == ",":
            self.update_index()

            ident = Identifier()

            if self.identifier(ident):
                identifiers = ident
                return True
        
        return False

    def instructions(self, instructions):
        inst_r = InstructionR()
        inst_r.instruction = Instruction()

        if self.instruction(inst_r.instruction):

            if self.instruction_r(inst_r.instructions):
                instructions = inst_r
                return True
                    
        inst = Instruction()

        if self.instruction(inst):
            instructions = inst
            return True

        return False

    def instruction_r(self, instructions):
        inst_r = InstructionR()
        inst_r.instruction = Instruction()

        if self.instruction(inst_r.instruction):

            if self.instruction_r(inst_r.instructions):
                instructions = inst_r
                return True
            
            return True
        
        inst = Instruction()

        if self.instruction(inst):
            instructions = inst
            return True

        return False

    def instruction(self, instruction):
        if self.get_token() == "IMPRIMA":
            return self.write()
        elif self.get_token() == "LEIA":
            return self.read()
        elif self.assign(instruction):
            return True

        return False

    def assign(self, instruction):
        instruction.identifier = Identifier()

        if not self.identifier(instruction.identifier):
            return False

        if self.get_token() == "=":
            self.update_index()
        else:
            return False
        
        instruction.expression = Expression()

        if not self.expressions():
            return False

        if self.get_token() == ";":
            self.update_index()
            return True
        else:
            return False

    def read(self):
        self.update_index()

        identifiers = Identifiers()

        if self.identifiers(identifiers):
            
            if self.get_token() == ";":
                self.update_index()
                return True
            else:
                return False

        else:
            return False

    def write(self):
        self.update_index()

        if self.expressions():

            if self.get_token() == ";":
                self.update_index()
                return True

        elif self.word():
            self.update_index()
            
            if self.get_token() == ";":
                self.update_index()
                return True
        
        return False

    def expression(self):
        if self.number():
            self.update_index()
            return True
        
        ident = Identifier()

        if self.identifier(ident):
            return True

        return False
    
    def expressions(self):

        if self.expression():

            if self.expression_r():
                return True

            return True

        if self.expression():
            return True

        return False

    def expression_r(self):

        if self.opcode():
            self.update_index()

            if self.expression():
                if self.expression_r():
                    return True

        if self.opcode():
            self.update_index()

            if self.expression():
                return True

        return False
    
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

    def check_type(self):
        token = self.get_token()
        if token == "INTEIRO":
            return True
        elif token == "REAL":
            return True
        else:
            return False

    def number(self):
        return self.get_token_type() == TokenEnum.INTEGER or self.get_token_type() == TokenEnum.FLOAT

    def word(self):
        return self.get_token_type() == TokenEnum.TEXT

    