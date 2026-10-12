frutas = ["naranja", "manzana", "banana"]
adjetivos = ["rojo", "verde", "amarillo"]
palabra = "Python"

for letra in palabra:
    print(letra)

for fruta in frutas:
    print(fruta)

    if fruta == "naranja":
        break

    if fruta == "naranja":
        continue 

else:
    print("ya terminó elbucle")

    for adjetivo in adjetivos:
        for fruta in frutas:
            print(fruta, adjetivo)

for i in range(10):
    pass

