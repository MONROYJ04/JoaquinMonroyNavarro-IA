primer_nomrbre= input("¿Cual es tu primer nombre?")
primer_apellido= input("¿Cual es tu primer apellido?")
print("\nTu nombre es"" "+primer_nomrbre+" "+primer_apellido+"\n")

print("°"+10*"_"+"°\n")

a= input("¿Cual es tu peso en kg?")
b= input("¿Cual es tu estatura en metros?")
print("El resultado de su IMC es: "+str(round(float(a)/float(b)**2,2))+"\n")


x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

hora = int (input("¿A que hora empieza la pelicula?"))
minuto = int (input("¿A que minuto empieza la pelicula?"))
duracion = int (input("¿Cual es la duracion de la pelicula?"))
minuto= minuto + duracion
hora= hora + minuto // 60
minuto= minuto % 60
hora= hora % 24
print(hora, ":", minuto, sep="  ")


