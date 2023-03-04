import numpy as np


def crear_tablero():
    tablero = np.full((10,10), " ")
    return tablero

def colocar_barcos(tablero):
    # longitud de los barcos
    barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] 

    # bucle para colocar cada barco
    for longitud in barcos:
        # bucle para generar una posición y orientación válidas
        while True:
            # elegir aleatoriamente una orientación horizontal o vertical
            orientacion = np.random.choice(["horizontal", "vertical"])
            if orientacion == "horizontal":
                # generar una posición aleatoria para la fila y la columna inicial
                fila_inicial = np.random.choice(np.arange(10))
                columna_inicial = np.random.choice(np.arange(10 - longitud + 1))

                # verifica si algún elemento en la fila fila_inicial y las columnas columna_inicial hasta columna_inicial+longitud no es un espacio en blanco.
                # si encuentra algún elemento que no sea un espacio en blanco
                # la declaración continue salta a la siguiente iteración del bucle while y comienza a buscar una nueva posición
                if np.any(tablero[fila_inicial, columna_inicial:columna_inicial+longitud] != " "):
                    continue
                # verifica si el barco se solapa o es adyacente a otros barcos con fila inicial > 0 y < 9.
                # Si encuentra un solapamiento, continue pasará a la siguiente iteración del bucle para buscar un nuevo sitio
                if fila_inicial > 0:
                    if np.any(tablero[fila_inicial-1, columna_inicial:columna_inicial+longitud] != " "):
                        continue
                if fila_inicial < 9:
                    if np.any(tablero[fila_inicial+1, columna_inicial:columna_inicial+longitud] != " "):
                        continue
                # comprobación a la izquierda
                if columna_inicial > 0:
                    if np.any(tablero[fila_inicial, columna_inicial-1:columna_inicial+longitud+1] != " "):
                        #desde la posición una columna a la izquierda de la posición inicial hasta la posición una columna a la derecha del final del barco == True continua
                        continue
                # comprobación a la derecha. Comprueba si la posición final del barco más 1 no supera el ancho del tablero
                if columna_inicial+longitud < 10:
                    if np.any(tablero[fila_inicial, columna_inicial:columna_inicial+longitud+1] != " "):
                        continue
                # si la posición es válida, colocar el barco en el tablero
                tablero[fila_inicial, columna_inicial:columna_inicial+longitud] = "O"
                break
            else:  
                # orientacion == "vertical"
                fila_inicial = np.random.choice(np.arange(10 - longitud + 1))
                columna_inicial = np.random.choice(np.arange(10))
                # verificar si el barco se solapa o es adyacente a otros barcos en la posicion vertical
                if np.any(tablero[fila_inicial:fila_inicial+longitud, columna_inicial] != " "):
                    continue
                # verificar si el barco se solapa o es adyacente a otros barcos a la izquierda
                if columna_inicial > 0:
                    if np.any(tablero[fila_inicial:fila_inicial+longitud, columna_inicial-1] != " "):
                        continue
                # verificar si el barco se solapa o es adyacente a otros barcos a la derecha
                if columna_inicial < 9:
                    if np.any(tablero[fila_inicial:fila_inicial+longitud, columna_inicial+1] != " "):
                        continue
                # verificar si el barco se solapa o es adyacente a otros barcos arriba
                if fila_inicial > 0:
                    if np.any(tablero[fila_inicial-1:fila_inicial+longitud+1, columna_inicial] != " "):
                        continue
                # verificar si el barco se solapa o es adyacente a otros barcos a la abajo
                if fila_inicial+longitud < 10:
                    if np.any(tablero[fila_inicial:fila_inicial+longitud+1, columna_inicial] != " "):
                        continue
                # si la posición es válida, colocar el barco en el tablero
                tablero[fila_inicial:fila_inicial+longitud, columna_inicial] = "O"
                break

    return tablero


def dispararJugador(tablero_ataque, tablero_enemigo, fila, columna):
    if tablero_enemigo[fila, columna] == "X" or tablero_enemigo[fila, columna] == "_":
        print("Has disparado al mismo sitio, tonto!, vuelve a intentarlo!")
        disparando = True
    if tablero_enemigo[fila, columna] == "O":
        # acierto, colocar una X
        tablero_ataque[fila, columna] = "X"
        tablero_enemigo[fila, columna] = "X"
        disparando = True
        print("Has acertado!")
    if tablero_enemigo[fila, columna] == " ":
        # fallo, colocar una barra baja
        tablero_enemigo[fila, columna] = "_"
        tablero_ataque[fila, columna] = "_"
        # cambiar al otro jugador
        disparando = False
        print("OOOH! Has fallado!")
    return  disparando

def dispararMaquina(tablero_ataque, tablero_enemigo, fila, columna):
    if tablero_enemigo[fila, columna] == "X" or tablero_enemigo[fila, columna] == "_":
        disparando = False
    if tablero_enemigo[fila, columna] == "O":
        # acierto, colocar una X
        tablero_ataque[fila, columna] = "X"
        tablero_enemigo[fila, columna] = "X"
        disparando = False #ataca cuando es false
        print("Te han dado!")
    if tablero_enemigo[fila, columna] == " ":
        # fallo, colocar una barra baja
        tablero_enemigo[fila, columna] = "_"
        tablero_ataque[fila, columna] = "_"
        # cambiar al otro jugador
        disparando = True
        print("AGUA")
    return  disparando
