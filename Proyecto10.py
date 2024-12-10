
class Libro:
    
    def __init__(self):
        self.libro = []
        
    def prestarLibro(self, titulo, autor ):
        libro = {"Titulo: ": titulo, "Autor: ": autor, "prestado": False}
        self.libro.append(libro)
        print(f"Libro '{titulo}' del autor {autor} añadido a la biblioteca.")
                 
    def devolverLibro(self, titulo, autor):
      for libro in self.libro:
          if libro["titulo"] == titulo:
              if not libro["prestado"]:
                  print (f"El libro {libro} está presente en la biblioteca")
              else:
               libro ["prestado"] == False
               print(f"Has devuelto correctamente el libro con nombre {titulo}") 
          return 
      print("EL libro no esta presente en la biblioteca" )
      
    def mostrarLibros(self):
        if not self.libro:
            print("La biblioteca actualmente se encuentra vacía ")
        else:
            for libro in self.libro:
                estado = 'prestado' if libro['prestado'] else 'disponible'
                print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {estado}")
                  
              