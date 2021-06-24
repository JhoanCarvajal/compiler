txt = ""
count = 0
def increment_count():
    global count
    count += 1
    return(str(count))

class Nodo():
    pass

class Lines1(Nodo):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
    
    # def imprimir(self, ident):
    #     self.son1.imprimir(" "+ident)
    #     self.son2.imprimir(" "+ident)
    #     self.son3.imprimir(" "+ident)
    #     self.son4.imprimir(" "+ident)
    #     print(ident + "Nodo: "+self.name)

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        return id

class Lines2(Nodo):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

# statements
class Statements1(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Statements2(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

# statement
class Statement1(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement2(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement3(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class Statement4(Nodo):
    def __init__(self, name):
        self.name = name
        self.name = name

    def translate(self):
        global txt
        id = increment_count()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class Statement5(Nodo):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class Statement6(Nodo):
    def __init__(self, name, son1,son2,son3,son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        return id

class Statement7(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement8(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement9(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Statement10(Nodo):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class Statement11(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement12(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Statement13(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Statement14(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement15(Nodo):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class Statement16(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement17(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement18(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Statement19(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement20(Nodo):
	def __init__(self,name):
		self.name = name
			
	def translate(self):
		global txt
		id = increment_count()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		return id

class Statement21(Nodo):
	def __init__(self,name):
		self.name = name
			
	def translate(self):
		global txt
		id = increment_count()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		return id
        
class Statement22(Nodo):
	def __init__(self,name):
		self.name = name
			
	def translate(self):
		global txt
		id = increment_count()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		return id

class Statement23(Nodo):
	def __init__(self,name):
		self.name = name
			
	def translate(self):
		global txt
		id = increment_count()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		return id

class Statement24(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement25(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Statement26(Nodo):
    def __init__(self, name):
        self.name = name

    def translate(self):
        global txt
        id = increment_count()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

# access
class Access1(Nodo):
    def __init__(self, name):
        self.name = name

    def translate(self):
        global txt
        id = increment_count()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class Access2(Nodo):
    def __init__(self, name):
        self.name = name

    def translate(self):
        global txt
        id = increment_count()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

# id_list
class Id_list1(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Id_list2(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

# value_list
class Value_list1(Nodo):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class Value_list2(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

# constant_list
class Constant_list1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Constant_list2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# integer_list
class Integer_list1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Integer_list2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# expression_list
class Expression_list1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Expression_list2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# print_list
class Print_list1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Print_list2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# expression
class Expression1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Expression2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# and_exp
class And_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class And_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# not_exp
class Not_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Not_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# compare_exp
class Compare_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp3(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp4(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp5(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp6(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp7(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Compare_exp8(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# add_exp
class Add_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

class Add_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

class Add_exp3(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# mult_exp
class Mult_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

class Mult_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

class Mult_exp3(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# negate_exp
class Negate_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Negate_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# power_exp
class Power_exp1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Power_exp2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# value
class Value1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Value2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Value3(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Value4(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# constant
class Constant1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
class Constant2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

# newline
class Newline1(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

class Newline2(Nodo):
    def __init__(self, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global txt
        id = increment_count()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

class Id(Nodo):
	def __init__(self,name):
		self.name = name
			
	def translate(self):
		global txt
		id = increment_count()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		return id

class Integer(Nodo):
	def __init__(self,name):
		self.name = name
			
	def translate(self):
		global txt
		id = increment_count()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		return id