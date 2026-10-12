edad = 18
tiene_identificacion = True
es_estudiante = False

if edad >= 18 and tiene_identificacion:
    print ("cumple ambas condiciones")

if edad >= 18 or es_estudiante:
    print("cumple al menos una condicion")

if not es_estudiante:
    print("no es estudiante")