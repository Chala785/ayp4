"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN B
                    Sistema de Gestión de Tareas (To-Do List)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Tarea)

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.siguiente = None


# PUNTO 1b: Clase Lista (ListaTareas)

class ListaTareas:
    
    def __init__(self):
        self.cabeza = None


    # Mostrar lista de tareas
    def mostrar(self):
        actual = self.cabeza
        
        if actual is None:
            print("La lista de tareas está vacía.")
            return
        
        while actual is not None:
            estado = "✓" if actual.completada else "○"
            print(f"[{estado}] {actual.descripcion} (Prioridad: {actual.prioridad})")
            actual = actual.siguiente


    # PUNTO 2: Agregar tarea ordenada (RECURSIVO)

    def agregar(self, descripcion, prioridad):
        nueva_tarea = Tarea(descripcion, prioridad)
        self.cabeza = self._agregar_recursivo(self.cabeza, nueva_tarea)

    def _agregar_recursivo(self, nodo_actual, nueva_tarea):

        if nodo_actual is None or nueva_tarea.prioridad > nodo_actual.prioridad:
            nueva_tarea.siguiente = nodo_actual
            return nueva_tarea

        nodo_actual.siguiente = self._agregar_recursivo(nodo_actual.siguiente, nueva_tarea)
        return nodo_actual


    # Método para marcar una tarea como completada
    def completar(self, descripcion):
        actual = self.cabeza

        while actual is not None:
            if actual.descripcion == descripcion:
                actual.completada = True
                return

            actual = actual.siguiente


    # PUNTO 3: Contar pendientes por prioridad (RECURSIVO)

    def contar_pendientes(self, prioridad):
        return self._contar_pendientes_recursivo(self.cabeza, prioridad)

    def _contar_pendientes_recursivo(self, nodo, prioridad):

        if nodo is None:
            return 0

        if nodo.prioridad == prioridad and not nodo.completada:
            return 1 + self._contar_pendientes_recursivo(nodo.siguiente, prioridad)

        return self._contar_pendientes_recursivo(nodo.siguiente, prioridad)


    # PUNTO 4: Obtener urgentes (RECURSIVO)

    def obtener_urgentes(self):

        urgentes = ListaTareas()
        self._obtener_urgentes_recursivo(self.cabeza, urgentes)

        return urgentes

    def _obtener_urgentes_recursivo(self, nodo, urgentes):

        if nodo is None:
            return

        if nodo.prioridad >= 4 and not nodo.completada:
            urgentes.agregar(nodo.descripcion, nodo.prioridad)

        self._obtener_urgentes_recursivo(nodo.siguiente, urgentes)


    # PUNTO 5: Limpiar completadas (RECURSIVO)

    def limpiar_completadas(self):
        self.cabeza = self._limpiar_completadas_recursivo(self.cabeza)

    def _limpiar_completadas_recursivo(self, nodo):

        if nodo is None:
            return None

        nodo.siguiente = self._limpiar_completadas_recursivo(nodo.siguiente)

        if nodo.completada:
            return nodo.siguiente

        return nodo


# ═══════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 60)
    print("         PRUEBAS DEL SISTEMA DE TAREAS")
    print("=" * 60)

    mis_tareas = ListaTareas()

    # Agregar tareas
    mis_tareas.agregar("Comprar leche", 2)
    mis_tareas.agregar("Estudiar para parcial", 5)
    mis_tareas.agregar("Llamar al médico", 4)
    mis_tareas.agregar("Ver serie", 1)
    mis_tareas.agregar("Entregar proyecto", 5)
    mis_tareas.agregar("Hacer ejercicio", 3)

    print("\n📋 Lista de tareas (ordenada por prioridad):")
    mis_tareas.mostrar()
    print("Esperado orden de prioridades: 5, 5, 4, 3, 2, 1")

    # Contar pendientes
    print("\n🔢 Tareas urgentes (prioridad 5):", mis_tareas.contar_pendientes(5))
    print("Esperado: 2")

    # Marcar algunas como completadas
    mis_tareas.completar("Comprar leche")
    mis_tareas.completar("Ver serie")
    mis_tareas.completar("Estudiar para parcial")

    # Obtener urgentes
    print("\n🚨 Tareas urgentes pendientes:")
    urgentes = mis_tareas.obtener_urgentes()
    urgentes.mostrar()

    # Limpiar completadas
    print("\n🗑️ Eliminando tareas completadas...")
    mis_tareas.limpiar_completadas()
    mis_tareas.mostrar()