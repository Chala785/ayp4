import re

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.

    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123

    Ejemplos:
        validar_placa_vehiculo("ABC123") -> True
        validar_placa_vehiculo("ABC-123") -> True
        validar_placa_vehiculo("AB1234") -> False
        validar_placa_vehiculo("abc123") -> False
    """

    # TODO: Implementar con re.match o re.search
    pass

def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.

    Ejemplo:
        extraer_hashtags("hola #python es #genial y #100dias")
        -> ["#python", "#genial", "#100dias"]
    """
    # TODO: Implementar con re.findall
    pass

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        estado = "✔" if self.entregado else "✘"
        return f"[{estado}] {self.cliente} - ${self.valor} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Sin pedidos")
            return
        while actual:
            print(f"{actual}")
            actual = actual.siguiente

def agregar(self, cliente, direccion, valor):
    """
    Agrega un nuevo pedido al FINAL de la lista.
    OBLIGATORIO usar recursividad.
    """
    # TODO: Implementar
    pass


def valor_pendiente(self):
    """
    Retorna la suma de valores de pedidos NO entregados.
    OBLIGATORIO usar recursividad.

    Ejemplo:
        Pedido1 (entregado, $25000) + Pedido2 (pendiente, $30000)
        + Pedido3 (pendiente, $15000)
        --> Retorna 45000
    """
    # TODO: Implementar
    pass


def eliminar_entregados(self):
    """
    Elimina todos los pedidos que ya fueron entregados.
    OBLIGATORIO usar recursividad.
    Modifica la lista original.
    """
    # TODO: Implementar
    pass

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_todos():
    """
    Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
    (Intersección de los tres)
    """
    # TODO: Implementar
    pass


def solo_un_club():
    """
    Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.

    Pista: Un estudiante está en exactamente un club si está en ese club
    pero NO en los otros dos.

    Ejemplo esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"}
    """
    # TODO: Implementar
    pass


def clubes_de_estudiante(nombre):
    """
    Retorna una lista con los nombres de los clubes a los que pertenece
    el estudiante.

    Ejemplo:
        clubes_de_estudiante("Carlos") -> ["Ciencias", "Deportes"]
        clubes_de_estudiante("Julia") -> ["Arte"]
    """
    # TODO: Implementar
    pass

"""
Tienes una escalera de N escalones. En cada paso puedes subir 1 o 2 escalones.
¿De cuántas formas distintas puedes llegar al escalón N?

Ejemplo:
N=1: 1 forma → [1]
N=2: 2 formas → [1+1, 2]
N=3: 3 formas → [1+1+1, 1+2, 2+1]
N=4: 5 formas → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
"""

def escalones_sin_memo(n):
    """
    Calcula de cuántas formas se puede subir una escalera de n escalones.
    En cada paso puedes subir 1 o 2 escalones.

    Implementar con recursividad pura (sin memorización).

    Casos base:
        n == 0 -> 1 (hay una forma de "no subir")
        n == 1 -> 1

    Caso recursivo:
        escalones(n) = escalones(n-1) + escalones(n-2)
    """
    # TODO: Implementar
    pass


def escalones_con_memo(n, memo=None):
    """
    Misma función pero usando un diccionario para guardar resultados
    ya calculados y evitar recalcular.

    Ejemplo:
        escalones_con_memo(10) -> 89
        escalones_con_memo(30) -> 1346269 (sin memo esto tardaría mucho)
    """
    # TODO: Implementar
    pass
