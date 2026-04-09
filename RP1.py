import re

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.
    """
    # TODO: Implementar con re.match o re.search
    patron = r'^[A-Z]{3}-?\d{3}$'
    return bool(re.match(patron, placa))
    pass


def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    """
    # TODO: Implementar con re.findall
    return re.findall(r'#\w+', texto)
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
        nuevo = Pedido(cliente, direccion, valor)

        def _agregar_rec(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                _agregar_rec(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            _agregar_rec(self.cabeza)
        pass


    def valor_pendiente(self):
        """
        Retorna la suma de valores de pedidos NO entregados.
        OBLIGATORIO usar recursividad.
        """
        # TODO: Implementar
        def _sumar(nodo):
            if nodo is None:
                return 0
            valor = nodo.valor if not nodo.entregado else 0
            return valor + _sumar(nodo.siguiente)

        return _sumar(self.cabeza)
        pass


    def eliminar_entregados(self):
        """
        Elimina todos los pedidos que ya fueron entregados.
        """
        # TODO: Implementar
        def _eliminar(nodo):
            if nodo is None:
                return None
            if nodo.entregado:
                return _eliminar(nodo.siguiente)
            nodo.siguiente = _eliminar(nodo.siguiente)
            return nodo

        self.cabeza = _eliminar(self.cabeza)
        pass


club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


def estudiantes_en_todos():
    """
    Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
    """
    # TODO: Implementar
    return club_ciencias & club_deportes & club_arte
    pass


def solo_un_club():
    """
    Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.
    """
    # TODO: Implementar
    solo_ciencias = club_ciencias - club_deportes - club_arte
    solo_deportes = club_deportes - club_ciencias - club_arte
    solo_arte = club_arte - club_ciencias - club_deportes

    return solo_ciencias | solo_deportes | solo_arte
    pass


def clubes_de_estudiante(nombre):
    """
    Retorna una lista con los nombres de los clubes a los que pertenece
    el estudiante.
    """
    # TODO: Implementar
    resultado = []

    if nombre in club_ciencias:
        resultado.append("Ciencias")
    if nombre in club_deportes:
        resultado.append("Deportes")
    if nombre in club_arte:
        resultado.append("Arte")

    return resultado
    pass


def escalones_sin_memo(n):
    """
    Calcula de cuántas formas se puede subir una escalera de n escalones.
    """
    # TODO: Implementar
    if n == 0:
        return 1
    if n == 1:
        return 1
    return escalones_sin_memo(n-1) + escalones_sin_memo(n-2)
    pass


def escalones_con_memo(n, memo=None):
    """
    Misma función pero usando memorización.
    """
    # TODO: Implementar
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if n == 1:
        return 1

    memo[n] = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
    return memo[n]
    pass