

    
contraseña = input("Crea una contraseña: ")
     
if len(contraseña) < 8:
         print("Contraseña muy corta")
elif "@" not in contraseña:
        print("La contraseña debe incluir al menos un '@'")
else:
        print("Contraseña válida")


        

     
   
