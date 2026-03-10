# datos= [5, 3, 8, 1, 2, 9, 4]
# import heapq

# heapq.heapify(datos)
# print("heap:", datos)

# heapq.heappush(datos, 6)
# print("heap después de agregar 6:", datos)

# minimo = heapq.heappop(datos)
# print("Elemento mínimo extraído:", minimo)
# print("heap después de extraer el mínimo:", datos)

# minimo = heapq.heappushpop(datos, 7)
# datos2= [(2, 'A'), (1, 'B'), (3, 'C'), (2, 'B')]
# heapq.heapify(datos2)
# print("heap con tuplas:", datos2)

"""---------------------------------"""
# Programa para un hospital
# Cada paciente tiene propiedad de 1 a 3, 1 es la mas importante 
# Las personas del hopspital deben saber quien es el siguiente en atender
# e indicar su nombre y su prioridad

# import heapq

# hospital = []
# turno = 0

# n = int(input("Cuántos pacientes desea ingresar? "))

# for i in range(n):
#     nombre = input(f"Nombre del paciente {i+1}: ")
#     prioridad = int(input(f"Prioridad del paciente {i+1} (1-3): "))
    
#     heapq.heappush(hospital, (prioridad, turno, nombre))
#     turno += 1

# print("\nPacientes en orden de atención:")

# while hospital:
#     prioridad, turno, nombre = heapq.heappop(hospital)
#     print("Paciente:", nombre)
#     print("Prioridad:", prioridad)

"""-------"""
# Un programa que me premita programar tareas y me diga
# cual es la sigueinte tarea a realizar segun calendario

from datetime import datetime, timedelta
import heapq
tareas = []
heapq.heapify(tareas)

hoy = datetime.now()
while True:
    linea = input("tarea:")
    if linea.lower() == "fin":
        break
    partes = linea.split(maxsplit=1)
    if len(partes) != 2:
        print("Entrada no válida. Use el formato: 'YYYY-MM-DD tarea'")
        continue
    dias = int(partes[0])
    descripcion = partes[1]
    fecha_ejecucion = hoy + timedelta(days=dias)
    heapq.heappush(tareas, (fecha_ejecucion, descripcion))
print(f"Tareas en el heap:", tareas)
print("Orden de ejecución de las tareas segun calendario: ")
while tareas:
    fecha, tarea = heapq.heappop(tareas)
    dias_restantes = (fecha - hoy).days
    print(f" en {dias_restantes} días: {descripcion}")
    
print("No hay más tareas programadas.")






# Escuela = []
# turno = 0

# n = int(input("Cuántas tareas desea ingresar? "))
# for i in range(n):
#     tarea = input(f"Descripción de la tarea {i+1}: ")
#     fecha = input(f"Fecha de la tarea {i+1} (YYYY-MM-DD): ")
    
#     heapq.heappush(Escuela, (fecha, turno, tarea))
#     turno += 1

# print("\nTareas en orden de ejecución:")

# while Escuela:
#     fecha, turno, tarea = heapq.heappop(Escuela)
#     print("Tarea:", tarea)
#     print("Fecha:", fecha)



