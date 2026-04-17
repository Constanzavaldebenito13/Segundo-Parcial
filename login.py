##Input ingresa la informacion

nombre= input("Dime tu nombre porfavor ")
#La f ayuda para no poner la informacion recibida fuera del las comillas
print (f"Hola{nombre}¡Bienvenido!")

contraseña= input("Por favor dime tu contraseña")
#If es como si-entonces else es o
if contraseña == "1234":
    print("Tu contraseña es correcta,puedes ingresar")
else:
    print("Tu contraseña es incorrecta,no puedes ingresar")
    print("Vuelve a intentarlo")

 


