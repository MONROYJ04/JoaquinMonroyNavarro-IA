#Realizaremos casos que expliquen el uso de funciones y metodos en python

#Funciones
#Una funcion es un bloque de codigo que solo se ejecuta cuando se llama
#Definir una funcion 
def saludar(nombre):
    return f"Hola {nombre}"

#Llamar a la funcion
mensaje = saludar ("Joaquin")
print(mensaje, "\n")

#Metodos
#Un metodo es una funcion que pertenece a un objeto
texto= "Hola Mundo"
texto_mayusculas= texto.upper()#El metodo upper convierte el texto a mayusculas
print(texto_mayusculas) 