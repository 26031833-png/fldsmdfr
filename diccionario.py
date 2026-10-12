##key: value
auto = {
    "marca": "Renault",
"modelo": "Clio",
"año": 2025
}

##Con corchetes
print(auto["marca"]) 

##Con get()
print(auto.get("marca"))

##TIp
##get() ## evita errores si la clave no existe:
print(auto.get("precio", "No existe"))

##CLAVES, VALORES Y VERIFICACIÓN
if "marca" in auto:
    print("Sí existe")

    ##Usa.lower() si necesitas ignorar mayúsculas:
if "marca".lower() in (k.lower() for k in auto): ...

##MODIFICAR, AGREGAR Y ELIMINAR
auto["año"] = 2020 # modifica 
auto["color"] = "verde" # agrega

##Con update() (varios cambios): 
auto.update({"año": 2022, "puertas": 4})
# modifica año y agrega puertas

auto.pop("puertas")
# elimina la clave indicada

auto.popitem()
# elimina el último par insertado

auto.clear()
# vacía el diccionario -> {}

## RECORRER UN DICCIONARIO
for k in auto:
    print(k, auto[k])
    # marca
    # modelo
    # año

    for v in auto.values():
        print(v)
        # Renault
        # Clio
        # 2025

        for key, value in auto.items():
            print(key, value)
            # marca Renault
            # modelo Clio
            # año 2025

       ##DICCIONARIOS ANIDADOS 
        familia = {
           "hijo1": {"nombre": "Pedro", "edad": 8},
            "hijo2": {"nombre": "Ana", "edad": 7},
            "hijo3": {"nombre": "Marcelo", "edad": 6}
       }

    print(familia["hijo1"]["nombre"])