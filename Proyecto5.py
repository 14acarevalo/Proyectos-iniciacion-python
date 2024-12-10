#Contador de vocales

def contadorVocales():
    print ("En este ejercicio, vamos a intentar contar las diferentes vocales de una palabra: ")
    palabra = input("Usuario, introduce una palabra: ")
    longitud = len(palabra)
    caracteres = palabra.split()
    num_palabra = len(palabra.split())
    vocales = "aeiou" 
    contador_de_vocales = 0
    
    print ("En primer lugar, vamos a sacar unos valores adicionales: ")
    print(f"La longitud de la palabra es: {longitud} caracteres")
    print(f"Los caracteres de la palabra/frase son: {caracteres}")
    print(f"En total tenemos: {num_palabra} palabra")
    
    
    for letra in palabra:
        if letra.lower() in vocales:
            contador_de_vocales += 1
        
    if contador_de_vocales > 0:
        print(f"En total, en la palabra '{palabra}' hay {contador_de_vocales} vocal(es).")
    else:
        print("Lo sentimos, tu palabra no tiene vocales.")        

contadorVocales()

    



    
    