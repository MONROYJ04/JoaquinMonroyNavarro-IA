#Definicion de variables
a=10
b=5
#Calculo de la hipotenusa
c=(a**2+b**2)**0.5
#Impresion de la hipotenusa
print("c=",c,"\n")

#Se declaran variables y se les asigna un valor
Josue=10
Braulio=5
Carlos=6
#Se imprime el valor de las variables Josue, Braulio y Carlos
print("Josue=",Josue,"Braulio=",Braulio,"Carlos=",Carlos,sep=",")

#Calculo del total de manzanas multiplicando las variables Josue, Braulio y Carlos
total_manzanas=Josue*Braulio*Carlos
print("total_manzanas=",total_manzanas,"\n")
#Incremento de la variable Carlos en 5
Carlos +=5
print("Carlos=",Carlos) #Se imprime el valor de la variable Carlos


# Definicion de variables pies y pulgadas
pies=1.0
pulgadas=12.0

#Calculo de pies a pulgadas y de pulgadas a pies
pies_a_pulgadas=pies*pulgadas
pulgasdas_a_pies=pies/pulgadas

#Impresion de los resultado usando la funcion round para redondear los valores
print(pies,"pies es",round(pies_a_pulgadas), "pulgadas")
print(pulgadas,"pulgadas es",round(pulgasdas_a_pies), "pies")
