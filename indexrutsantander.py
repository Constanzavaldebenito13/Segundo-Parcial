
try:
    rut = int(input("Hola,Bienvenido a Banco Santander,Ingrese su rut,sin puntos ni guion"))

    if rut == 135466791:
        password=int(input("Por favor introduzca su contraseña,No debe ser mayor o menor a 10 dígitos"))

    if rut==0:
        raise ZeroDivisionError
    
    if password== 12121212121212121212:
     print("Contraseña correcta,ingreso exitoso")
        
except ValueError:
    print("¡Error! Debes ingresar valores numéricos.")

except ZeroDivisionError:
    print("¡Error! ,Ingrese un rut valido.")


print("Programa finalizado.")


    
