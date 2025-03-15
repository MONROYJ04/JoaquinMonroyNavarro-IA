#En este codigo usaremos coniciones y condicionales en diferentes casos

#If
numero= int(input("Introduce un numero:"))#Se pide un numero
if numero > 0:
    print("El numero es positivo")

#Else
numero= int(input("Introduce un numero:"))#Se pide un numero
if numero > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

#Elif
numero= int(input("Introduce un numero:"))#Se pide un numero
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print ("El numero es negativo")
else:
    print("El numero es cero")

#Ejercicio 1 de condicional con multiples condiciones
#Se pide un numero
numero= input("Intruduce un numero:")
if 1 <= int(numero) <=100:
    print("El numero esta entre 1 y 100")
else:
    print("El numero no esta entre 1 y 100")

#Ejercicio 2 verficar si un numero es par o impar
numero= int(input("Introduce un numero:"))#Se pide un numero
if numero % 2 == 0: #El % es para sacar el residuo de una division y compara si es igual a 0
    print("El numero es par")
else:
    print("El numero es impar")

#Ejercicio 3 verificar si un año es bisiesto
año= int(input("Introduce un año:"))#Se pide un año
if año % 4 == 0 and año % 100 !=0 or año % 400 == 0:
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")

#Ejercico 4 verificar si un triangulo es equilatero
lado1= float(input("Introduce el primer lado del triangulo:"))#Se pide el primer lado
lado2= float(input("Introduce el segundo lado del triangulo:"))#Se pide el segundo lado
lado3= float(input("Introduce el tercer lado del triangulo:"))#Se pide el tercer lado
if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilatero")
else:
    print("El triangulo no es equilatero")
    
