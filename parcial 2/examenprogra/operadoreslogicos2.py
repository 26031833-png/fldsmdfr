señal_del_router = 67
tienes_Datos = True
tiene_buena_conexion = False

if señal_del_router >= 67 and tienes_Datos:
    print ("cumple ambas condiciones")

if señal_del_router >= 67 or tiene_buena_conexion:
    print("cumple al menos una condicion")

if not tiene_buena_conexion:
    print("no puede ver tiktoks de el campeon")