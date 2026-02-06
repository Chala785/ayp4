class Nodo:
    def __init__(self, Documento, Nombre):
        self.documento = Documento
        self.nombre = Nombre
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

def append(self, Documento, Nombre):
    new_node = Nodo(Documento, Nombre)
    if  self.cabeza == None:
        self.cabeza = new_node
        return
    else:
        actual = self.cabeza
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = new_node

def AgegarAlFinal(self, Documento, Nombre):
    new_node = Nodo(Documento, Nombre)

    if self.cabeza == None:
        self.cabeza = Nodo
        self.cola = Nodo
    else:
        self.cola.siguiente = Nodo
        self.cola = Nodo 



    
