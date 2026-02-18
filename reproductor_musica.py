class Cancion:
    """Nodo para lista de canciones."""
    
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.titulo} - {self.artista}"


class ReproductorMusica:
    """Lista doblemente enlazada de canciones."""
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None  # Canción que se está reproduciendo

    def esta_vacio(self):
        return self.cabeza is None

    def agregar_cancion(self, titulo, artista):
        """Agrega una canción al final de la lista."""
        nueva = Cancion(titulo, artista)
        if self.esta_vacio():
            self.cabeza = nueva
            self.cola = nueva
            self.actual = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva
        print(f"Canción agregada: {nueva}")

    def siguiente_cancion(self):
        """Avanza a la siguiente canción."""
        if self.esta_vacio():
            print("No hay canciones en la lista.")
            return
        if self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("Llegaste al final de la lista, volviendo al inicio.")
            self.actual = self.cabeza
        self.reproducir_actual()

    def anterior_cancion(self):
        """Retrocede a la canción anterior."""
        if self.esta_vacio():
            print("No hay canciones en la lista.")
            return
        if self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("Estás en la primera canción, yendo a la última.")
            self.actual = self.cola
        self.reproducir_actual()

    def buscar_cancion(self, titulo):
        """Busca una canción por título."""
        actual = self.cabeza
        while actual:
            if actual.titulo.lower() == titulo.lower():
                print(f"Canción encontrada: {actual}")
                return
            actual = actual.siguiente
        print("Canción no encontrada.")

    def mostrar_lista(self):
        """Muestra todas las canciones de la lista."""
        if self.esta_vacio():
            print("Lista de reproducción vacía.")
            return
        actual = self.cabeza
        canciones = []
        while actual:
            canciones.append(str(actual))
            actual = actual.siguiente
        print("Lista de reproducción:")
        print(" -> ".join(canciones))

    def reproducir_actual(self):
        """Muestra la canción que se está reproduciendo."""
        if self.actual:
            print(f"Reproduciendo: {self.actual}")
        else:
            print("No hay canción seleccionada.")


# ================= MENÚ INTERACTIVO =================
def menu():
    reproductor = ReproductorMusica()

    while True:
        print("\n--- REPRODUCTOR DE MÚSICA ---")
        print("1 - Siguiente canción")
        print("2 - Anterior canción")
        print("3 - Agregar canción")
        print("4 - Buscar canción")
        print("5 - Mostrar lista")
        print("0 - Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            reproductor.siguiente_cancion()
        elif opcion == "2":
            reproductor.anterior_cancion()
        elif opcion == "3":
            titulo = input("Título de la canción: ")
            artista = input("Artista: ")
            reproductor.agregar_cancion(titulo, artista)
        elif opcion == "4":
            titulo = input("Título a buscar: ")
            reproductor.buscar_cancion(titulo)
        elif opcion == "5":
            reproductor.mostrar_lista()
        elif opcion == "0":
            print("Saliendo del reproductor...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar menú interactivo
if __name__ == "__main__":
    menu()
