alumno = {
"nombre": "Ana López",
"grupo": "3A",
"calificaciones": [8.5, 9.0, 7.5]
}

# Acceder
print(alumno["nombre"]) # "Ana López"


# Agregar / modificar
alumno["email"] = "ana@mail.com"
alumno["grupo"] = "3B"

# Recorrer
# c1AVE Y VALOR
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

# Valores
for valor in alumno.values(): 
    print(valor)

# Claves
for clave in alumno: 
    print(clave)

    ##extra 

alumno = {
    "nombre": "Guillermo",
    "edad": 18,
    "carrera": "Ingeniería en mecatronica",
}

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

for valor in alumno.values():
    print(valor)

for clave in alumno:
    print(clave)