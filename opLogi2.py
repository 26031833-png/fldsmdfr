
# Programa de conversion de tipos

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

# Convertir la edad a texto
edad_texto = str(edad)

print("Hola", nombre)
print("Tu edad es:", edad_texto)
print("Tu altura es:", altura)

# Comprobar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
