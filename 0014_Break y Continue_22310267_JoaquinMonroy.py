#Uso de las sentencias break y continue en diversos casos

#Ejemplo 1 uso del break para salir del bucle 
for i in range(1, 11):
    if i == 5:
        print("Se ha encontrado el número 5")
        break
    print(i)

#Ejemplo 2 uso del continue para saltar una iteración
for i in range(1, 11):
    if i %2 == 0:
        continue
    print(i)
print()


#Ejemplo 3 uso del break y continue juntos
for i in range(1,14):
    if i > 8:
        break 
    if i % 3 == 0: #Si el número es divisible entre 3, se salta la iteración
        continue
    print(i)
print()



#Ejemplo 4 uso del continue para imprimir vocales 
texto="Hola mundo"
vocales="aeiou"
for caracater in texto:
    if caracater in vocales:
        continue
    print(caracater)
print()

#Ejemplo 5 uso del break en bucle infinito
while True:
    numero=int(input("Ingrese un número: "))
    if numero == 0:
        print("Saliendo del bucle")
        break
    print(f"El número ingresado es: {numero}")


