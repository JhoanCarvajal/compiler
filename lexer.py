import sly
import codecs

class Lexer(sly.Lexer):
    
    tokens = {
        ASSIGN, EQ, LT, LE, GT, GE, NE,
        ID, INTEGER, STRING, LET, READ, DATA, PRINT, GOTO, IF, THEN, ELSE, FOR, NEXT, TO, STEP, END,
        STOP, GOSUB, DIM, RETURN, RUN, INPUT, OR, AND, NOT, AS,
        OPEN, CLOSE, POKE, RESTORE, SYS, WAIT, OUPUT, CR, LF, REM
    }

    literals = { '+','-','*','/','(', ')', ',', ';', '#', ':', '^' }
    
    ignore = ' \t'
    
    EQ = r'=='
    ASSIGN = r'='
    NE = r'<>'
    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'

    STRING = r'\".*?\"'
    CR = r'\r+'
    LF = r'\n+'
    REM = r'REM.[^\r]*'

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*\$?')
    def ID(self, t):
        if t.value.upper() in self.tokens:
            t.value = t.value.upper()
            t.type = t.value
        return t

    
    @_("\d+")
    def INTEGER(self, t):
        t.value = int(t.value)
        return t
    
    # @_("[\d.+]")
    # def REAL(self, t):
    #     t.value = float(t.value)
    #     return t
    
    # @_("\n+")
    # def ignore_newline(self, t):
    #     self.lineno += t.value.count('\n')
    
    def error(self, t):
        print(f"{t.lineno} - Caracter ilegal '{t.value[0]}'")
        self.index += 1

if __name__ == '__main__':
    lexer = Lexer()
    env = {}
    archivo = "C:\\Users\\Jhoan\\Documents\\personal\\universidad\\compiler\\test\\test2.txt"
    fp = codecs.open(archivo, "r", "utf-8")
    data = fp.read()
    fp.close()
    
    for tok in lexer.tokenize(data):
        print(tok)