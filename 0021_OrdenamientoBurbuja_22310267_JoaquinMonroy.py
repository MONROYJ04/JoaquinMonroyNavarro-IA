def ordenamiento_burbuja(lista):
    #Coseguir la longitud de la lista
    n=len(lista)

    #Recorrer la lista n-1 veces
    for i in range(n):
        #Una bandera para identificar si hubo cambios en el recorrido
        cambios=False

        #Recorrer la lista de 0 a n-i-1
        for j in range(0,n-i-1):
            #Si el elemento actual es mayor que el siguiente
            if lista[j]>lista[j+1]:
                #Intercambiar los elementos
                lista[j],lista[j+1]=lista[j+1],lista[j]
                #Marcar que hubo cambios
                cambios=True
        #Si no hubo cambios, entonces la lista ya esta ordenada
        if not cambios:
            break 

#Crear una lista desordenada
numeros=[78,41,3,23,98,11]
#Llamar a la funcion
ordenamiento_burbuja(numeros)
print("Lista ordenada:",numeros)



