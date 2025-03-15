#Se hara uso del ciclo for en diferentes casos

#Ejemplo 1 imprimir numeros del 1 al 10
for i in range (1,8): #El 1 es el inicio y el 8 es el final
    print(i)

print("\n")

#Ejemplo 2 imprimir numeros pares del 1 al 10
for i in range (2,11,2): #El 2 es el inicio, el 11 es el final y el 2 es el incremento 
    print(i)
print("\n")

#Ejemplo 3 imprimir una piramide 
altura=5
for i in range(1,altura+1):
    print(" " * (altura-i) + "°" *(2*i-1))
print("\n")

#Ejemplo 4 imprimir una piramide invertida
altura=5
for i in range(altura,0,-1):
    print(" " * (altura-i) + "°" *(2*i-1))
print("\n")