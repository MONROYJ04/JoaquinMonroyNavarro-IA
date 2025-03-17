#Aprenderemos a usar diccionarios y tuplas

#Crear una tupla
estudiantes=("Joaquin","Jose","Luis","Maria","Ana")

#Crear un diccionario con infromacion de los estudiantes
diccionario={
    "Joaquin":(20,"Masculino","Soltero"),
    "Jose":(21,"Masculino","Casado"),
    "Luis":(22,"Masculino","Soltero"),
    "Maria":(19,"Femenino","Soltera"),
    "Ana":(20,"Femenino","Soltera")
}

#Recorrer la tupla y mostrar los datos de los estudiantes
for estudiante in estudiantes:
    if estudiante in diccionario:
        datos=diccionario[estudiante]#Obtener los datos del estudiante
        print(f"{estudiante} tiene {datos[0]} años, es {datos[1]} y es {datos[2]}.")
    else:
        print(f"No se encontro informacion de {estudiante}.")
        
#Agregar un nuevo estudiante
nuevo_estudiante="Pedro"
estudiantes+=(nuevo_estudiante,)
diccionario[nuevo_estudiante]=(20,"Masculino","Soltero")

#Mostrar la informacion actualizada
print("\nInformacion actualizada de los estudiantes:")
for estudiante in estudiantes:
    if estudiante in diccionario:
        datos=diccionario[estudiante]#Obtener los datos del estudiante
        print(f"{estudiante} tiene {datos[0]} años, es {datos[1]} y es {datos[2]}.")
    else:
        print(f"No se encontro informacion de {estudiante}.")

#Modificar informacion del diccionario
diccionario["Joaquin"]=(25,"Masculino","Casado")

#Mostrar la informacion actualizada
print("\nInformacion actualizada de los estudiantes:")
for estudiante in estudiantes:
    if estudiante in diccionario:
        datos=diccionario[estudiante]#Obtener los datos del estudiante
        print(f"{estudiante} tiene {datos[0]} años, es {datos[1]} y es {datos[2]}.")
    else:
        print(f"No se encontro informacion de {estudiante}.")

#Eliminar un estudiante
del diccionario["Jose"]

#Mostrar despues de eliminar
print("\nInformacion actualizada de los estudiantes:")
for estudiante in estudiantes:
    if estudiante in diccionario:
        datos=diccionario[estudiante]#Obtener los datos del estudiante
        print(f"{estudiante} tiene {datos[0]} años, es {datos[1]} y es {datos[2]}.")
    else:
        print(f"No se encontro informacion de {estudiante}.")
