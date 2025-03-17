import random

# Función para tablero 
def imprimir_tablero(tablero):
    print("+-------+-------+-------+")
    for row in tablero:
        print("|       |       |       |")
        print("|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    return False

# Función para verificar si hay tablero lleno
def tablero_lleno(tablero):
    for row in tablero:
        if any(isinstance(cell, int) for cell in row):
            return False
    return True

# Función para obtener el movimiento de la maquina
def movimiento_maquina(tablero):
    opciones = [cell for row in tablero for cell in row if isinstance(cell, int)]
    return random.choice(opciones)

# Función principal del juego
def jugar():
    tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    tablero[1][1] = "X"
    imprimir_tablero(tablero)

    while True:
        # Movimiento del jugador
        movimiento = input("Ingresa un numero del 1 al 9: ")
        if movimiento.isdigit():
            movimiento = int(movimiento)
            if 1 <= movimiento <= 9:
                fila = (movimiento - 1) // 3
                columna = (movimiento - 1) % 3

                if isinstance(tablero[fila][columna], int):
                    tablero[fila][columna] = "O"
                else:
                    print("Esa casilla ya esta ocupada, Intenta de nuevo")
                    continue
            else:
                print("Movimiento invalido. Debes ingresar un numero del 1 al 9")
                continue
        else:
            print("Movimiento invalido. Debes ingresar un numero del 1 al 9")
            continue

        # Imprimir tablero después del movimiento del jugador
        imprimir_tablero(tablero)

        # Verificar si el jugador gano
        if verificar_ganador(tablero, "O"):
            print("Felicidades, Ganaste!")
            break

        # Verificar si hay empate
        if tablero_lleno(tablero):
            print("Empate!")
            break

        # Movimiento de la maquina
        movimiento_maquina_valor = movimiento_maquina(tablero)
        print(f"La maquina elige su movimiento en la casilla {movimiento_maquina_valor}")
        fila = (movimiento_maquina_valor - 1) // 3
        columna = (movimiento_maquina_valor - 1) % 3
        tablero[fila][columna] = "X"

        # Imprimir tablero después del movimiento de la maquina
        imprimir_tablero(tablero)

        # Verificar si la maquina gano
        if verificar_ganador(tablero, "X"):
            print("La maquina gano!, Intenta de nuevo")
            break

        # Verificar si hay empate
        if tablero_lleno(tablero):
            print("Empate!")
            break

# Iniciar el juego
jugar()