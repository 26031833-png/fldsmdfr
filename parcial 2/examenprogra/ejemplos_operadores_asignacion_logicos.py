x=5
y=3
z=5
x > y
y < z
x == z
#ejemplo and
x > y and y > z
x > y
y > z
#ejemplo or
x > y or y > z
x > y
y > z
 
x=7
y=5
z=9
x > y
y < z
x == z
#ejemplo and
x > y and y > z
x > y
y > z
#ejemplo or
x > y or y > z
x > y
y > z
# 1. FORMA LARGA vs OPERADOR DE ASIGNACIÓN
x = 5
x = x + 3  # 8 forma larga
x = 5
x += 3  # 8 forma corta
x = 5
x -= 3  # 2

# 2. OPERACIONES BÁSICAS Y TIPOS
x = 5
x *= 3
print(x)  # 15 int

x = 5
x /= 3
print(x)  # 5.0 float

x = 5
x %= 2
print(x)  # 1.0 float

x = 5
x //= 2
print(x)  # 2 int

x = 5
x **= 3
print(x)  # 125 int

# 3. MÓDULO (%) Y DIVISIÓN ENTERA (//)
# Módulo - resto de la división
x = 5.0
x %= 2
print(x)  # 1.0

# División entera - ignora decimales
y = 20
y //= 2
print(y)  # 10

y = 21
y //= 2
print(y)  # 10 (ignora el .5)

# 4. EXPONENTE (**=)
y = 10
y **= 3  # 10 * 10 * 10
print(y)  # 1000

# 5. OPERADOR WALRUS (:=) - asigna y devuelve a la vez
print(z := 3)  # imprime 3 y a la vez z = 3
print(z)       # 3
# Ejemplo práctico - Cambiando números
a = 12
print(f"Valor inicial: {a}")

a += 7
print(f"a += 7 -> {a}")  # 19

a -= 4
print(f"a -= 4 -> {a}")  # 15

a *= 2
print(f"a *= 2 -> {a}")  # 30

a /= 3
print(f"a /= 3 -> {a}")  # 10.0 float

a %= 4
print(f"a %= 4 -> {a}")  # 2.0 resto de 10 / 4

a = 12
a //= 5
print(f"12 //= 5 -> {a}")  # 2

a = 4
a **= 3
print(f"4 **= 3 -> {a}")  # 64

# Walrus con números diferentes
print(f"Con walrus: {a : = 10} y ahora a vale {a}")