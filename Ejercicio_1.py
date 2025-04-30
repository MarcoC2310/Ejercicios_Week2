#Ejercio 1: Determinar signo y paridad.

#Declaracion de variables y mensaje para ingresar dato
num = int(input("Hola, digita un valor\n"))

#Condicionales para la determinacion de signo
if num > 0:
    print("\nEl número es positivo")
    #Concionales para determinar su paridad
    if num % 2 == 0:  
        print("\nEl número es par")
    else:
        print ("\nEl numero es impar")
elif num < 0:
    print("\nEl numero es negativo")
    #Concionales para determinar su paridad
    if num % 2 == 0:
        print("\nEl número es par")
    else:
        print ("\nEl numero es impar")
elif num == 0:
    print ("El numero es 0")



