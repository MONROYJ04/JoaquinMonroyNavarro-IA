#Operadores logios and , or y not

#and
#Ejemplo 1 verificar si un numero esta dentro de un rango
numero = 10
if numero > 0 and numero < 20:
    print("El numero esta dentro del rango")
else:
    print("El numero no esta dentro del rango")
print()

#Ejemplo 2 verificar si un usuario puede votar 
edad = 17
if edad >= 18 and edad <= 100: #si la edad es mayor o igual a 18 y menor o igual a 100
    print("El usuario puede votar")
else:
    print("El usuario no puede votar")
print()

#or
#Ejemplo 1 verificar si un numero es par o impar
numero = 10
if numero % 2 == 0 or numero % 2 == 1:
    print("El numero es par o impar")
else:
    print("El numero no es par ni impar")
print()

#Ejemplo 2 verifcar si un alumno aprobo o reprobo
calificacion = 5
if calificacion >=6 or calificacion <=5 :#si la calificacion es mayor o igual a 6 o menor o igual a 5
    print("El alumno aprobo")
else:  
    print("El alumno reprobo")
print()

#not
#Ejemplo 1 verificar si un numero no es positivo
numero= input("Ingresa un numero: ")
if not int (numero) > 0:
    print("El numero no es positivo")
else:
    print("El numero es positivo")
print()

#Ejemplo 2 verificar si un usuario es admin 
usuario = "admin"
if not usuario == "admin":
    print("El usuario no es admin")
else:
    print("El usuario es admin")
print()
