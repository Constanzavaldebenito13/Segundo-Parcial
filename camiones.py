print("Hola,bienvenido a camionesapp")

print("El precio transporte por camion es de 150000")
precio_camion=150000
camion_metros=29
import math
while True:

    nombre=input("Ingrese su nombre")
    if len(nombre)>=3:
        break
    else:
        print("El nombre no puede ser menor a tres caracteres")

while True:

    numero=input("Ingrese su número de telefono")
    if numero.isdigit() and 8 <= len(numero) <= 9:
        break
    else:
        print("Su numero de telefono debe tener de 8 a 9 digitos")

print("=====DATOS DE LA CARGA=====")

while True:
     
    cajas_largo=int(input("Ingrese el largo de su mercaderia en cm"))
    cajas_ancho=int(input("Ingrese el ancho de su mercaderia en cm"))
    cajas_alto=int(input("Ingrese el alto de su mercaderia en cm"))
    
    volumen_cajas=(cajas_largo/100)*(cajas_ancho/100)*(cajas_alto/100)
   
    cantidad_cajas=int(input("Ingrese la cantidad de cajas a transportar"))
    volumen_carga_total=volumen_cajas*cantidad_cajas
#math.ceil redondea a cualquier decimal,pero esta se debe llamar con import math en la parte de arriba
    camiones_necesarios=math.ceil(volumen_carga_total/camion_metros)

    valor_total=camiones_necesarios*precio_camion
    break
print("=====BOLETA=====")
print(f"Cliente: {nombre}")
print(f"Telefono: {numero}")
print(f"Cantidad de cajas transportadas: {cantidad_cajas}")
print(f"Camiones necesarios: {camiones_necesarios}")
print(f"Valor total a pagar: $",valor_total)