#En esta practica usaremos los operadores para diversos casos 

#Igualdad
print(5 == 5,"\n") 

#Desigualdad
print(5 != 5,"\n")

#Mayor que
print(5 > 25)
print(25 > 5,"\n")

#Menor que
print(15.6666 < 15.6667)
print(15.6667 < 15.6666,"\n")

#Mayor o igual que
print(5 >= 5)
print(5 >= 4,"\n")

#Menor o igual que
print(5 <= 5)
print(5 <= 6,"\n")

#Ejericio 
edad_pablo=input("Introduce la edad de Pablo: ")#Se pide la edad de Pablo
edad_pedro=input("Introduce la edad de Pedro: ")#Se pide la edad de Pedro
#Se comparan las edades y se imprime el resultado
if edad_pablo > edad_pedro:
    print("Pablo es mayor que Pedro")
elif edad_pablo < edad_pedro:
        print("Pedro es mayor que Pablo")
else:
    print("Pablo y Pedro tienen la misma edad")
    
