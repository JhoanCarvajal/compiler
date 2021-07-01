import os
import codecs
import sly
from lexer import Lexer
from graph import *


class Parser(sly.Parser):
    # debugfile = 'parser.out'
    tokens = Lexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('left', '(', ')'),
        # ('right', '^'),
    )
    #program
    @_('lines')
    def program(sefl, p):
        p = Program('program', p.lines)
        return p

    # lines
    @_('INTEGER statements newline lines')
    def lines(self, p):
        # print("lines: statement : INTEGER statements newline lines")
        p = NoTerminal(Terminal(p.INTEGER), p.statements, p.newline, p.lines, name='lines1')
        return p

    @_('INTEGER statements newline')
    def lines(self, p):
        # print("lines: INTEGER statements newline")
        p = NoTerminal(Terminal(p.INTEGER), p.statements, p.newline, name='lines2')
        return p
    
    # statements
    @_('statement ":" statements')
    def statements(self, p):
        # print("statements: statement : statements")
        p = NoTerminal(p.statement, p.statements, name='statements1')
        return p

    @_('statement')
    def statements(self, p):
        # print("statements: statement")
        p = NoTerminal(p.statement, name='statements2')
        return p

    # statement
    @_('CLOSE "#" INTEGER')
    def statement(self, p):
        # print('statement: CLOSE "#" INTEGER')
        p = NoTerminal(Terminal(p.INTEGER), name='statement1')
        return p

    @_('DATA constant_list')
    def statement(self, p):
        # print("statement: DATA constant_list")
        p = NoTerminal(p.constant_list, name='statement2')
        return p
    
    @_('DIM ID "(" integer_list ")"')
    def statement(self, p):
        # print("statement: DIM ID ( integer_ list )")
        p = NoTerminal(Terminal(p.ID), Terminal(p[2]), p.integer_list, Terminal(p[2]), name='statement3')
        return p
    
    @_('END')
    def statement(self, p):
        # print("statement: END")
        p = NoTerminal(name='statement4')
        return p

    @_('FOR ID ASSIGN expression TO expression')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression")
        p = NoTerminal(Terminal(p.ID), Terminal(p[2]), p.expression0, p.expression1, name='statement5')
        return p

    @_('FOR ID ASSIGN expression TO expression STEP INTEGER')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression STEP INTEGER")
        p = NoTerminal(Terminal(p.ID), Terminal(p[2]), p.expression0, p.expression1, Terminal(p.INTEGER), name='statement6')
        return p

    @_('GOTO expression')
    def statement(self, p):
        # print("statement: GOTO expression")
        p = NoTerminal(p.expression, name='statement7')
        return p

    @_('GOSUB expression')
    def statement(self, p):
        # print("statement: GOSUB expression")
        p = NoTerminal(p.expression, name='statement8')
        return p

    @_('IF expression THEN statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement")
        p = NoTerminal(p.expression, p.statement, name='statement9')
        return p

    @_('IF expression THEN statement ELSE statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement ELSE statement")
        p = NoTerminal(p.expression, p.statement0, p.statement1, name='statement10')
        return p

    @_('INPUT id_list')
    def statement(self, p):
        # print("statement: INPUT id_list")
        p = NoTerminal(p.id_list, name='statement11')
        return p

    @_('INPUT "#" INTEGER "," id_list')
    def statement(self, p):
        # print('statement: INPUT "#" INTEGER "," id_list')
        p = NoTerminal(Terminal(p.INTEGER), p.id_list, name='statement12')
        return p

    @_('LET ID ASSIGN expression')
    def statement(self, p):
        # print("statement: LET ID ASSIGN expression")
        p = NoTerminal(Terminal(p.ID), Terminal(p[2]), p.expression, name='statement13')
        return p

    @_('NEXT id_list')
    def statement(self, p):
        # print("statement: NEXT id_list")
        p = NoTerminal(p.id_list, name='statement14')
        return p

    @_('OPEN value FOR access AS "#" INTEGER')
    def statement(self, p):
        # print('statement: OPEN value FOR access AS "#" INTEGER')
        p = NoTerminal(p.value, p.access, Terminal(p.INTEGER), name='statement15')
        return p

    @_('POKE value_list')
    def statement(self, p):
        # print('statement: POKE value_list')
        p = NoTerminal(p.value_list, name='statement16')
        return p

    @_('PRINT print_list')
    def statement(self, p):
        # print('statement: PRINT print_list')
        p = NoTerminal(p.print_list, name='statement17')
        return p

    @_('PRINT "#" INTEGER "," print_list')
    def statement(self, p):
        # print('statement: PRINT "#" INTEGER "," print_list')
        p = NoTerminal(Terminal(p.INTEGER), p.print_list, name='statement18')
        return p

    @_('READ id_list')
    def statement(self, p):
        # print('statement: READ id_list')
        p = NoTerminal(p.id_list, name='statement19')
        return p

    @_('RETURN')
    def statement(self, p):
        # print('statement: RETURN')
        p = NoTerminal(name='statement20')
        return p

    @_('RESTORE')
    def statement(self, p):
        # print('statement: RESTORE')
        p = NoTerminal(name='statement21')
        return p

    @_('RUN')
    def statement(self, p):
        # print('statement: RUN')
        p = NoTerminal(name='statement22')
        return p

    @_('STOP')
    def statement(self, p):
        # print('statement: STOP')
        p = NoTerminal(name='statement23')
        return p

    @_('SYS value')
    def statement(self, p):
        # print('statement: SYS value')
        p = NoTerminal(p.value, name='statement24')
        return p

    @_('WAIT value_list')
    def statement(self, p):
        # print('statement: WAIT value_list')
        p = NoTerminal(p.value_list, name='statement25')
        return p

    @_('REM')
    def statement(self, p):
        # print('statement: Remark')
        p = NoTerminal(name='statement26')
        return p

    # access
    @_('INPUT')
    def access(self, p):
        # print('access: INPUT')
        p = NoTerminal(name='access1')
        return p

    @_('OUPUT')
    def access(self, p):
        # print('access: OUPUT')
        p = NoTerminal(name='access2')
        return p

    # id_list
    @_('ID "," id_list')
    def id_list(self, p):
        # print('id_list: ID "," id_list')
        p = NoTerminal(Terminal(p.ID), p.id_list, name='id_list1')
        return p

    @_('ID')
    def id_list(self, p):
        # print('id_list: ID')
        p = NoTerminal(Terminal(p.ID), name='id_list2')
        return p

    # value_list
    @_('value "," value_list')
    def value_list(self, p):
        # print('value_list: value "," value_list')
        p = NoTerminal(p.value, p.value_list, name='value_list1')
        return p

    @_('value')
    def value_list(self, p):
        # print('value_list: value')
        p = NoTerminal(p.value, name='value_list2')
        return p

    # constant_list
    @_('constant "," constant_list')
    def constant_list(self, p):
        # print('constant_list: constant "," constant_list')
        p = NoTerminal(p.constant, Terminal(p[1]), p.constant_list, name='constant_list1')
        return p

    @_('constant')
    def constant_list(self, p):
        # print('constant_list: constant')
        p = NoTerminal(p.constant, name='constant_list2')
        return p

    # integer_list
    @_('INTEGER "," integer_list')
    def integer_list(self, p):
        # print('integer_list: INTEGER "," integer_list')
        p = NoTerminal(Terminal(p.INTEGER), Terminal(p[1]), p.integer_list, name='integer_list1')
        return p

    @_('INTEGER')
    def integer_list(self, p):
        # print('integer_list: INTEGER')
        p = NoTerminal(Terminal(p.INTEGER), name='integer_list2')
        return p

    # expression_list
    @_('expression "," expression_list')
    def expression_list(self, p):
        # print('expression_list: expression "," expression_list')
        p = NoTerminal(p.expression, Terminal(p[1]), p.expression_list, name='expression_list1')
        return p

    @_('expression')
    def expression_list(self, p):
        # print('expression_list: expression')
        p = NoTerminal(p.expression, name='expression_list2')
        return p

    # print_list
    @_('expression ";" print_list')
    def print_list(self, p):
        # print('print_list: expression ";" print_list')
        p = NoTerminal(p.expression, Terminal(p[1]), p.print_list, name='Print_list1')
        return p

    @_('expression')
    def print_list(self, p):
        # print('print_list: expression')
        p = NoTerminal(p.expression, name='Print_list2')
        return p

    # expression
    @_('and_exp OR expression')
    def expression(self, p):
        # print('expression: and_exp OR expression')
        p = NoTerminal(p.and_exp, Terminal(p[1]), p.expression, name='Expression1')
        return p

    @_('and_exp')
    def expression(self, p):
        # print('expression: and_exp')
        p = NoTerminal(p.and_exp, name='Expression2')
        return p

    # and_exp
    @_('not_exp AND and_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp AND and_exp')
        p = NoTerminal(p.not_exp, Terminal(p[1]), p.and_exp, name='And_exp1')
        return p

    @_('not_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp')
        p = NoTerminal(p.not_exp, name='And_exp2')
        return p

    # not_exp
    @_('NOT compare_exp')
    def not_exp(self, p):
        # print('not_exp: NOT compare_exp')
        p = NoTerminal(Terminal(p[0]), p.compare_exp, name='Not_exp1')
        return p

    @_('compare_exp')
    def not_exp(self, p):
        # print('not_exp: compare_exp')
        p = NoTerminal(p.compare_exp, name='Not_exp2')
        return p

    # compare_exp
    @_('add_exp ASSIGN compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp ASSIGN compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp1')
        return p
    
    @_('add_exp NE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp NE compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp2')
        return p
    
    @_('add_exp EQ compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp EQ compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp3')
        return p
    
    @_('add_exp GT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GT compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp4')
        return p
    
    @_('add_exp GE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GE compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp5')
        return p
    
    @_('add_exp LT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LT compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp6')
        return p
    
    @_('add_exp LE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LE compare_exp')
        p = NoTerminal(p.add_exp, Terminal(p[1]), p.compare_exp, name='Compare_exp7')
        return p
    
    @_('add_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp')
        p = NoTerminal(p.add_exp, name='Compare_exp8')
        return p
    
    # add_exp
    @_('mult_exp "+" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "+" add_exp')
        p = NoTerminal(p.mult_exp, Terminal(p[1]), p.add_exp, name='Add_exp1')
        return p
    
    @_('mult_exp "-" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "-" add_exp')
        p = NoTerminal(p.mult_exp, Terminal(p[1]), p.add_exp, name='Add_exp2')
        return p
    
    @_('mult_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp')
        p = NoTerminal(p.mult_exp, name='Add_exp3')
        return p
    
    # mult_exp
    @_('negate_exp "*" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "*" mult_exp')
        p = NoTerminal(p.negate_exp, Terminal(p[1]), p.mult_exp, name='Mult_exp1')
        return p
    
    @_('negate_exp "/" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "/" mult_exp')
        p = NoTerminal(p.negate_exp, Terminal(p[1]), p.mult_exp, name='Mult_exp2')
        return p
    
    @_('negate_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp')
        p = NoTerminal(p.negate_exp, name='Mult_exp3')
        return p

    # negate_exp
    @_('"-" power_exp')
    def negate_exp(self, p):
        # print('negate_exp: "-" power_exp')
        p = NoTerminal(p.power_exp, name='Negate_exp1')
        return p

    @_('power_exp')
    def negate_exp(self, p):
        # print('negate_exp: power_exp')
        p = NoTerminal(p.power_exp, name='Negate_exp2')
        return p
    
    # power_exp
    @_('power_exp "^" value')
    def power_exp(self, p):
        # print('power_exp: power_exp "^" value')
        p = NoTerminal(Terminal(p[1]), p.power_exp, p.value, name='Power_exp1')
        return p

    @_('value')
    def power_exp(self, p):
        # print('power_exp: value')
        p = NoTerminal(p.value, name='Power_exp2')
        return p

    # value
    @_('"(" expression ")"')
    def value(self, p):
        # print('value: "(" expression ")"')
        p = NoTerminal(Terminal(p[0]), p.expression, Terminal(p[2]), name='Value1')
        return p

    @_('ID')
    def value(self, p):
        # print('value: ID')
        p = NoTerminal(Terminal(p.ID), name='Value2')
        return p

    @_('ID "(" expression_list ")"')
    def value(self, p):
        # print('value: ID "(" expression_list ")"')
        p = NoTerminal(Terminal(p.ID), Terminal(p[1]), p.expression_list, Terminal(p[3]), name='Value3')
        return p

    @_('constant')
    def value(self, p):
        # print('value: constant')
        p = NoTerminal(p.constant, name='Value4')
        return p

    # constant
    @_('INTEGER')
    def constant(self, p):
        # print('constant: INTEGER')
        p = NoTerminal(Terminal(p.INTEGER), name='Constant1')
        return p

    @_('STRING')
    def constant(self, p):
        # print('constant: STRING')
        p = NoTerminal(String(p.STRING), name='Constant2')
        return p

    # @_('REAL')
    # def constant(self, p):
    #     print('constant: REAL')
    
    # newline
    @_('CR LF')
    def newline(self, p):
        # print('newline: CR LF')
        p = NoTerminal(name='Newline1')
        return p

    @_('CR')
    def newline(self, p):
        # print('newline: CR')
        p = NoTerminal(name='Newline2')
        return p

    # @_('LF')
    # def newline(self, p):
    #     print('newline: LF')

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print("Has escogido \"%s\"" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

if __name__ == '__main__':
    from graphviz import render
    lexer = Lexer()
    parser = Parser()
    env = {}
    def translate(result):
        graphFile = open('graph.gv','w')
        graphFile.write(result.translate())
        graphFile.close()
        print("El programa traducido")

    directorio = 'C:\\Users\\Jhoan\\Documents\\personal\\universidad\\compiler\\test\\'
    archivo = buscarFicheros(directorio)
    test = directorio+archivo
    fp = codecs.open(test,"r","utf-8")
    data = fp.read()
    fp.close()

    result = parser.parse(lexer.tokenize(data))
    translate(result)

    render('dot', 'png', 'graph.gv')

    os.system(f"C:\\Users\\Jhoan\\Documents\\personal\\universidad\\compiler\\graph.gv.png")

