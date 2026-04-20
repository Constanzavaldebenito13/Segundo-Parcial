def saludo(nombre):
    return ("hola", nombre + "!")

mensaje = saludo("Bienvenido ")

nombre=input("Ingrese su nombre:")

print(f"{mensaje}", nombre)

