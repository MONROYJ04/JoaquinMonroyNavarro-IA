#Crear una lista
frutas=["manzana","pera","uva","sandia","melon"]

#Verificar si un elemento esta en la lista
print("¿banana esta en la lista de frutas?")
if "banana" in frutas:
    print("Banana si esta en la lista")
else:
    print("Banana no esta en la lista")

#Verificar si un elemento no esta en la lista
print("¿manzana no esta en la lista de frutas?")
if "manzana" not in frutas:
    print("Manzana no esta en la lista")
else:
    print("Manzana si esta en la lista")

#Usamos in de forma mas compleja
print("\n uva o pera esta en la lista de frutas?")
if "uva" in frutas or "pera" in frutas:
    print("Uva si esta en la lista o pera si esta en la lista")
else:
    print("No se cumple la condicion")

#Usamos not in de forma mas compleja 
print("\n uva o naranja esta en la lista de frutas?")
if "uva" in frutas and "naranja" not in frutas:
    print("Uva esta en la lista pero naranja no")
else:
    print("No se cumple la condicion")
    
#Usar in en lista vacia 
lista_vacia=[]
print("\n¿manzana esta en la lista vacia?")
if "manzana" in lista_vacia:
    print("Manzana si esta en la lista")
else:
    print("Manzana no esta en la lista")

#Usar not para filtrar elementos de una lista
print("\nFrutas que no son uva")
for fruta in frutas:
    if fruta not in "uva":
        print(fruta)
        