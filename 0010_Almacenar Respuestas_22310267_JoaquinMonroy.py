#Solicitar al usuario las edades de Pablo y Pedro 
edad_pablo = input("Introduce la edad de Pablo: ")
edad_pedro = input("Introduce la edad de Pedro: ")
#Comparar las edades y alamacenar el resultado en una variable
if edad_pablo > edad_pedro:
    resultado = "Pablo es mayor que Pedro"
elif edad_pablo < edad_pedro:
    resultado = "Pedro es mayor que Pablo"
else:  
    resultado = "Pablo y Pedro tienen la misma edad"
#Imprimir el resultado
print(resultado)
