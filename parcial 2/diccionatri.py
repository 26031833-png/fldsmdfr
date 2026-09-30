taquerias = {

"Taqueria1" : {
    "nombre" : "tacos el toño",
    "empleados" : 5,
    "platillos" : ["combo 2"]
 },
"Taqueria2" : {
 "nombre" : "tacos el bajito",
   "empleados" : 14,
    "platillos" : ["combo 1"]
}
}

for clave,info in taquerias.items():
   print(f"numero de taqueria {clave}")
   print(f"Nombre: {info['nombre']}\n")
