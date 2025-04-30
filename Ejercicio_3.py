#Ejercicio3: Tarifa de transporte segun el dia y la hora
while True:
    respuesta = input("El dia de hoy es laborable?\n Ingresa 'S' para si o 'N' para no:\n").upper()
   
 
    if respuesta == 'S': 
        hora = int(input("Ingresa la hora en formato 24 horas:\n"))
        if hora >= 6 and hora < 9 or hora >= 17 and hora < 20:
            print ("la tarifa a cobrar será de $7")
        elif hora >= 9 and hora < 17:
            print ("la tarifa a cobrar será de $5")
        elif hora >= 20 and hora < 24:
            print ("la tarifa a cobrar será de $5")
        elif hora >= 0 and hora < 6:
            print ("la tarifa a cobrar será de $5")
        else: 
            print("Hora no valida. Por favor ingresa una hora entre 0 y 23,")
        break
    elif respuesta == 'N':
        print ("Disfruta de tu fin de semana!")
        break
    else:
        print("Respuesta no valida. Por favor ingresa 'S' o 'N'.")
        

    





