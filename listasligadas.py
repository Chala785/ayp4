class NodoDoble:
    """Nodo para lista doblemente enlazada."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    """Lista doblemente enlazada."""

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        """Verifica si la lista está vacía"""
        return self.cabeza is None

    def insertar_inicio(self, dato):
        """Inserta un elemento al inicio de la lista"""
        nuevo = NodoDoble(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, dato):
        """Inserta un elemento al final de la lista"""
        nuevo = NodoDoble(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar_inicio(self):
        """Elimina el primer elemento de la lista"""
        if self.esta_vacia():
            return None

        dato = self.cabeza.dato

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        return dato

    def eliminar_final(self):
        """Elimina el último elemento de la lista"""
        if self.esta_vacia():
            return None

        dato = self.cola.dato

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

        return dato

    def recorrer_adelante(self):
        """Imprime la lista de inicio a fin"""
        if self.esta_vacia():
            print("Lista vacía")
            return

        print("Inicio -> Fin:", end=" ")
        actual = self.cabeza
        elementos = []

        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        print(" <-> ".join(elementos))

    def recorrer_atras(self):
        """Imprime la lista de fin a inicio"""
        if self.esta_vacia():
            print("Lista vacía")
            return

        print("Fin -> Inicio:", end=" ")
        actual = self.cola
        elementos = []

        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior

        print(" <-> ".join(elementos))

    def buscar(self, dato):
        """Busca un elemento en la lista"""
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

    def __len__(self):
        """Retorna la cantidad de elementos en la lista"""
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador

    def __str__(self):
        """Retorna una representación en cadena de la lista"""
        if self.esta_vacia():
            return "Lista vacía"

        elementos = []
        actual = self.cabeza

        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        return " <-> ".join(elementos)


# ================= PRUEBAS =================
if __name__ == "__main__":
    lista = ListaDoble()

    # Insertar elementos
    print("Insertando al final: 10, 20, 30")
    lista.insertar_final(10)
    lista.insertar_final(20)
    lista.insertar_final(30)
    print("Lista:", lista)

    print("\nInsertar al inicio: 5")
    lista.insertar_inicio(5)
    print("Lista:", lista)

    # Recorridos
    print("\n=== RECORRIDOS ===")
    lista.recorrer_adelante()
    lista.recorrer_atras()

    # Eliminaciones
    print("\n=== ELIMINACIONES ===")
    eliminado = lista.eliminar_inicio()
    print(f"Eliminado del inicio: {eliminado}")
    print("Lista:", lista)

    eliminado = lista.eliminar_final()
    print(f"Eliminado del final: {eliminado}")
    print("Lista:", lista)

    # Búsqueda
    print("\n=== BÚSQUEDA ===")
    print(f"¿Existe 20? {lista.buscar(20)}")
    print(f"¿Existe 100? {lista.buscar(100)}")

    # Longitud
    print(f"\nLongitud de la lista: {len(lista)}")
