class Estudiante:
    def __init__(self, Documento, Nombre):
        self.Documento = Documento
        self.Nombre = Nombre

estudiante1 = Estudiante("Alberto", 11111)
print(estudiante1.Documento)
print(estudiante1.Nombre)        