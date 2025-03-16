#Crear lista anidada
lista_anidada= [[1,2,3],[4,5,6],[7,8,9]]

#Imprimir lista anidada
print("lista_anidada completa:")
for sublista in lista_anidada:
    print(sublista)

#Verificar si un elemento esta en la lista anidada
elemento= lista_anidada[0][1] 
print("\nEl segundo elemento de la primer sublista es:",elemento)

#Modificar un elemento de la lista anidada
lista_anidada[0][1]= 20
print("\nLa lista anidada despues de modificar:")
for sublista in lista_anidada:
    print(sublista)

#Agregar una nueva sublista
nueva_sublista=[10,11,12]
lista_anidada.append(nueva_sublista)
print("\nLa lista anidada despues de agregar una nueva sublista:")
for sublista in lista_anidada:
    print(sublista)

#Eliminar una sublista
lista_anidada.pop(1)
print("\nLa lista anidada despues de eliminar la segunda sublista:")
for sublista in lista_anidada:
    print(sublista)

