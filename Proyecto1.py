# Proyecto 1 - Contador de palabras



def contadorPalabras():
    frase = input("Usuario, introduce una frase por favor: ")
    longitud = len(frase)
    lineas = len(frase.split())
    palabras = frase.split()
    
    print (f"La longitud de las palabras es: {longitud}")
    print (f"El número de palabras es: {lineas}")
    print (f"Las palabras de la frase son: {palabras}")
    
    
    
contadorPalabras()


    


