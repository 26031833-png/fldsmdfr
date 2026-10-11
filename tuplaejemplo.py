tecnologias = ("Python","JavaScript", "Go")
print(tecnologias)  #('Python', 'JavaScript', 'Go')
print(type(tecnologias)) #<class 'tuple'>
print(tecnologias[1]) #JavaScript

#tupla de un solo elemento
fruta = ("manzana","pera")
print (type(fruta))

#Duplicados
t = ("Python","JavaScript", "Go", "Python")
print(len(t))

#tipos mezclados
tupla = ("Python", 5, True)
print(type(tupla))

#empaquetado
x, y, z = tupla
print(type(tupla))

#conectar
tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2
print(tupla3)

#duplicar
tupla = ("A", "B", "C")
print(tupla * 2)

#recorrer con for
colores = ("rojo", "verde", "azul") 
for color in colores:
    print (color)    

#modificar tupla
tupla_a_modificar = ("Python", "JavaScript", "Go")
lista_comodin = list(tupla_a_modificar)
lista_comodin.append("ReactJS")
tupla_a_modificar = tuple(lista_comodin)
print(tupla_a_modificar)
