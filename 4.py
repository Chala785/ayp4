"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN D
                    Sistema de Inventario de Productos
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Una tienda necesita un sistema para gestionar su inventario de productos.
Los productos se organizan por categoría y se debe poder consultar stock,
calcular valores y gestionar el inventario.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Producto) con los atributos necesarios
2. Diseñar la clase Lista (Inventario) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos
6. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Producto):
   - Debe almacenar: nombre, categoría, precio, cantidad en stock
   - Debe poder enlazarse con otro producto

b) Clase LISTA (Inventario):
   - Mantener los productos ordenados alfabéticamente por nombre


PUNTO 2 (1.0): AGREGAR PRODUCTO - RECURSIVO
-------------------------------------------
Implementa un método para agregar un producto.
- Debe mantener el orden alfabético por nombre
- Si el producto ya existe, solo actualizar la cantidad
- OBLIGATORIO usar recursividad


PUNTO 3 (1.0): VALOR TOTAL DEL INVENTARIO - RECURSIVO
-----------------------------------------------------
Implementa un método que calcule el valor total del inventario.
- Valor = suma de (precio × cantidad) de cada producto
- OBLIGATORIO usar recursividad


PUNTO 4 (1.0): PRODUCTOS CON BAJO STOCK - RECURSIVO
---------------------------------------------------
Implementa un método que retorne una NUEVA lista con productos
cuyo stock sea menor a un valor dado.
- OBLIGATORIO usar recursividad
- No modificar la lista original


PUNTO 5 (1.0): ELIMINAR PRODUCTO - RECURSIVO
--------------------------------------------
Implementa un método que elimine un producto por su nombre.
- OBLIGATORIO usar recursividad
- Retorna True si se eliminó, False si no existía

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Producto)

class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.siguiente = None


# PUNTO 1b: Clase Lista (Inventario)

class Inventario:

    def __init__(self):
        self.cabeza = None


    # Mostrar inventario
    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("Inventario vacío")
            return

        while actual:
            print(f"{actual.nombre} | {actual.categoria} | ${actual.precio} | Stock: {actual.cantidad}")
            actual = actual.siguiente


    # PUNTO 2: Agregar producto ordenado (RECURSIVO)

    def agregar(self, nombre, categoria, precio, cantidad):
        nuevo = Producto(nombre, categoria, precio, cantidad)
        self.cabeza = self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, nodo, nuevo):

        if nodo is None:
            return nuevo

        # Si el producto ya existe
        if nodo.nombre == nuevo.nombre:
            nodo.cantidad += nuevo.cantidad
            return nodo

        # Insertar antes si corresponde al orden alfabético
        if nuevo.nombre < nodo.nombre:
            nuevo.siguiente = nodo
            return nuevo

        nodo.siguiente = self._agregar_rec(nodo.siguiente, nuevo)
        return nodo


    # PUNTO 3: Valor total del inventario (RECURSIVO)

    def valor_total(self):
        return self._valor_total_rec(self.cabeza)

    def _valor_total_rec(self, nodo):

        if nodo is None:
            return 0

        valor = nodo.precio * nodo.cantidad
        return valor + self._valor_total_rec(nodo.siguiente)


    # PUNTO 4: Productos con bajo stock (RECURSIVO)

    def productos_bajo_stock(self, limite):
        nueva_lista = Inventario()
        self._bajo_stock_rec(self.cabeza, limite, nueva_lista)
        return nueva_lista

    def _bajo_stock_rec(self, nodo, limite, nueva_lista):

        if nodo is None:
            return

        if nodo.cantidad < limite:
            nueva_lista.agregar(nodo.nombre, nodo.categoria, nodo.precio, nodo.cantidad)

        self._bajo_stock_rec(nodo.siguiente, limite, nueva_lista)


    # PUNTO 5: Eliminar producto (RECURSIVO)

    def eliminar(self, nombre):
        eliminado = [False]
        self.cabeza = self._eliminar_rec(self.cabeza, nombre, eliminado)
        return eliminado[0]

    def _eliminar_rec(self, nodo, nombre, eliminado):

        if nodo is None:
            return None

        if nodo.nombre == nombre:
            eliminado[0] = True
            return nodo.siguiente

        nodo.siguiente = self._eliminar_rec(nodo.siguiente, nombre, eliminado)
        return nodo


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":
    inv = Inventario()
    
    # Agregar productos (deben quedar ordenados: Arroz, Leche, Pan, Sal)
    inv.agregar("Pan", "Panadería", 2500, 50)
    inv.agregar("Leche", "Lácteos", 4500, 30)
    inv.agregar("Arroz", "Granos", 3200, 100)
    inv.agregar("Sal", "Condimentos", 1500, 5)
    
    inv.mostrar()
    
    # Valor total: 2500*50 + 4500*30 + 3200*100 + 1500*5 = 587,500
    print("Valor total:", inv.valor_total())
    
    # Productos con stock < 40: Leche (30), Sal (5)
    bajo_stock = inv.productos_bajo_stock(40)
    bajo_stock.mostrar()
    
    # Eliminar Sal
    inv.eliminar("Sal")
    inv.mostrar()
