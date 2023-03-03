import numpy as np
from funciones import*

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)
tablero_ataque_jugador = crear_tablero()
tablero_ataque_maquina = crear_tablero()

disparando = True
partida_continua = True

vidas_jugador = 20
vidas_maquina = 20

while partida_continua:

    print("Campo de batalla\n",tablero_ataque_jugador)
    print("Tu flota\n",tablero_jugador)
    print("-------------------------------------------------------------------")
    if disparando == True:
        # fila = int(input("Elije fila entre 0-9: "))
        # columna = int(input("Elije fila entre 0-9: "))
        fila = np.random.randint(0,10)
        columna = np.random.randint(0,10)
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