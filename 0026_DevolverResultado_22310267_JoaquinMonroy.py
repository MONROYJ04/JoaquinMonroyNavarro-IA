def procesar_lista(lista=None):# Se define la función procesar_lista con un parámetro opcional lista
    if lista is None:
        lista=[]

    if len(lista)==0:# Si la lista está vacía, se regresa un mensaje de error
        print("Error: Lista vacía")
    else:
        suma= sum(lista)# Se calcula la suma de los elementos de la lista
        promedio= suma/len(lista)# Se calcula el promedio de los elementos de la lista
        print(f"Suma de los elementos: {suma}")
        print(f"Promedio de los elementos: {promedio}")


print("Llamar a la función sin lista:")
procesar_lista()

print("\nLlamar a la funcion con lista: ")
procesar_lista([1,2,3,4,5,6,7,8,9,10])

print("\nLlamar a la función con lista vacía:")

procesar_lista([])
