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

class Portugol:

    '''
    <Portugol> := PROGRAMA <identiﬁcadores> ; VARIAVEIS <declaracoes> INICIO <instrucoes> FIM
    ''' 
    def __init__(self):
        self.identifiers = None
        self.statements = None
        self.instructions = None


class Statements(Portugol):

    '''
    <declaracoes> := <declaracao> <declaracoes> | <declaracao>
    '''
    pass


class StatementR(Statements):

    '''
    <declaracoes> := <declaracao> <declaracoes> | <declaracao>
    '''
    def __init__(self):
        self.statements = None
        self.statment = None


class Statement(Statements):

    '''
    <declaracao> := <tipo> : <identiﬁcadores>
    '''
    def __init__(self):
        self.vartype = None
        self.identifiers = None


class Identifiers(Statement):

    '''
    <identificadores>   := <identificador> <identificador_r>
    '''
    def __init__(self):
        self.identifier = None
        self.identifier_r = None


class IdentifierR(Identifiers):

    '''
    <identificador_r>   := ,<identificador> <identificador_r> | lambda
    '''
    def __init__(self):
        self.identifier = None
        self.identifiers = None


class Identifier(Identifiers):

    '''
    <identiﬁcador> := <letra> (<letra> | <digito>)∗
    '''
    def __init__(self):
        self.value = None


class Instructions(Portugol):
    
    '''
    <instrucoes> := <instrucao> <instrucoes> | <instrucao>
    '''
    def __init__(self):
        self.instruction = None
        self.instructions = None


class Instruction(Instructions):
    
    '''
    <instrucao> := <atribuicao> | <instrucao_leitura> | <instrucao_escrita>
    '''
    def __init__(self):
        self.assign = None
        self.write = None
        self.read = None


class Assign(Instruction):
    
    '''
    <atribuicao> := <identiﬁcador> = <expressao>;
    '''
    def __init__(self):
        self.identifier = None
        self.expression = None


class Read(Instruction):
    
    '''
    <instrucao_leitura> := LEIA <identiﬁcador>;
    '''
    def __init__(self):
        self.identifier = None


class Write(Instruction):

    '''
    <instrucao_escrita> := IMPRIMA (<texto> | <expressao>);
    '''    
    def __init__(self):
        self.value = None


class Expressions:
        
    '''
    <expressao> := <expressao> <operador> <expressao> | <identiﬁcador> | <inteiro> | <real>
    '''
    pass

class Expression(Expressions):
        
    '''
    <expressao> := <expressao> <operador> <expressao> | <identiﬁcador> | <inteiro> | <real>
    '''
    def __init__(self):
        self.expression = None


class ExpressionR(Expressions):
        
    '''
    <expressao> := <expressao> <operador> <expressao> | <identiﬁcador> | <inteiro> | <real>
    '''
    def __init__(self):
        self.expression = None
        self.expressions = None


class Type(Statement):

    '''
    <tipo> := INTEIRO | REAL
    '''
    def __init__(self):
        self.value = None

class Integer:
        
    def __init__(self, value):
        self.value = value


class Real:
        
    def __init__(self, value):
        self.value = value


class Text:
        
    def __init__(self, value):
        self.value = value

