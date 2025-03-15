#Bucle while

#Ejemplo 1
limite= int(input("Introduce un numero:"))#Se pide un numero
contador= 1
while contador <= limite: #Mientras el contador sea menor o igual al limite
    print(contador,"\n")
    contador +=1 #Esto hace que el contador incremente en 1

#Ejemplo 2 Sumar numeros dados por el usuario
suma = 0
numero= int(input("Introduce un numero (0 es para terminar)"))#Se pide un numero

while numero != 0: 
    suma += numero  #Esto hace que la suma sea igual a la suma mas el numero
    numero = int(input("Introduce otro numero:"))

print(f"La suma de los numeros es {suma}")

#Ejemplo 3 Menu de helados
opcion= 4

while opcion != 3:
    print("\nMenu de helados\n")
    print("1_Vainilla\n")
    print("2_Chocolate\n")
    print("3_Salir\n")

    opcion= int(input("Introduce una opcion:"))
    if opcion == 1:
        print("Vainilla\n")
    elif opcion == 2:
        print("Chocolate\n")
    elif opcion == 3:
        print("Salir\n")
    else:   
        print("Opcion no valida\n")