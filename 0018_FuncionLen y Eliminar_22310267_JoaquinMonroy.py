#La funcion len() nos permite saber cuantos elementos tiene una lista
#Se eliminaran elementos de una lista con ciertas funciones

#Crear una lista
numeros = [1,2,3,4,5,6,7,8,9,10]
print("Los elementos de la lista son:")
for numero in numeros:
    print(numero)

    #Usar len() para saber cuantos elementos tiene la lista
print(f"La lista tiene {len(numeros)} elementos")

#Crear una lista 
colores = ["rojo","azul","verde","amarillo","naranja"]
print(colores)

#Eliminar un elemento por indice
colores.pop(1)#Elimina el elemento en la posicion 1
print(colores)

#Eliminar usando del
del colores[2]#Elimina el elemento en la posicion 2
print(colores)

#Eliminar con remove
colores.remove("naranja")
print(colores)#["rojo","verde"]
print()

#Ejercicio combinado 
#Crear una lista
paises=["Mexico","Argentina","Brasil","Chile","Peru"]

#1. indexacion de listas
print(paises[0]) #Mexico
print(paises[1]) #Argentina

#2.Usar len() para saber cuantos elementos tiene la lista
print("Todos los paises son:")
for pais in paises:
    print(pais)
print(f"Total de paises: {len(paises)} ")

#3. Eliminar elementos de la lista
paises.remove("Brasil")
print("Despues de eliminar Brasil:",paises)

paises.pop(1)
print("Despues de usar pop(1):",paises) 

del paises[-1]
print("Despues de usar del paises[-1]:",paises)

#4.Mostrar con indices negativos
print("Ultimo pais restante:",paises[-1]) 
print("Primer pais restante:",paises[-len(paises)])

