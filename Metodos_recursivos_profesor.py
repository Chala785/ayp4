class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazadaRecursiva:
    def __init__(self):
        self.cabeza = None

    # =============================
    # MÉTODO ITERATIVO
    # =============================
    def agregar(self, dato):
        nuevo = Nodo(dato)

        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # =============================
    # MÉTODOS RECURSIVOS
    # =============================

    # ---- LONGITUD ----
    def longitud(self):
        return self._longitud_rec(self.cabeza)

    def _longitud_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._longitud_rec(nodo.siguiente)

    # ---- SUMA ----
    def suma(self):
        return self._suma_rec(self.cabeza)

    def _suma_rec(self, nodo):
        if nodo is None:
            return 0
        return nodo.dato + self._suma_rec(nodo.siguiente)

    # ---- BUSCAR ----
    def buscar(self, dato):
        return self._buscar_rec(dato, self.cabeza)

    def _buscar_rec(self, dato, nodo):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        return self._buscar_rec(dato, nodo.siguiente)

    # ---- IMPRIMIR ----
    def imprimir(self):
        self._imprimir_rec(self.cabeza)

    def _imprimir_rec(self, nodo):
        if nodo is None:
            print("None")
            return
        print(f"{nodo.dato} -> ", end="")
        self._imprimir_rec(nodo.siguiente)


# =============================
# EJEMPLO DE USO
# =============================
if __name__ == "__main__":
    lista = ListaEnlazadaRecursiva()

    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)

    print("Lista enlazada:")
    lista.imprimir()

    print("Longitud:", lista.longitud())
    print("Suma:", lista.suma())
    print("Buscar 20:", lista.buscar(20))
    print("Buscar 40:", lista.buscar(40))