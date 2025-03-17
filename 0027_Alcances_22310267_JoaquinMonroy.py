#se abordara sobre variables locales y globales
#Funciones y sus alcances
#En Python, una variable declarada dentro de una funcion es una variable local
#Una variable declarada fuera de una funcion es una variable global
def funcion_alcance():
    variable_local = "Soy una variable local"
    print(variable_local)

funcion_alcance()

variable_global = "Soy una variable global"
def modificar_variable_global():
    global variable_global
    variable_global = "Modificando variable global"

print("Antes de modificar la variable global:", variable_global)
modificar_variable_global()

print("Después de modificar la variable global:", variable_global)


#Como Interactuan
def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

mi_lista=[1,2,3]
print("Lista original:", mi_lista)

modificar_lista(mi_lista)
print("Lista después de llamar a la función:", mi_lista)

#Las funciones no pueden modificar objetos inmutables pasados como argumentos
def modificar_entero(entero):
    entero += 10
    print("Dentro de la función:", entero)

mi_entero = 5
print("Entero original:", mi_entero)

modificar_entero(mi_entero)
print("Entero después de llamar a la función:", mi_entero) 
