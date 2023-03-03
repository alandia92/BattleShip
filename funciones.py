import numpy as np

#TABLERO
# tamaño_tablero = 10
# tablero = np.full((10,10), " ")

def crear_tablero():
    tablero = np.full((10,10), " ")
    return tablero

#COLOCAR BARCO
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
                # verificar si el barco se solapa o es adyacente a otros barcos
                # np.any comprueba si hay algun elemento en el rango tablero[] que no sea espacio en blanco
                # si es true, si hay algun elemento que no es e blanco pasa a continue y omite cualquier codigo que sigue de el
                # continue salta a la siguiente iteracion del bucle
                # Cada if comprueba una cosa son independientes uno de otro
                # Todas las comprobaciones se realizan si o si
                if np.any(tablero[fila_inicial, columna_inicial:columna_inicial+longitud] != " "):
                    continue
                if fila_inicial > 0:
                    if np.any(tablero[fila_inicial-1, columna_inicial:columna_inicial+longitud] != " "):
                        continue
                if fila_inicial < 9:
                    if np.any(tablero[fila_inicial+1, columna_inicial:columna_inicial+longitud] != " "):
                        continue
                if columna_inicial > 0:
                    if np.any(tablero[fila_inicial, columna_inicial-1:columna_inicial+longitud+1] != " "):
                        continue
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
                # verificar si el barco se solapa o es adyacente a otros barcos
                if np.any(tablero[fila_inicial:fila_inicial+longitud, columna_inicial] != " "):
                    continue
                if columna_inicial > 0:
                    if np.any(tablero[fila_inicial:fila_inicial+longitud, columna_inicial-1] != " "):
                        continue
                if columna_inicial < 9:
                    if np.any(tablero[fila_inicial:fila_inicial+longitud, columna_inicial+1] != " "):
                        continue
                if fila_inicial > 0:
                    if np.any(tablero[fila_inicial-1:fila_inicial+longitud+1, columna_inicial] != " "):
                        continue
                if fila_inicial+longitud < 10:
                    if np.any(tablero[fila_inicial:fila_inicial+longitud+1, columna_inicial] != " "):
                        continue
                # si la posición es válida, colocar el barco en el tablero
                tablero[fila_inicial:fila_inicial+longitud, columna_inicial] = "O"
                break

    return tablero


#DISPARAR
# No se como gestionar tablero_adversario
def disparar(tablero_ataque, tablero_enemigo, fila, columna):


    if tablero_enemigo[fila, columna] == "O":
        # acierto, colocar una X
        tablero_ataque[fila, columna] = "X"
        tablero_enemigo[fila, columna] = "X"
        disparando = True
    else:
        # fallo, colocar un punto
        tablero_enemigo[fila, columna] = "_"
        tablero_ataque[fila, columna] = "_"
        # cambiar al otro jugador
        disparando = False
        
    return  disparando

#para que funcione disparar meterlo en una variable para que esa variable tenga return disparando