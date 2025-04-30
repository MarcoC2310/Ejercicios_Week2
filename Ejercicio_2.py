#Ejercicio 2: Clasificacion de edades.

#Declaracion de Variables y mensaje para la entrada de un dato.
while True:
    try:
        # Solicitar al usuario que ingrese su edad
        edad = int(input("Hola, Cuál es tu edad? \n"))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingresa un número entero válido.")


#Condiciones para determinar la categoria de la edad.
if edad > 65:
    print ("\nHola, eres un adulto mayor")
elif edad < 65 and edad >= 31:
    print ("\nHola, eres un adulto maduro")
elif edad < 31 and edad >= 18:
    print ("\nHola, eres un adulto joven")
elif edad < 18:
    print ("\nHola, eres un menor de edad")




    

