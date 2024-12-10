#Calcular el IMC

def IMC ():
    print("El indice de masa muscular puede orientarnos levemente, actualmente no es la mejor herramienta para valorar nuestro estado de salud. \nPor eso, siempre es mejor usar los pliegues ")
    print("\n")
    print("Usuario, vamos a calcular el IMC (Indice de Masa Muscular): ")
    try:
        peso = float(input("Introduce tu peso en kilogramos: "))
    except TypeError:
        print ("Necesitamos un valor númerico...")  
    try:    
        altura = float(input("Introduce tu altura en metros: "))
    except TypeError:
        print ("Necesitamos un valor númerico...")
        
    IMC = peso/altura**2
    print (f"Tu IMC se corresponde con: {IMC}")
    
    if IMC > 18.5:
        print ("Tienes un peso muy bajo... come algo más")
    elif IMC < 24.5 and IMC >= 18.6:
        print ("Tienes un peso normal, bien")
    elif IMC < 29.9 and IMC >= 24.6:
        print ("Tienes sobrepeso")
    elif IMC > 30:
        print ("Tienes obesidad")
        
        
IMC()

    
    

        
    
    
    