#Número mágico

import random


def numeroMagico():
    print("Usuario, vamos a jugar a un juego, necesito que adivines un número mágico el cual se encuentra entre el 1 y el 20")
    numero_magico = random.randint(1,20)
    intentos = 0
    
    while True:   
        try:
            numero = int(input("Usuario, introduce un número: "))
            if numero < 1 or numero > 20:
                print("El número tiene que estar entre 1 y 20")
                continue
            
            intentos +=1

            if numero == numero_magico :
                print (f"Has acertado, el digito era {numero_magico}")
                break
            elif numero > numero_magico:
                print ("Tu numero es más grande que el número mágico")
            elif numero < numero_magico:
                print ("Tu numero es menor que el número mágico")   
            
        except ValueError:
            print ("El número se encuentra fuera del rango deseado")
        


numeroMagico()



   