#FUNCIONES PARAMETRIZADAS
#Ejercicio 1
def saludar(nombre):
    return f"Hola {nombre}, bienvenido a Python"
print(saludar("Joaquin"))

#PASO DE PARAMETROS POSICIONALES
def sumar(a,b):
    return a+b
reusltado= sumar(5,3)
print(reusltado)

#PASO DE ARGUMENTOS DE PALABRA CLAVE
def mostrar_info(nombre,edad):
    return f"Nombre: {nombre}, Edad: {edad}"
print(mostrar_info(edad=20,nombre="Joaquin"))

#PALABRAS CLAVE Y ARGUMENTOS POSICIIONALES
def calcular_area(base,altura,unidad="metros"):
    return f"El area del rectangulo es {base*altura} {unidad} cuadrados"
area= calcular_area(5,3)
print("El area del rectangulo es:",area)

#USO DE VALORES PREDEERMINADOS Y ARGUMENTOS VARIBALES 
def mostrar_detalles(nombre, *hobbies, **datos_adicionales):
    detalles = f"{nombre} tiene los siguientes hobbies: {', '.join(hobbies)}. "
    detalles += "Además, tiene los siguientes datos adicionales: "
    detalles += ', '.join([f"{k}: {v}" for k, v in datos_adicionales.items()])
    return detalles

detalles=mostrar_detalles(
    "Joaquin",
    "leer",
    "jugar videojuegos",
    edad=20,
    ciudad="CDMX",
    telefono="5555555555"
)
print("Detalles completos:",detalles)
