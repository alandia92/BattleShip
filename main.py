import numpy as np
from funciones import*
from variables import*

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)
# Hay que hacer algo con los tableros imprimirpor pantalla, no se como
# No se como hacer que cambie de jugador ->  haciendo que no sea 1
# Pero luego no se como hacer que vuelva a ser otra vez el jugador
disparando = True
partida_continua = True

# tablero jugador, tablero maquina
# def jugar
# mientras jugador dispara y acierta, que siga jugando si no acierta brak para que juegue la maquina
# turnos con par e impar
# Con las vidas igual puedo hacer el cambio de turno, igual tambien hasta que no queden "O", con tres while(tabero maquina,) while dispara(acierta vuelva si no break),otro?
while partida_continua:
    if disparando == 1:
        fila = int(input("Elije fila entre 0-9: "))
        columna = int(input("Elije fila entre 0-9: "))
        
    else:
        fila = 
        columna = 
        

    # realizar disparo al tablero del adversaio
    # Tengo que gestionar tablero del adversaro de alguna manera, igual no hace falta con la variabe es_maquina
    pum = disparar(tablero_adversario, fila, columna, es_maquina)

    # acertamos o no y se reduce las vidas
    if not pum: 
        vidas -=1
        print(f"Has fallado! Te quedan {vidas} vidas")
        if vidas == 0:
            # Gestionar jugadores
            print(f"El jugador {x} a perdido")
            disparando = False
            break
    else:
        print("Acertaste!")
    
    # verificar si el juego a terminado
    # No se como, igual una funcion nueva. disparando seria false

    # cambiar al otro jugador
    # igual con pum acierto o no acierto
            if np.any(tablero_enemigo == "O"):
            # quedan barcos, sigue disparando
            partida_continua = True
        else:
            # no quedan barcos, el juego ha terminado
            partida_continua = False