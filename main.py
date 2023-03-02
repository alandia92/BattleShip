import numpy as np
from funciones import*
from variables import*
# Hay que hacer algo con los tableros imprimirpor pantalla, no se como
# No se como hacer que cambie de jugador ->  haciendo que no sea 1
# Pero luego no se como hacer que vuelva a ser otra vez el jugador
disparando = True
jugador = 1
vidas = 20
# Con las vidas igual puedo hacer el cambio de turno
while disparando:
    if jugador == 1:
        fila = int(input("Elije fila entre 0-9: "))
        columna = int(input("Elije fila entre 0-9: "))
        es_maquina = False
    else:
        fila = None
        columna = None
        es_maquina = True

    # realizar disparo al tablero del adversaio
    # Tengo que gestionar tablero del adversaro de alguna manera
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