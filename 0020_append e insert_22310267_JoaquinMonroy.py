#Se aprendera la diferencia entre append e insert en listas

#Append
#El metodo append agrega un elemento al final de la lista
#Crear una lista
frutas=["manzana","pera"]

#Agregar un elemento a la lista
frutas.append("platano")
print(frutas,"\n")

#Insert
#El metodo insert agrega un elemento en la posicion que se le indique
numeros= [10,20,30,40,50]

#Agregar un elemento en la posicion 2
numeros.insert(2,25)
print(numeros,"\n")

#Ejecicio combinado 
colores=["rojo","azul","verde"]
colores.append("amarillo")
print(colores)

colores.insert(1,"morado")
print(colores)

#Ejemplo practico
tareas=["Estudiar","Trabajar","Dormir"]
tareas.append("Comer")
print(tareas,"\n")

tareas.insert(2,"Ejercitarse")
print(tareas,"\n")

