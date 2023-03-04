import numpy as np
from funciones import*
from variables import*

while partida_continua:

    print("Campo de batalla\n",tablero_ataque_jugador)
    print("Tu flota\n",tablero_jugador)
    print("-------------------------------------------------------------------")
    if disparando == True:
        fila = None
        columna = None
        while fila is None or columna is None:
            try:
                fila = int(input("Elije fila entre 0-9: "))
                columna = int(input("Elije columna entre 0-9: "))
                if not (0 <= fila <= 9) or not (0 <= columna <= 9):
                    print("Tienes que elegir un número entre 0-9")
                    fila = None
                    columna = None
            except ValueError:
                print("Tienes que elegir un número entre 0-9")
                fila = None
                columna = None
        disparando = dispararJugador(tablero_ataque_jugador,tablero_maquina,fila,columna)
        if disparando == True:
            vidas_maquina -= 1
    else:
        fila = np.random.randint(0,10)
        columna = np.random.randint(0,10)
        disparando = dispararMaquina(tablero_ataque_maquina,tablero_jugador,fila,columna)
        if disparando == False:
            vidas_jugador -= 1
    print(f"Te quedan {vidas_jugador} vidas y a tu contrincante {vidas_maquina} vidas")
    if vidas_jugador == 0:
        partida_continua = False
        print("Has perdido!")
    if vidas_maquina == 0:
        partida_continua = False
        print("Has ganado!")