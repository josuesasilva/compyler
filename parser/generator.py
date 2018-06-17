import sys
from scanner.token import Token, TokenEnum
from re import match

'''
Grammar:

<Portugol> := PROGRAMA <identiﬁcadores> ; VARIAVEIS <declaracoes> INICIO <instrucoes> FIM
<declaracoes> := <declaracao> <declaracoes> | <declaracao>
<declaracao> := <tipo> : <identiﬁcadores> ;
<tipo> := INTEIRO | REAL
<identiﬁcadores> := <identiﬁcador>, <identiﬁcadores> | <identiﬁcador>
<instrucoes> := <instrucao> <instrucoes> | <instrucao>
<instrucao> := <atribuicao> | <instrucao_leitura> | <instrucao_escrita>
<atribuicao> := <identiﬁcador> = <expressao>;
<instrucao_leitura> := LEIA <identiﬁcador>;
<instrucao_escrita> := IMPRIMA (<texto> | <expressao>);
<expressao> := <expressao> <operador> <expressao> | <identiﬁcador> | <inteiro> | <real>
<operador> := + | - | * | /
<identiﬁcador> := <letra> (<letra> | <digito>)∗
<inteiro> := [-](<digito>)+
<real> := [-](<digito>)+.(<digito>)+
<texto> := “(<letra>)∗”
<digito> := 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<letra> := A|B|...|Z|a|b|...|z
'''

class Generator:

    '''
    Instruction set

    [+, a, b, c] #Plus
    [-, a, b, c] #Minus
    [*, a, b, c] #Times
    [/, a, b, c] #Division
    [=, a, b, -] #Atribution
    [r, a, -, -] #Read
    [w, a, -, -] #Write
    '''
    def __init__(self, tokens, ast):
        self.tokens = tokens
        self.ast = ast

    def start(self):
        if "INICIO" in self.ast:
            self.statements = self.ast[1:self.ast.index("INICIO")]
            self.ast = self.ast[self.ast.index("INICIO") + 1:len(self.ast)]
            instructions = []

            last_index = 0
            for index, value in enumerate(self.ast):
                if value == ";":
                    instructions.append(self.ast[last_index:index])
                    last_index = index + 1

            for inst in instructions:
                if len(inst) > 1 and inst[0] == inst[1]:
                    inst.pop(0)

            print(instructions)
            print(self.statements)

            for inst in instructions:
                if inst[0] == "IMPRIMA":
                    self.generate_write(inst)
                elif inst[0] == "LEIA":
                    self.generate_read(inst)
                else:
                    self.generate_attribution(inst)

        else:
            print("Missing main identifier")
            sys.exit(1)

    def generate_read(self, instruction):
        
        if len(instruction) == 2:

            if not self.has_statment(instruction[1]):
                sys.exit(1)

            print("[r, {}, -, -]".format(instruction[1]))
        else:
            self.generate_multi("t0", instruction[1:len(instruction)])

    def generate_write(self, instruction):

        if len(instruction) == 2:

            if not self.has_statment(instruction[1]):
                sys.exit(1)

            print("[w, {}, -, -]".format(instruction[1]))
        else:
            self.generate_multi("t0", instruction[1:len(instruction)])

    def generate_attribution(self, instruction):
        
        if not self.has_statment(instruction[0]):
            sys.exit(1)

        if len(instruction) == 3:
            
            if not self.has_statment(instruction[2]):
                sys.exit(1)

            print("[=, {}, {}, -]".format(instruction[0], instruction[1]))
        else:
            self.generate_multi(instruction[0], instruction[instruction.index("=") + 1:len(instruction)])
    
    def generate_multi(self, id, instruction):
        
        if len(instruction) < 3:
            print("Invalid statement")
            sys.exit()
        # 1, +, 2, *, 4
        print("[{}, {}, {}, {}]".format(instruction[1], instruction[0], instruction[2], id))

        instruction = instruction[3:len(instruction)]
        
        while len(instruction) > 0:
            print("[{}, {}, {}, {}]".format(instruction[0], instruction[1], id, id))
            instruction = instruction[2:len(instruction)]

    def has_statment(self, id):
        if id.startswith("\"") and id.endswith("\"") or match("(\d+(?:\.\d+)?)", id):
            return True
        
        if id in self.statements:
            return True

        print("Missing statement {}".format(id))
        return False
