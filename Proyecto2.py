#Conversor de temperaturas

def conversor_temperaturas():
    print ("Recuerda, que solo se puede pasar de Farenheit a Celsius, de Celsius a Kelvin, de Kelvin a Celsius y Fareheit a Kelvin")
    palabra = input("Usuario, nombra la temperatura que deseas convertir: ").lower()
    grados = float(input("Usuario, nombra los grados que deseas convertir: "))
    conversion = input ("Usuario, ¿a que quieres convertirla?: ").lower()
    
    try: 
        if palabra == "farenheit" and conversion == "celsius":
            cambio1 = (grados-32) * 5/ 9
            print (f"La conversión da como resultado: {cambio1:.2f} Gº")
        elif  palabra == "farenheit" and conversion == "kelvin":
            cambio2 = (grados-32) * 5/ 9 +273,15
            print (f"La conversión da como resultado: {cambio2:.2f} K")
        elif palabra == "celsius" and conversion == "kelvin":
            cambio3 = grados + 273,15
            print (f"La conversión da como resultado: {cambio3:.2f} K")
        elif palabra == "kelvin" and conversion == "celsius":
            cambio4 = grados - 273,15
            print (f"La conversión da como resultado: {cambio4:.2f} Gº")
        else:
            print ("Has introducido valores no válidos...")
              
    except TypeError:
        print ("Has introducido valores no validos")
        
conversor_temperaturas()

