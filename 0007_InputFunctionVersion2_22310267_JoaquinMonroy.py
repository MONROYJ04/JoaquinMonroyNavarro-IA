#Este programa es una practica de como usar la funcion input en python
primer_nomrbre= input("¿Cual es tu primer nombre?")
primer_apellido= input("¿Cual es tu primer apellido?")
#Se imprime el nombre y el apellido que ingreso el usuario
print("\nTu nombre es"" "+primer_nomrbre+" "+primer_apellido+"\n")

#Se imprime una linea decorativa
print("°"+10*"_"+"°\n")

#Se solicita al usuario que ingrese su peso y su estatura
a= input("¿Cual es tu peso en kg?")
b= input("¿Cual es tu estatura en metros?")
#Se calcula el indice de masa corporal (IMC) y se imprime el resultado
print("El resultado de su IMC es: "+str(round(float(a)/float(b)**2,2))+"\n")

#Solicita al usuario que ingrese un valor para x y lo convierte a float
x = float(input("Enter value for x: "))
#Calcula el valor de y y lo imprime
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)


#Solicita al usuario la duracion de una pelicula y la hora de inicio
hora = int (input("¿A que hora empieza la pelicula?"))
minuto = int (input("¿A que minuto empieza la pelicula?"))
duracion = int (input("¿Cual es la duracion de la pelicula?"))
#Calcula la hora de finalizacion de la pelicula y la imprime
minuto= minuto + duracion
hora= hora + minuto // 60
minuto= minuto % 60
hora= hora % 24
#Se imprime la hora de finalizacion de la pelicula
print(hora, ":", minuto, sep="  ")


