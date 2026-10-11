
frutas = {"manzana", "naranja", "mandarina", "naranja"}     
print(frutas) 
print(type(frutas))
print(len(frutas))

#verificar elementos
frutas = {"manzana", "naranja", "mandarina"}
print("manzana" in frutas)
print("pera" not in frutas)

#add
frutas = {"manzana", "naranja"}
frutas.add("pera")
print(frutas)

#update
frutas_tropicales = {"piña", "mango"}   
frutas.update(frutas_tropicales)
print(frutas)

#remove
s = {1, 2, 3}
s.remove(2)
print(s) 

#discard
s = {1, 2, 3}
s.discard(5)
print(s) 

#pop
s = {1, 2, 3}
s.pop()
print(s) 

#clear
s = {1, 2, 3}
s.clear()
print(s)

#operaciones entre conjuntos
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
#union
set1.union(set2)
#interseccion
set1.intersection(set2)
#diferencia
set1.difference(set2)

#eliminar diplicados
lista = {1, 2, 2, 2, 3, 4}
set(lista)
lista_limpia = list(set(lista))
lista_limpia