#Lista de compras

class Lista_de_compra:
    
    def __init__(self):
        self.lista_compra = []
        
    
    def añadir_producto(self,producto):
        self.lista_compra.append(producto)
        print(f"El nuevo producto esta añadido {producto}")
    
    
    def eliminar_producto(self, producto):
        if producto in self.lista_compra:
            self.lista_compra.remove(producto)
        else:
            print ("Lo siento, el producto no está en la lista...")
            
    def mostrar_lista(self):
        if not self.lista_compra:
            print ("La lista de la compra está vacia...")
        else:
            for producto in self.lista_compra:
                print(f"Producto: {producto}")
                


mi_lista = Lista_de_compra()
mi_lista.añadir_producto("chocolate")
mi_lista.eliminar_producto("aceitunas")
mi_lista.mostrar_lista()
        
    