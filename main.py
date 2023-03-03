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

    print("Campo de batalla\n",tablero_ataque_jugador)
    print("Tu flota\n",tablero_jugador)
    print("-------------------------------------------------------------------")
    if disparando == True:
        fila = int(input("Elije fila entre 0-9: "))
        columna = int(input("Elije fila entre 0-9: "))
        disparando = disparar(tablero_ataque_jugador,tablero_maquina,fila,columna)
        
    else:
        fila = np.random.randint(0,9)
        columna = np.random.randint(0,9)
        disparando = disparar(tablero_ataque_maquina,tablero_jugador,fila,columna)

    # for i in range(len(tablero_jugador)):
    #     if i == "O":
    #         partida_continua = True
    #         break
    #     if i != "O":
    #         partida_continua = False
    # if partida_continua == False:
    #     print("Has perdido!")

    # for i in range(len(tablero_maquina)):
    #     if i == "O":
    #         partida_continua = True
    #         break
    #     if i != "O":
    #         partida_continua = False

    # if partida_continua == False:
    #     print("Has ganado!")