import numpy as np
from funciones import*
from variables import*
# Hay que hacer algo con los tableros imprimirpor pantalla, no se como
# No se como hacer que cambie de jugador ->  haciendo que no sea 1
# Pero luego no se como hacer que vuelva a ser otra vez el jugador
disparando = True
jugador = 1
while disparando:
    if jugador == 1:
        fila = int(input("Elije fila entre 0-9: "))
        columna = int(input("Elije fila entre 0-9: "))
        es_maquina = False
    else:
        fila = None
        columna = None
        es_maquina = True

    