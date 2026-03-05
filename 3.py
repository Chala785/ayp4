"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Un banco necesita un sistema para gestionar la cola de clientes en espera.
Los clientes tienen diferentes tipos de atención (preferencial, normal) y
se debe poder atender, consultar y gestionar la cola.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Cliente) con los atributos necesarios
2. Diseñar la clase Lista (Cola) con los métodos requeridos
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

a) Clase NODO (Cliente):
   - Debe almacenar: nombre, tipo de atención (preferencial/normal), 
     tiempo estimado de atención en minutos
   - Debe poder enlazarse con otro cliente

b) Clase LISTA (Cola):
   - Los clientes preferenciales van al INICIO
   - Los clientes normales van al FINAL


PUNTO 2 (1.0): AGREGAR CLIENTE - RECURSIVO
------------------------------------------
Implementa un método para agregar un cliente.
- Si es preferencial: insertar al inicio de los preferenciales
- Si es normal: insertar al final de la cola
- OBLIGATORIO usar recursividad para encontrar la posición


PUNTO 3 (1.0): TIEMPO DE ESPERA - RECURSIVO
-------------------------------------------
Implementa un método que calcule el tiempo de espera de un cliente
dado su nombre (suma de tiempos de todos los que están antes).
- OBLIGATORIO usar recursividad
- Retorna -1 si el cliente no está en la cola


PUNTO 4 (1.0): ATENDER SIGUIENTE
--------------------------------
Implementa un método que retire y retorne el primer cliente de la cola.
- Retorna None si la cola está vacía


PUNTO 5 (1.0): CONTAR POR TIPO - RECURSIVO
------------------------------------------
Implementa un método que cuente cuántos clientes hay de cada tipo.
- OBLIGATORIO usar recursividad
- Retorna una tupla (preferenciales, normales)

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""
# PUNTO 1a: Clase Nodo (Cliente)

class Cliente:
    def __init__(self, nombre, tipo, tiempo):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo = tiempo
        self.siguiente = None


# PUNTO 1b: Clase Lista (Cola)

class Cola:

    def __init__(self):
        self.cabeza = None


    # Mostrar cola
    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("Cola vacía")
            return

        while actual:
            print(f"{actual.nombre} | {actual.tipo} | {actual.tiempo} min")
            actual = actual.siguiente


    # PUNTO 2: Agregar cliente (RECURSIVO)

    def agregar(self, nombre, tipo, tiempo):
        nuevo = Cliente(nombre, tipo, tiempo)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self.cabeza = self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, nodo, nuevo):

        if nuevo.tipo == "preferencial":
            if nodo.tipo == "normal":
                nuevo.siguiente = nodo
                return nuevo

            if nodo.siguiente is None:
                nodo.siguiente = nuevo
                return nodo

            nodo.siguiente = self._agregar_rec(nodo.siguiente, nuevo)
            return nodo

        else:  # cliente normal
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
                return nodo

            nodo.siguiente = self._agregar_rec(nodo.siguiente, nuevo)
            return nodo


    # PUNTO 3: Tiempo de espera (RECURSIVO)

    def tiempo_espera(self, nombre):
        return self._tiempo_rec(self.cabeza, nombre, 0)

    def _tiempo_rec(self, nodo, nombre, acumulado):

        if nodo is None:
            return -1

        if nodo.nombre == nombre:
            return acumulado

        return self._tiempo_rec(nodo.siguiente, nombre, acumulado + nodo.tiempo)


    # PUNTO 4: Atender siguiente

    def atender(self):

        if self.cabeza is None:
            return None

        atendido = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return atendido


    # PUNTO 5: Contar por tipo (RECURSIVO)

    def contar_por_tipo(self):
        return self._contar_rec(self.cabeza)

    def _contar_rec(self, nodo):

        if nodo is None:
            return (0, 0)

        pref, norm = self._contar_rec(nodo.siguiente)

        if nodo.tipo == "preferencial":
            return (pref + 1, norm)
        else:
            return (pref, norm + 1)

# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":
    cola = Cola()
    
    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Ana", "preferencial", 8)
    
    # Orden esperado: María, Ana, Juan, Pedro (preferenciales primero)
    cola.mostrar()
    
    # Tiempo de espera de Pedro: 5 + 8 + 10 = 23 minutos
    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))
    
    # Contar por tipo: (2 preferenciales, 2 normales)
    print("Por tipo:", cola.contar_por_tipo())
    
    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)
