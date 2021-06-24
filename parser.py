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
    # lines
    @_('INTEGER statements newline lines')
    def lines(self, p):
        # print("lines: statement : INTEGER statements newline lines")
        p[0] = Lines1('lines1', p[1], p[2], p[3], p[4])

    @_('INTEGER statements newline')
    def lines(self, p):
        # print("lines: INTEGER statements newline")
        p[0] = Lines2('lines2', p[1], p[2], p[3])
    
    # statements
    @_('statement ":" statements')
    def statements(self, p):
        # print("statements: statement : statements")
        p[0] = Statements1('statements1', p[1], p[3])

    @_('statement')
    def statements(self, p):
        # print("statements: statement")
        p[0] = Statements2('statements2', p[1])

    # statement
    @_('CLOSE "#" INTEGER')
    def statement(self, p):
        # print('statement: CLOSE "#" INTEGER')
        p[0] = Statement1('statement1', p[3])

    @_('DATA constant_list')
    def statement(self, p):
        # print("statement: DATA constant_list")
        p[0] = Statement2('statement2', p[2])
    
    @_('DIM ID "(" integer_list ")"')
    def statement(self, p):
        # print("statement: DIM ID ( integer_ list )")
        p[0] = Statement3('statement3', Id(p[2]), p[4])
    
    @_('END')
    def statement(self, p):
        # print("statement: END")
        p[0] = Statement4('statement4')

    @_('FOR ID ASSIGN expression TO expression')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression")
        p[0] = Statement5('statement5', Id(p[2]), p[4], p[6])

    @_('FOR ID ASSIGN expression TO expression STEP INTEGER')
    def statement(self, p):
        # print("statement: FOR ID ASSIGN expression TO expression STEP INTEGER")
        p[0] = Statement6('statement6', Id(p[2]), p[4], p[6], p[8])

    @_('GOTO expression')
    def statement(self, p):
        # print("statement: GOTO expression")
        p[0] = Statement7('statement7', p[2])

    @_('GOSUB expression')
    def statement(self, p):
        # print("statement: GOSUB expression")
        p[0] = Statement8('statement8', p[2])

    @_('IF expression THEN statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement")
        p[0] = Statement9('statement9', p[2], p[4])

    @_('IF expression THEN statement ELSE statement')
    def statement(self, p):
        # print("statement: IF expression THEN statement ELSE statement")
        p[0] = Statement10('statement10', p[2], p[4], p[6])

    @_('INPUT id_list')
    def statement(self, p):
        # print("statement: INPUT id_list")
        p[0] = Statement11('statement11', p[2])

    @_('INPUT "#" INTEGER "," id_list')
    def statement(self, p):
        # print('statement: INPUT "#" INTEGER "," id_list')
        p[0] = Statement12('statement12', Integer(p[3]), p[5])

    @_('LET ID ASSIGN expression')
    def statement(self, p):
        # print("statement: LET ID ASSIGN expression")
        p[0] = Statement13('statement13', Id(p[2]), p[4])

    @_('NEXT id_list')
    def statement(self, p):
        # print("statement: NEXT id_list")
        p[0] = Statement14('statement14', p[2])

    @_('OPEN value FOR access AS "#" INTEGER')
    def statement(self, p):
        # print('statement: OPEN value FOR access AS "#" INTEGER')
        p[0] = Statement15('statement15', p[2], p[4], p[7])

    @_('POKE value_list')
    def statement(self, p):
        # print('statement: POKE value_list')
        p[0] = Statement16('statement16', p[2])

    @_('PRINT print_list')
    def statement(self, p):
        # print('statement: PRINT print_list')
        p[0] = Statement17('statement17', p[2])

    @_('PRINT "#" INTEGER "," print_list')
    def statement(self, p):
        # print('statement: PRINT "#" INTEGER "," print_list')
        p[0] = Statement18('statement18', Integer(p[3]), p[5])

    @_('READ id_list')
    def statement(self, p):
        # print('statement: READ id_list')
        p[0] = Statement19('statement19', p[2])

    @_('RETURN')
    def statement(self, p):
        # print('statement: RETURN')
        p[0] = Statement20('statement20')

    @_('RESTORE')
    def statement(self, p):
        # print('statement: RESTORE')
        p[0] = Statement21('statement21')

    @_('RUN')
    def statement(self, p):
        # print('statement: RUN')
        p[0] = Statement22('statement22')

    @_('STOP')
    def statement(self, p):
        # print('statement: STOP')
        p[0] = Statement23('statement23')

    @_('SYS value')
    def statement(self, p):
        # print('statement: SYS value')
        p[0] = Statement24('statement24', p[2])

    @_('WAIT value_list')
    def statement(self, p):
        # print('statement: WAIT value_list')
        p[0] = Statement25('statement25', p[2])

    @_('REM')
    def statement(self, p):
        # print('statement: Remark')
        p[0] = Statement26('statement26')

    # access
    @_('INPUT')
    def access(self, p):
        # print('access: INPUT')
        p[0] = Access1('access1')

    @_('OUPUT')
    def access(self, p):
        # print('access: OUPUT')
        p[0] = Access2('access2')

    # id_list
    @_('ID "," id_list')
    def id_list(self, p):
        # print('id_list: ID "," id_list')
        p[0] = Id_list1('id_list1', Id(p[1]), p[3])

    @_('ID')
    def id_list(self, p):
        # print('id_list: ID')
        p[0] = Id_list2('id_list2', Id(p[1]))

    # value_list
    @_('value "," value_list')
    def value_list(self, p):
        # print('value_list: value "," value_list')
        p[0] = Value_list1('value_list1', p[1], p[3])

    @_('value')
    def value_list(self, p):
        # print('value_list: value')
        p[0] = Value_list2('value_list2', p[1])

    # constant_list
    @_('constant "," constant_list')
    def constant_list(self, p):
        # print('constant_list: constant "," constant_list')
        return ('constant_list_constant_constant_list', p.constant, p.constant_list)

    @_('constant')
    def constant_list(self, p):
        # print('constant_list: constant')
        return ('constant_list_constant', p.constant)

    # integer_list
    @_('INTEGER "," integer_list')
    def integer_list(self, p):
        # print('integer_list: INTEGER "," integer_list')
        return ('integer_list_integer_integer_list', p.INTEGER, p.integer_list)

    @_('INTEGER')
    def integer_list(self, p):
        # print('integer_list: INTEGER')
        return ('integer_list_integer', p.INTEGER)

    # expression_list
    @_('expression "," expression_list')
    def expression_list(self, p):
        # print('expression_list: expression "," expression_list')
        return ('expression_list_expression_expression_list', p.expression, p.expression_list)

    @_('expression')
    def expression_list(self, p):
        # print('expression_list: expression')
        return ('expression_list', p.expression)

    # print_list
    @_('expression ";" print_list')
    def print_list(self, p):
        # print('print_list: expression ";" print_list')
        return ('print_list_expression_print_list', p.expression, p.print_list)

    @_('expression')
    def print_list(self, p):
        # print('print_list: expression')
        return ('print_list_expression', p.expression)

    # expression
    @_('and_exp OR expression')
    def expression(self, p):
        # print('expression: and_exp OR expression')
        return ('expression_and_exp_or_expression', p.and_exp, p.expression)

    @_('and_exp')
    def expression(self, p):
        # print('expression: and_exp')
        return ('expression_and_exp', p.and_exp)

    # and_exp
    @_('not_exp AND and_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp AND and_exp')
        return ('and_exp_not_exp_and_and_exp', p.not_exp, p.and_exp)

    @_('not_exp')
    def and_exp(self, p):
        # print('and_exp: not_exp')
        return ('and_exp_not_exp', p.not_exp)

    # not_exp
    @_('NOT compare_exp')
    def not_exp(self, p):
        # print('not_exp: NOT compare_exp')
        return ('not_exp_not_compare_exp', p.compare_exp)

    @_('compare_exp')
    def not_exp(self, p):
        # print('not_exp: compare_exp')
        return ('not_exp_compare_exp', p.compare_exp)

    # compare_exp
    @_('add_exp ASSIGN compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp ASSIGN compare_exp')
        return ('compare_exp_add_exp_assign_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp NE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp NE compare_exp')
        return ('compare_exp_add_exp_ne_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp EQ compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp EQ compare_exp')
        return ('compare_exp_add_exp_eq_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp GT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GT compare_exp')
        return ('compare_exp_add_exp_gt_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp GE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp GE compare_exp')
        return ('compare_exp_add_exp_ge_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp LT compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LT compare_exp')
        return ('compare_exp_add_exp_lt_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp LE compare_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp LE compare_exp')
        return ('compare_exp_add_exp_le_compare_exp', p.add_exp, p.compare_exp)
    
    @_('add_exp')
    def compare_exp(self, p):
        # print('compare_exp: add_exp')
        return ('compare_exp_add_exp', p.add_exp)
    
    # add_exp
    @_('mult_exp "+" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "+" add_exp')
        return ('add_exp_mult_exp_plus_add_exp', p.mult_exp, p.add_exp)
    
    @_('mult_exp "-" add_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp "-" add_exp')
        return ('add_exp_mult_exp_minus_add_exp', p.mult_exp, p.add_exp)
    
    @_('mult_exp')
    def add_exp(self, p):
        # print('add_exp: mult_exp')
        return ('add_exp_mult_exp', p.mult_exp)
    
    # mult_exp
    @_('negate_exp "*" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "*" mult_exp')
        return ('mult_exp_negate_exp_mult_mult_exp', p.negate_exp, p.mult_exp)
    
    @_('negate_exp "/" mult_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp "/" mult_exp')
        return ('mult_exp_negate_exp_div_mult_exp', p.negate_exp, p.mult_exp)
    
    @_('negate_exp')
    def mult_exp(self, p):
        # print('mult_exp: negate_exp')
        return ('mult_exp_negate_exp', p.negate_exp)

    # negate_exp
    @_('"-" power_exp')
    def negate_exp(self, p):
        # print('negate_exp: "-" power_exp')
        return ('negate_exp_menos_power_exp', p.power_exp)

    @_('power_exp')
    def negate_exp(self, p):
        # print('negate_exp: power_exp')
        return ('negate_exp_power_exp', p.power_exp)
    
    # power_exp
    @_('power_exp "^" value')
    def power_exp(self, p):
        # print('power_exp: power_exp "^" value')
        return ('power_exp_value', p.power_exp, p.value)

    @_('value')
    def power_exp(self, p):
        # print('power_exp: value')
        return ('value', p.value)

    # value
    @_('"(" expression ")"')
    def value(self, p):
        # print('value: "(" expression ")"')
        return ('value_expression', p.expression)

    @_('ID')
    def value(self, p):
        # print('value: ID')
        return ('value_id', p.ID)

    @_('ID "(" expression_list ")"')
    def value(self, p):
        # print('value: ID "(" expression_list ")"')
        return ('value_id_expression_list', p.ID, p.expression_list)

    @_('constant')
    def value(self, p):
        # print('value: constant')
        return ('value_constant', p.constant)

    # constant
    @_('INTEGER')
    def constant(self, p):
        # print('constant: INTEGER')
        return ('integer', p.INTEGER)

    @_('STRING')
    def constant(self, p):
        # print('constant: STRING')
        return ('string', p.STRING)

    # @_('REAL')
    # def constant(self, p):
    #     print('constant: REAL')
    
    # newline
    @_('CR LF')
    def newline(self, p):
        # print('newline: CR LF')
        return ('newline_cr_lf', p.CR, p.LF)

    @_('CR')
    def newline(self, p):
        # print('newline: CR')
        return ('newline_cr', p.CR)

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

    # directorio = 'C:\\Users\\Jhoan\\Documents\\personal\\universidad\\compiler\\test\\'
    # archivo = buscarFicheros(directorio)
    # test = directorio+archivo
    # fp = codecs.open(test,"r","utf-8")
    # data = fp.read()
    # fp.close()

    # result = parser.parse(lexer.tokenize(data))

    # print(result)
    while True:
        try:
            text = input('basic > ')
        except EOFError:
            break
        if text == "exit()":
            break
        else:
            text = text + " \r"
            print(text)
            tree = parser.parse(lexer.tokenize(text))
            print(tree)