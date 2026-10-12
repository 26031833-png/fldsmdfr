
# calcular el precio de un producto

producto = input("Ingresa el nombre del producto: ")

precio = float(input("Ingresa el precio del producto: "))

cantidad = int(input("¿Cuantos productos quieres comprar? "))

total = precio * cantidad

# Convertir el total a texto
total_texto = str(total)

print("Producto:", producto)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total a pagar:", total_texto)
