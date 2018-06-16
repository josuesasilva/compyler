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