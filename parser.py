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
        p = Lines1('lines1', Terminal(p.INTEGER), p.statements, p.newline, p.lines)
        return p

    @_('INTEGER statements newline')
    def lines(self, p):
        # print("lines: INTEGER statements newline")
        p = Lines2('lines2', Terminal(p.INTEGER), p.statements, p.newline)
        return p
    
    # statements
    @_('statement ":" statements')
    def statements(self, p):
        # print("statements: statement : statements")
        p = Statements1('statements1', p.statement, p.statements)
        return p

    @_('statement')
    def statements(self, p):
        # print("statements: statement")
        p = Statements2('statements2', p.statement)
        return p

    # statement
    @_('CLOSE "#" INTEGER')
    def statement(self, p):
        # print('statement: CLOSE "#" INTEGER')
        p = Statement1('statement1', Terminal(p.INTEGER))
        return p

    @_('DATA constant_list')
    def statement(self, p):
        # print("statement: DATA constant_list")
        p = Statement2('statement2', p.constant_list)
        return p
    
    @_('DIM ID "(" integer_list ")"')
    def statement(self, p):
        # print("statement: DIM ID ( integer_ list )")
        p = Statement3('statement3', Terminal(p.ID), Terminal(p[2]), p.integer_list, Terminal(p[2]))
        return p
    
    @_('END')
    def statement(self, p):
        # print("statement: END")
        p = Statement4('statement4')
        return p

    @_('FOR ID ASSIGN expression TO expression')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression")
        p = Statement5('statement5', Terminal(p.ID), Terminal(p[2]), p.expression0, p.expression1)
        return p

    @_('FOR ID ASSIGN expression TO expression STEP INTEGER')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression STEP INTEGER")
        p = Statement6('statement6', Terminal(p.ID), Terminal(p[2]), p.expression0, p.expression1, Terminal(p.INTEGER))
        return p

    @_('GOTO expression')
    def statement(self, p):
        # print("statement: GOTO expression")
        p = Statement7('statement7', p.expression)
        return p

    @_('GOSUB expression')
    def statement(self, p):
        # print("statement: GOSUB expression")
        p = Statement8('statement8', p.expression)
        return p

    @_('IF expression THEN statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement")
        p = Statement9('statement9', p.expression, p.statement)
        return p

    @_('IF expression THEN statement ELSE statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement ELSE statement")
        p = Statement10('statement10', p.expression, p.statement0, p.statement1)
        return p

    @_('INPUT id_list')
    def statement(self, p):
        # print("statement: INPUT id_list")
        p = Statement11('statement11', p.id_list)
        return p

    @_('INPUT "#" INTEGER "," id_list')
    def statement(self, p):
        # print('statement: INPUT "#" INTEGER "," id_list')
        p = Statement12('statement12', Terminal(p.INTEGER), p.id_list)
        return p

    @_('LET ID ASSIGN expression')
    def statement(self, p):
        # print("statement: LET ID ASSIGN expression")
        p = Statement13('statement13', Terminal(p.ID), Terminal(p[2]), p.expression)
        return p

    @_('NEXT id_list')
    def statement(self, p):
        # print("statement: NEXT id_list")
        p = Statement14('statement14', p.id_list)
        return p

    @_('OPEN value FOR access AS "#" INTEGER')
    def statement(self, p):
        # print('statement: OPEN value FOR access AS "#" INTEGER')
        p = Statement15('statement15', p.value, p.access, Terminal(p.INTEGER))
        return p

    @_('POKE value_list')
    def statement(self, p):
        # print('statement: POKE value_list')
        p = Statement16('statement16', p.value_list)
        return p

    @_('PRINT print_list')
    def statement(self, p):
        # print('statement: PRINT print_list')
        p = Statement17('statement17', p.print_list)
        return p

    @_('PRINT "#" INTEGER "," print_list')
    def statement(self, p):
        # print('statement: PRINT "#" INTEGER "," print_list')
        p = Statement18('statement18', Terminal(p.INTEGER), p.print_list)
        return p

    @_('READ id_list')
    def statement(self, p):
        # print('statement: READ id_list')
        p = Statement19('statement19', p.id_list)
        return p

    @_('RETURN')
    def statement(self, p):
        # print('statement: RETURN')
        p = Statement20('statement20')
        return p

    @_('RESTORE')
    def statement(self, p):
        # print('statement: RESTORE')
        p = Statement21('statement21')
        return p

    @_('RUN')
    def statement(self, p):
        # print('statement: RUN')
        p = Statement22('statement22')
        return p

    @_('STOP')
    def statement(self, p):
        # print('statement: STOP')
        p = Statement23('statement23')
        return p

    @_('SYS value')
    def statement(self, p):
        # print('statement: SYS value')
        p = Statement24('statement24', p.value)
        return p

    @_('WAIT value_list')
    def statement(self, p):
        # print('statement: WAIT value_list')
        p = Statement25('statement25', p.value_list)
        return p

    @_('REM')
    def statement(self, p):
        # print('statement: Remark')
        p = Statement26('statement26')
        return p

    # access
    @_('INPUT')
    def access(self, p):
        # print('access: INPUT')
        p = Access1('access1')
        return p

    @_('OUPUT')
    def access(self, p):
        # print('access: OUPUT')
        p = Access2('access2')
        return p

    # id_list
    @_('ID "," id_list')
    def id_list(self, p):
        # print('id_list: ID "," id_list')
        p = Id_list1('id_list1', Terminal(p.ID), p.id_list)
        return p

    @_('ID')
    def id_list(self, p):
        # print('id_list: ID')
        p = Id_list2('id_list2', Terminal(p.ID))
        return p

    # value_list
    @_('value "," value_list')
    def value_list(self, p):
        # print('value_list: value "," value_list')
        p = Value_list1('value_list1', p.value, p.value_list)
        return p

    @_('value')
    def value_list(self, p):
        # print('value_list: value')
        p = Value_list2('value_list2', p.value)
        return p

    # constant_list
    @_('constant "," constant_list')
    def constant_list(self, p):
        # print('constant_list: constant "," constant_list')
        p = Constant_list1('constant_list1', p.constant, Terminal(p[1]), p.constant_list)
        return p

    @_('constant')
    def constant_list(self, p):
        # print('constant_list: constant')
        p = Constant_list2('constant_list2', p.constant)
        return p

    # integer_list
    @_('INTEGER "," integer_list')
    def integer_list(self, p):
        # print('integer_list: INTEGER "," integer_list')
        p = Integer_list1('integer_list1', Terminal(p.INTEGER), Terminal(p[1]), p.integer_list)
        return p

    @_('INTEGER')
    def integer_list(self, p):
        # print('integer_list: INTEGER')
        p = Integer_list2('integer_list2', Terminal(p.INTEGER))
        return p

    # expression_list
    @_('expression "," expression_list')
    def expression_list(self, p):
        # print('expression_list: expression "," expression_list')
        p = Expression_list1('expression_list1', p.expression, Terminal(p[1]), p.expression_list)
        return p

    @_('expression')
    def expression_list(self, p):
        # print('expression_list: expression')
        p = Expression_list2('expression_list2', p.expression)
        return p

    # print_list
    @_('expression ";" print_list')
    def print_list(self, p):
        # print('print_list: expression ";" print_list')
        p = Print_list1('Print_list1', p.expression, Terminal(p[1]), p.print_list)
        return p

    @_('expression')
    def print_list(self, p):
        # print('print_list: expression')
        p = Print_list2('Print_list2', p.expression)
        return p

    # expression
    @_('and_exp OR expression')
    def expression(self, p):
        # print('expression: and_exp OR expression')
        p = Expression1('Expression1', p.and_exp, Terminal(p[1]), p.expression)
        return p

    @_('and_exp')
    def expression(self, p):
        # print('expression: and_exp')
        p = Expression2('Expression2', p.and_exp)
        return p

    # and_exp
    @_('not_exp AND and_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp AND and_exp')
        p = And_exp1('And_exp1', p.not_exp, Terminal(p[1]), p.and_exp)
        return p

    @_('not_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp')
        p = And_exp2('And_exp2', p.not_exp)
        return p

    # not_exp
    @_('NOT compare_exp')
    def not_exp(self, p):
        # print('not_exp: NOT compare_exp')
        p = Not_exp1('Not_exp1', Terminal(p[0]), p.compare_exp)
        return p

    @_('compare_exp')
    def not_exp(self, p):
        # print('not_exp: compare_exp')
        p = Not_exp2('Not_exp2', p.compare_exp)
        return p

    # compare_exp
    @_('add_exp ASSIGN compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp ASSIGN compare_exp')
        p = Compare_exp1('Compare_exp1', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp NE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp NE compare_exp')
        p = Compare_exp2('Compare_exp2', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp EQ compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp EQ compare_exp')
        p = Compare_exp3('Compare_exp3', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp GT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GT compare_exp')
        p = Compare_exp4('Compare_exp4', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp GE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GE compare_exp')
        p = Compare_exp5('Compare_exp5', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp LT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LT compare_exp')
        p = Compare_exp6('Compare_exp6', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp LE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LE compare_exp')
        p = Compare_exp7('Compare_exp7', p.add_exp, Terminal(p[1]), p.compare_exp)
        return p
    
    @_('add_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp')
        p = Compare_exp8('Compare_exp8', p.add_exp)
        return p
    
    # add_exp
    @_('mult_exp "+" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "+" add_exp')
        p = Add_exp1('Add_exp1', p.mult_exp, Terminal(p[1]), p.add_exp)
        return p
    
    @_('mult_exp "-" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "-" add_exp')
        p = Add_exp2('Add_exp2', p.mult_exp, Terminal(p[1]), p.add_exp)
        return p
    
    @_('mult_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp')
        p = Add_exp3('Add_exp3', p.mult_exp)
        return p
    
    # mult_exp
    @_('negate_exp "*" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "*" mult_exp')
        p = Mult_exp1('Mult_exp1', p.negate_exp, Terminal(p[1]), p.mult_exp)
        return p
    
    @_('negate_exp "/" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "/" mult_exp')
        p = Mult_exp2('Mult_exp2', p.negate_exp, Terminal(p[1]), p.mult_exp)
        return p
    
    @_('negate_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp')
        p = Mult_exp3('Mult_exp3', p.negate_exp)
        return p

    # negate_exp
    @_('"-" power_exp')
    def negate_exp(self, p):
        # print('negate_exp: "-" power_exp')
        p = Negate_exp1('Negate_exp1', p.power_exp)
        return p

    @_('power_exp')
    def negate_exp(self, p):
        # print('negate_exp: power_exp')
        p = Negate_exp2('Negate_exp2', p.power_exp)
        return p
    
    # power_exp
    @_('power_exp "^" value')
    def power_exp(self, p):
        # print('power_exp: power_exp "^" value')
        p = Power_exp1('Power_exp1', Terminal(p[1]), p.power_exp, p.value)
        return p

    @_('value')
    def power_exp(self, p):
        # print('power_exp: value')
        p = Power_exp2('Power_exp2', p.value)
        return p

    # value
    @_('"(" expression ")"')
    def value(self, p):
        # print('value: "(" expression ")"')
        p = Value1('Value1', Terminal(p[0]), p.expression, Terminal(p[2]))
        return p

    @_('ID')
    def value(self, p):
        # print('value: ID')
        p = Value2('Value2', Terminal(p.ID))
        return p

    @_('ID "(" expression_list ")"')
    def value(self, p):
        # print('value: ID "(" expression_list ")"')
        p = Value3('Value3', Terminal(p.ID), Terminal(p[1]), p.expression_list, Terminal(p[3]))
        return p

    @_('constant')
    def value(self, p):
        # print('value: constant')
        p = Value4('Value4', p.constant)
        return p

    # constant
    @_('INTEGER')
    def constant(self, p):
        # print('constant: INTEGER')
        p = Constant1('Constant1', Terminal(p.INTEGER))
        return p

    @_('STRING')
    def constant(self, p):
        # print('constant: STRING')
        p = Constant2('Constant2', String(p.STRING))
        return p

    # @_('REAL')
    # def constant(self, p):
    #     print('constant: REAL')
    
    # newline
    @_('CR LF')
    def newline(self, p):
        # print('newline: CR LF')
        p = Newline1('Newline1')
        return p

    @_('CR')
    def newline(self, p):
        # print('newline: CR')
        p = Newline2('Newline2')
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

