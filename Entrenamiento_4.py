#. Descuento en tienda según monto y tipo de cliente

#Se declaran las variables y mensaje para el ingreso de dato
valor_compra = float(input("Hola, ingresa el valor de tu compra: \n"))

while True:
    tipo_cliente = input("Eres cliente VIP, Marca; 'S' para si y 'N' para no:  ").upper()

    if tipo_cliente == 'S':
         if valor_compra >= 0 and valor_compra < 500:
              descuento = 10
              monto_descuento = (valor_compra * descuento) / 100
              valor_final = valor_compra - monto_descuento
              print("El descuento es: 10%")
              print(f"Valor del producto: {valor_compra:.1f}")
              print(f"El valor de tu producto es: {valor_final:.1f}")
              break

         elif valor_compra > 500:
              descuento = 20
              monto_descuento = (valor_compra * descuento) / 100
              valor_final = valor_compra - monto_descuento
              print("El descuento aplicado es: 20%")
              print(f"Valor del producto: {valor_compra:.1f}")
              print(f"El valor de tu producto es: {valor_final:.1f}")
              break
         else:
              print("Ingresa un valor positivo")


    elif tipo_cliente == 'N':
        
         print(f"El valor del producto es: {valor_compra}")
    else:
         print("Dato invalido. Por favor responde 'S' o 'N'\n")



            
        