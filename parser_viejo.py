import os
import codecs
import sly
from lexer import Lexer
from analizador_semantico import *


class Parser(sly.Parser):
    debugfile = 'parser.out'
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
        return ('program', p.lines)
    # lines
    @_('INTEGER statements newline lines')
    def lines(self, p):
        # print("lines: statement : INTEGER statements newline lines")
        return ('lines1', p.INTEGER, p.statements, p.newline, p.lines)

    @_('INTEGER statements newline')
    def lines(self, p):
        # print("lines: INTEGER statements newline")
        return ('lines2', p.INTEGER, p.statements, p.newline)
    
    # statements
    @_('statement ":" statements')
    def statements(self, p):
        # print("statements: statement : statements")
        return ('statements1', p.statement, p.statements)

    @_('statement')
    def statements(self, p):
        # print("statements: statement")
        return ('statements2', p.statement)

    # statement
    @_('CLOSE "#" INTEGER')
    def statement(self, p):
        # print('statement: CLOSE "#" INTEGER')
        return ('statement1', p.INTEGER)

    @_('DATA constant_list')
    def statement(self, p):
        # print("statement: DATA constant_list")
        return ('statement2', p.constant_list)
    
    @_('DIM ID "(" integer_list ")"')
    def statement(self, p):
        # print("statement: DIM ID ( integer_ list )")
        return ('statement3', p.ID, p.integer_list)
    
    @_('END')
    def statement(self, p):
        # print("statement: END")
        return ('statement4')

    @_('FOR ID ASSIGN expression TO expression')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression")
        return ('statement5', p.ID, p.expression0, p.expression1)

    @_('FOR ID ASSIGN expression TO expression STEP INTEGER')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression STEP INTEGER")
        return ('statement6', p.ID, p.expression0, p.expression1, p.INTEGER)

    @_('GOTO expression')
    def statement(self, p):
        # print("statement: GOTO expression")
        return ('statement7', p.expression)

    @_('GOSUB expression')
    def statement(self, p):
        # print("statement: GOSUB expression")
        return ('statement8', p.expression)

    @_('IF expression THEN statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement")
        return ('statement9', p.expression, p.statement)

    @_('IF expression THEN statement ELSE statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement ELSE statement")
        return ('statement10', p.expression, p.statement0, p.statement1)

    @_('INPUT id_list')
    def statement(self, p):
        # print("statement: INPUT id_list")
        return ('statement11', p.id_list)

    @_('INPUT "#" INTEGER "," id_list')
    def statement(self, p):
        # print('statement: INPUT "#" INTEGER "," id_list')
        return ('statement12', p.INTEGER, p.id_list)

    @_('LET ID ASSIGN expression')
    def statement(self, p):
        # print("statement: LET ID ASSIGN expression")
        return ('statement13', p.ID, p.expression)

    @_('NEXT id_list')
    def statement(self, p):
        # print("statement: NEXT id_list")
        return ('statement14', p.id_list)

    @_('OPEN value FOR access AS "#" INTEGER')
    def statement(self, p):
        # print('statement: OPEN value FOR access AS "#" INTEGER')
        return ('statement15', p.value, p.access, p.INTEGER)

    @_('POKE value_list')
    def statement(self, p):
        # print('statement: POKE value_list')
        return ('statement16', p.value_list)

    @_('PRINT print_list')
    def statement(self, p):
        # print('statement: PRINT print_list')
        return ('statement17', p.print_list)

    @_('PRINT "#" INTEGER "," print_list')
    def statement(self, p):
        # print('statement: PRINT "#" INTEGER "," print_list')
        return ('statement18', p.INTEGER, p.print_list)

    @_('READ id_list')
    def statement(self, p):
        # print('statement: READ id_list')
        return ('statement19', p.id_list)

    @_('RETURN')
    def statement(self, p):
        # print('statement: RETURN')
        return ('statement20')

    @_('RESTORE')
    def statement(self, p):
        # print('statement: RESTORE')
        return ('statement21')

    @_('RUN')
    def statement(self, p):
        # print('statement: RUN')
        return ('statement22')

    @_('STOP')
    def statement(self, p):
        # print('statement: STOP')
        return ('statement23')

    @_('SYS value')
    def statement(self, p):
        # print('statement: SYS value')
        return ('statement24', p.value)

    @_('WAIT value_list')
    def statement(self, p):
        # print('statement: WAIT value_list')
        return ('statement25', p.value_list)

    @_('REM')
    def statement(self, p):
        # print('statement: Remark')
        return ('statement26')

    # access
    @_('INPUT')
    def access(self, p):
        # print('access: INPUT')
        return ('access1')

    @_('OUPUT')
    def access(self, p):
        # print('access: OUPUT')
        return ('access2')

    # id_list
    @_('ID "," id_list')
    def id_list(self, p):
        # print('id_list: ID "," id_list')
        return ('id_list1', p.ID, p.id_list)

    @_('ID')
    def id_list(self, p):
        # print('id_list: ID')
        return ('id_list2', p.ID)

    # value_list
    @_('value "," value_list')
    def value_list(self, p):
        # print('value_list: value "," value_list')
        return ('value_list1', p.value, p.value_list)

    @_('value')
    def value_list(self, p):
        # print('value_list: value')
        return ('value_list2', p.value)

    # constant_list
    @_('constant "," constant_list')
    def constant_list(self, p):
        # print('constant_list: constant "," constant_list')
        return ('constant_list1', p.constant, p.constant_list)

    @_('constant')
    def constant_list(self, p):
        # print('constant_list: constant')
        return ('constant_list2', p.constant)

    # integer_list
    @_('INTEGER "," integer_list')
    def integer_list(self, p):
        # print('integer_list: INTEGER "," integer_list')
        return ('integer_list1', p.INTEGER, p.integer_list)

    @_('INTEGER')
    def integer_list(self, p):
        # print('integer_list: INTEGER')
        return ('integer_list2', p.INTEGER)

    # expression_list
    @_('expression "," expression_list')
    def expression_list(self, p):
        # print('expression_list: expression "," expression_list')
        return ('expression_list1', p.expression, p.expression_list)

    @_('expression')
    def expression_list(self, p):
        # print('expression_list: expression')
        return ('expression_list2', p.expression)

    # print_list
    @_('expression ";" print_list')
    def print_list(self, p):
        # print('print_list: expression ";" print_list')
        return ('Print_list1', p.expression, p.print_list)

    @_('expression')
    def print_list(self, p):
        # print('print_list: expression')
        return ('Print_list2', p.expression)

    # expression
    @_('and_exp OR expression')
    def expression(self, p):
        # print('expression: and_exp OR expression')
        return ('Expression1', p.and_exp, p[1], p.expression)

    @_('and_exp')
    def expression(self, p):
        # print('expression: and_exp')
        return ('Expression2', p.and_exp)

    # and_exp
    @_('not_exp AND and_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp AND and_exp')
        return ('And_exp1', p.not_exp, p[1], p.and_exp)

    @_('not_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp')
        return ('And_exp2', p.not_exp)

    # not_exp
    @_('NOT compare_exp')
    def not_exp(self, p):
        # print('not_exp: NOT compare_exp')
        return ('Not_exp1', p.compare_exp)

    @_('compare_exp')
    def not_exp(self, p):
        # print('not_exp: compare_exp')
        return ('Not_exp2', p.compare_exp)

    # compare_exp
    @_('add_exp ASSIGN compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp ASSIGN compare_exp')
        return ('Compare_exp1', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp NE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp NE compare_exp')
        return ('Compare_exp2', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp EQ compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp EQ compare_exp')
        return ('Compare_exp3', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp GT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GT compare_exp')
        return ('Compare_exp4', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp GE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GE compare_exp')
        return ('Compare_exp5', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp LT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LT compare_exp')
        return ('Compare_exp6', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp LE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LE compare_exp')
        return ('Compare_exp7', p.add_exp, p[1], p.compare_exp)
    
    @_('add_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp')
        return ('Compare_exp8', p.add_exp)
    
    # add_exp
    @_('mult_exp "+" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "+" add_exp')
        return ('Add_exp1', p.mult_exp, p[1], p.add_exp)
    
    @_('mult_exp "-" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "-" add_exp')
        return ('Add_exp2', p.mult_exp, p[1], p.add_exp)
    
    @_('mult_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp')
        return ('Add_exp3', p.mult_exp)
    
    # mult_exp
    @_('negate_exp "*" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "*" mult_exp')
        return ('Mult_exp1', p.negate_exp, p[1], p.mult_exp)
    
    @_('negate_exp "/" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "/" mult_exp')
        return ('Mult_exp2', p.negate_exp, p[1], p.mult_exp)
    
    @_('negate_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp')
        return ('Mult_exp3', p.negate_exp)

    # negate_exp
    @_('"-" power_exp')
    def negate_exp(self, p):
        # print('negate_exp: "-" power_exp')
        return ('Negate_exp1', p.power_exp)

    @_('power_exp')
    def negate_exp(self, p):
        # print('negate_exp: power_exp')
        return ('Negate_exp2', p.power_exp)
    
    # power_exp
    @_('power_exp "^" value')
    def power_exp(self, p):
        # print('power_exp: power_exp "^" value')
        return ('Power_exp1', p.power_exp, p[1], p.value)

    @_('value')
    def power_exp(self, p):
        # print('power_exp: value')
        return ('Power_exp2', p.value)

    # value
    @_('"(" expression ")"')
    def value(self, p):
        # print('value: "(" expression ")"')
        return ('Value1', p.expression)

    @_('ID')
    def value(self, p):
        # print('value: ID')
        return ('Value2', p.ID)

    @_('ID "(" expression_list ")"')
    def value(self, p):
        # print('value: ID "(" expression_list ")"')
        return ('Value3', p.ID, p.expression_list)

    @_('constant')
    def value(self, p):
        # print('value: constant')
        return ('Value4', p.constant)

    # constant
    @_('INTEGER')
    def constant(self, p):
        # print('constant: INTEGER')
        return ('Constant1', p.INTEGER)

    @_('STRING')
    def constant(self, p):
        # print('constant: STRING')
        return ('Constant2', p.STRING)

    # @_('REAL')
    # def constant(self, p):
    #     print('constant: REAL')
    
    # newline
    @_('CR LF')
    def newline(self, p):
        # print('newline: CR LF')
        return ('Newline1', p.CR, p.LF)

    @_('CR')
    def newline(self, p):
        # print('newline: CR')
        return ('Newline1', p.CR)

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
    lexer = Lexer()
    parser = Parser()
    env = {}
    # archivo = "C:\\Users\\Jhoan\\Documents\\personal\\universidad\\compiler\\test2.txt"
    # fp = codecs.open(archivo, "r", "utf-8")
    # data = fp.read()
    # fp.close()
    
    # for tree in parser.parse(lexer.tokenize(data)):
    #     print(tree)
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
    print(result)
    # translate(result)

    # while True:
    #     try:
    #         text = input('basic > ')
    #     except EOFError:
    #         break
    #     if text == "exit()":
    #         break
    #     else:
    #         text = text + " \r"
    #         print(text)
    #         tree = parser.parse(lexer.tokenize(text))
    #         print(tree)