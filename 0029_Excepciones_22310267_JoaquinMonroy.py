#Errores en diversas situcaiones 

#Dividir por cero
try:
    resultado = 10/0
    print(resultado)

except:
    print("Error al dividir por cero")

#Intentar acceder a un indice que no existe
try:
    lista=[1,2,3]
    print(lista[5])
except:
    print("Error al acceder a un indice que no existe")

#Pedir un numero al usuario y se ingrese un texto
try:
    numero=int(input("Ingrese un numero (escribe una letra): "))
    print(numero)
except ValueError:
    print("Error al ingresar un texto en lugar de un numero")

#Abrir un archivo que no existe
try:
    archivo=open("archivo.txt")
    contenido=archivo.read()
    print(contenido)
except:
    print("Error al abrir el archivo")

#Manejar dos errores dividir por cero y convertir cadena a numero
try:
    numero=int("no es un numero")
    resultado = 10/0
except ValueError:
    print("Error al convertir cadena a numero")
except ZeroDivisionError:
    print("Error al dividir por cero")

#Acceder a una clave que no existe en un diccionario
try:
    diccionario={"clave":"valor"}
    print(diccionario["no existe"])
except KeyError:
    print("Error al acceder a una clave que no existe")

#Asegurar que un mensaje se muestre siempre 
try:
    archivo=open("archivo.txt")
except FileNotFoundError:
    print("Error al abrir el archivo")
finally:
    print("Mensaje de error")

#Depurar errores
def multiplicar(a,b):
    print("Multiplicando",a,"por",b)
    return a*b

resultado=multiplicar(5,2)
print("Resultado:",resultado)

#Excepciones especificas
try:
    resultado=10/0
except ZeroDivisionError as e:
    print(f"Error al dividir por cero: {e}")