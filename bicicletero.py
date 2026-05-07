print("Hola,Bienvenido")

#entrada de datos y valores base

print("El valor mensual de los bicicleteros es de 15000 pesos mensuales")
valor_bicicletero=15000
print("El valor de los candados es de 9000 pesos mensuales")
valor_candado=9000

dias=int(input("Ingresa la cantidad de dias que utilizaras el  bicicletero"))

estudiante=input("¿Eres estudiante? (si/no)")

candado=input("¿Desea incluir el candado? (si/no)")

tarjeta=input("¿Pagara con tarjeta de credito) (si/no)")

#Descuentos

descuento=0 

if dias <10:
    descuento=0
elif dias >=20 and estudiante=="no":
    descuento=15
elif 10<=dias <20 and estudiante=="si":
    descuento=15
elif 10<=dias <20 and estudiante=="no":
    descuento=8

#Descuento estudiantes

if estudiante=="si":

    if tarjeta=="si":
        descuento+=12
        
    if dias <15:
        descuento=5

monto_descuento=valor_bicicletero*(descuento/100)
valor_final=valor_bicicletero-monto_descuento

if candado=="si":
    valor_final +=valor_candado

print("=======RESUMEN=======")
print("Valor bicicletero: $",valor_bicicletero)
print("Descuento aplicado:",descuento,"%")

if candado=="si":
    print("Candado agregado$",valor_candado)

print("Valor final a pagar: $",valor_final)