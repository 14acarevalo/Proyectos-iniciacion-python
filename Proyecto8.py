

class Biblioteca:
    
    def __init__(self):
        self.libros = []
        
    def añadir_libro (self, libro, autor):
        if (libro, autor) in self.libros:
            print ("Lo siento, no se puede añadir ese libro, ya lo tenemos en la biblioteca")
        else:
            self.libros.append((libro, autor))
            print("Libro añadido correctamente ")
    
    def eliminar_libro (self, libro, autor):
        if (libro, autor) in self.libros:
            self.libros.remove((libro, autor))
            print ("Libro eliminado con éxito ")

    def buscar_libro(self, libro, autor):
        if (libro, autor) in self.libros:
            print (f"Hemos encontrado tu libro {libro} cuyo autor es {autor}")
        else:
            print ("Lo siento, el libro no aparece en nuestra biblioteca")
    
    def mostrar_libros(self):
        if not self.libros:  # Comprobamos si la lista de libros está vacía.
            print("La biblioteca no tiene libros.")
        else:
            print("Libros en la biblioteca:")
            for libro, autor in self.libros:  # Desempaquetamos la tupla (libro, autor) correctamente.
                print(f"Libro: {libro} - Autor: {autor}")
                
                
                
libreria = Biblioteca()
libreria.añadir_libro("Harry Potter", "J.K Rowgling")
libreria.añadir_libro("El señor de los anillos", "Tolkie")
libreria.añadir_libro("Harry Potter", "J.K Rowgling")
libreria.mostrar_libros()
libreria.buscar_libro("Harry Potter", "J.K Rowgling")
libreria.buscar_libro("Star Wars", "J.K Rowgling")
libreria.eliminar_libro("Harry Potter", "J.K Rowgling")
libreria.mostrar_libros()


