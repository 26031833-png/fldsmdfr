nombre = input("ingresar tu nombre: ")
calificaciones = []
for i in range(3):
    calificacion = float(input(f"Ingresa la calificacion {i + 1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)
print("Nombre; ", nombre)
print("Calificaciones:", calificaciones)
print(f"Promedio: {promedio:.2f}")

if promedio >= 69.0:
    print("Calificaciones: Aprobó")
else:
    print("Resultados: Reprobó")