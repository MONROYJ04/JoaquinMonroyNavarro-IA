#Se realizaran operaciones con lista especialmente empleando el metodo de rebanadas

numeros=[10,20,30,40,50,60,70,80,90]
print("Lista original:" , numeros)

#Rebanada start y end
#Extraer elementos de la lsita desde el indice -6 hasta el -2 sin incluirlo
rebanada= numeros[-6:-2]
print("Rebanada [-6:-2]:", rebanada)

#Rebanada con start pero sin end
#Extraer elementos de la lista desde el indice 3 hasta el final
rebanada = numeros[3:]
print("Rebanada [3:]:", rebanada)

#Rebanada sin start pero con end
#Extraer elementos de la lista desde el inicio hasta el indice 4 sin incluirlo
rebanada = numeros[:4]
print("Rebanada [:4]:", rebanada)

#Rebanada con step
#Extraer elementos de la lista desde el indice 1 hasta con paso 2
rebanada = numeros[1::2]
print("Rebanada [1::2]:", rebanada)

#Eliminar una rebanada
#Eliminar elementos de la lista desde el indice 2 hasta el indice 5 sin incluirlo
del numeros[2:5]
print("Lista con elementos eliminados:", numeros)

#Ordenar la lista 
numeros.sort()
print("Lista ordenada:", numeros)

#Invertir la lista
numeros.reverse()
print("Lista invertida:", numeros)



