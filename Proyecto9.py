#Inventario productos

class inventario:
    def __init__(self) :
        self.productos = []
        
    def añadir_Productos (self, productos, nombre):
        self.productos.append((productos, nombre));
        return (f"El producto {productos} ha sido añadido con el nombre {nombre}")
    
    def eliminar_Productos(self, productos, nombre):
        if (productos, nombre) in self.productos:
            self.productos.remove((productos,nombre))
            print ("Producto eliminado exitosamente ")
        else:
            print ("Lo siento, no he podido encontrar tu producto en nuestro inventario")
    
    def mostrar_productos (self):
        if not self.productos:
            print ("No hay productos que mostrar...")
        else:
            for productos, nombre in self.productos:
                print (f"Producto: {productos} - Nombre: {nombre}")
                
    
tienda = inventario()
tienda.añadir_Productos("Laca", "Nelly")
tienda.añadir_Productos("Colacao", "Neskey")
tienda.añadir_Productos("Sal", "Yodada")
tienda.mostrar_productos()
tienda.eliminar_Productos("Sal", "Yodada")
tienda.mostrar_productos()



