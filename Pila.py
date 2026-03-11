# Crear nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Crear pila
class Pila:
    def __init__(self):
        self.tope = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamaño += 1

    def pop(self):
        if self.esta_vacia():
            return None
        
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamaño -= 1
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato


# Prueba
pila = Pila()

pila.push(10)
pila.push(20)
pila.push(30)

print("Tope:", pila.peek())   # 30
print("Pop:", pila.pop())     # 30
print("Tope:", pila.peek())   # 20

        