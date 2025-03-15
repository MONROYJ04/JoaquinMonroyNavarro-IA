#Permite acceder a los elementos de una lista mediante su índice

#Crear una lista
frutas = ["manzana", "pera", "uva", "sandía", "mango"]

#Acceder a los elementos de la lista mediante su índice
print(frutas[0]) #manzana
print(frutas[3]) #sandía
print(frutas[1]) #pera
print(frutas[4]) #mango
print(frutas[2]) #uva

#Los indices negativos son legales
letras=["a","b","c","d","e"]
#Acceder al ultimo elemento de la lista
print(letras[-1]) #e
#Acceder al penultimo elemento de la lista
print(letras[-2])#a
#Acceder al primer elemento usando un indice negativo
print(letras[-len(letras)]) #a


