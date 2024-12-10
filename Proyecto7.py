# Gestion de contactos

class GestionContactos:
    
    def __init__(self):
        self.agenda = []
    
    def añadir_contacto(self, contacto, telefono):
        self.agenda.append((contacto, telefono))
        print (f"Hemos añadido un nuevo contacto, su nombre es {contacto} y su telefono es {telefono}")
        
    def eliminar_contacto(self, contacto):
        # Cambiado: debemos buscar el contacto y su teléfono en la lista de tuplas
        for c, t in self.agenda:  # Iteramos sobre la lista de contactos y teléfonos
            if c == contacto:
                self.agenda.remove((c, t))  # Eliminar la tupla del contacto y su teléfono
                print("Contacto eliminado...")
                return  # Salimos de la función
        print("Lo sentimos, el contacto no está en la agenda...")  # Mensaje mejorado
     
    
    def mostrar_contacto(self):
        for contacto, telefono in self.agenda:
            
            print(f"Contacto: {contacto} y su telefono es {telefono}")
            
            
Libreta = GestionContactos()
Libreta.añadir_contacto("Alberto", 1234567)
Libreta.añadir_contacto("Pepe", 4567)
Libreta.añadir_contacto("Juan", 67)
Libreta.añadir_contacto("Lucas", 1237)
Libreta.mostrar_contacto()
Libreta.eliminar_contacto("Pepe")
Libreta.mostrar_contacto()


        
        