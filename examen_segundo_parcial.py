# Numeros en python
# Numeros Complejos
print("===================================================")
print("Numeros Complejos")
a = complex(5,1)
b = complex(-5,-1)
print(a)
print(type (a))
print (b)
print (type (b))

# Ejemplo extra 
print("Ejemplo extra")
a2 = complex(8,3)
b2 = complex(-8,-3)
print(a2)
print(type (a2))
print (b2)
print (type (b2))
print("===================================================")

#Aleatorios con randoms
print("Aleatorios con randoms")
import random
print ("Numero random: ", random.randrange(1,10))
print("Ejemplo extra")
print ("Numero random: ", random.randrange(1,100))
print("===================================================")

#Strings en python
#contar caracteres
print("Contar Caracteres (string)")
palabra = "murcielago"
print("caracteres en palabra: ",len(palabra))
print("Ejemplo extra")
palabra2 = "popocatepetl"
print(f"Caracteres en la palabra {palabra2}: ", len(palabra2))
print("===================================================")

#Booleanos en python
print("Booleanos en python")
print(f"por ejemplo (5>3)?", {5>3})
print(f"por ejemplo (5<3)?", {5<3})
print("Ejemplo extra")
print(f"por ejemplo (50+6>80-26), {50+6 > 80-26}")
print(f"por ejemplo (50+6<80-26), {50+6 < 80-26}")
print("===================================================")

#Operadores Aritmeticos en python
print("Operadores aritmeticos en python")
aritmeticos1 = 5
aritmeticos2 = 10
print(aritmeticos1+aritmeticos2)
print(aritmeticos1-aritmeticos2)
print("Ejemplo extra")
aritmeticos3 = 89
aritmeticos4 = 63
print(aritmeticos3+aritmeticos4)
print(aritmeticos3-aritmeticos4)
print("===================================================")

#ejemplos operadores aritmeticos
print("Ejemplos de operadores aritmeticos")
print("Suma: ", 5+3)
print("Resta: ", 10-4)
print("Multiplicacion: ", 3*4)
print("Divicion: ", f"{10/3}")
#Limitar a dos decimales 
print("División", f"{10 / 3:.2f}")
print("Divicion entera:", 10 // 3)
print("Módulo: ", 10 % 3 )
print("Potencia:", 2 ** 3)

print("Ejemplos extra")
print("Suma: ", 94+63)
print("Resta: ", 75-12)
print("Multiplicacion: ", 45*9)
print("Divicion: ", f"{89/2}")
#Limitar a dos decimales 
print("División", f"{89 / 3:.2f}")
print("Divicion entera:", 751 // 4)
print("Módulo: ", 89 % 5 )
print("Potencia:", 5 ** 4)
print("===================================================")

#Operadores de asignacion
#ejemplo (c=5)
c = 5
c *= 3
print("Operador (*=)",c)
c = 5
c /= 3
print("Operador (/=)", c)
c = 5
c %= 2
print("Operador (%=)", c)
c = 5
c //= 2
print("Operador (//=)", c)
c = 5
c **= 3
print("Operador (**=)", c)