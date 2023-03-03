import numpy as np
from funciones import*
from variables import*

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)
tablero_ataque_jugador = crear_tablero()
tablero_ataque_maquina = crear_tablero()

disparando = True
partida_continua = True


while partida_continua:

    print(tablero_ataque_jugador)

    if disparando == True:
        fila = int(input("Elije fila entre 0-9: "))
        columna = int(input("Elije fila entre 0-9: "))
        disparando = disparar(tablero_ataque_jugador,tablero_maquina,fila,columna)
        
    else:
        fila = np.random.randint(0,9)
        columna = np.random.randint(0,9)
        disparando = disparar(tablero_ataque_maquina,tablero_jugador,fila,columna)

    if np.any(tablero_jugador != "O" | tablero_maquina != "O"):
            partida_continua = False

if np.any(tablero_jugador != "O"):
    print("Has perdido!")
else:
     print("Has ganado!")
