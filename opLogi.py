
# Programa de operadores logicos

edad = int(input("Ingresa tu edad: "))
tiene_credencial = input("¿Tienes credencial? (si/no): ")

# Operador AND
if edad >= 18 and tiene_credencial == "si":
    print("Puedes entrar")

# Operador OR
elif edad < 18 or tiene_credencial == "no":
    print("No puedes entrar")

# Operador NOT
if not edad >= 18:
    print("Eres menor de edad")
