txt = ""
count = 0

def increment_count():
    global count
    count += 1
    return count


class Nodo():
    pass


class Program(Nodo):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global txt
        id = increment_count()
        son1 = self.son1.translate()
        txt += str(id) + '[label= "'+str(self.name)+'"]'+'\n\t'
        txt += str(id) + ' -> ' + str(son1) + "\n\t"
        return "digraph {\n\t"+txt+"}"


class NoTerminal(Nodo):
    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.sons = []
        for arg in args:
            son = arg
            self.sons.append(son)
    def translate(self):
        global txt
        id = increment_count()
        sons_translate = []
        for son in self.sons:
            son_translate = son.translate()
            sons_translate.append(son_translate)
        txt += str(id) + '[label= "'+str(self.name)+'"]'+'\n\t'
        for son in sons_translate:
            txt += str(id) + ' -> ' + str(son) + "\n\t"
        return id


class Terminal(Nodo):
    def __init__(self, name):
        self.name = name
        # self.translate()

    def translate(self):
        global txt
        id = increment_count()
        txt += str(id) + '[label= "'+str(self.name)+'"]'+'\n\t'
        return id


class String(Nodo):
    def __init__(self, name):
        self.name = name
        # self.translate()

    def translate(self):
        global txt
        id = increment_count()
        txt += str(id) + '[label= '+str(self.name)+']'+'\n\t'
        return id