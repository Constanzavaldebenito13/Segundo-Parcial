nombre=input("Hola,dime tu nombre porfavor")


intento = 5

while intento > 0:
   password=input ("Ingrese su clave porfavor")
   if password =="1234":
     print (f"Su clave es correcta Bienvenido,{nombre}")
     break
   else:
      intento = intento - 1
      print(f"Intento fallido,intentelo nuevamente,te falta, {intento}")
if intento == 0:
         print("acceso denegado,porfavor comuniquese con nuestro call center")