from funciones import*

# Creación de cada tablero
tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()
# Colocación de los barcos
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)
# Crear el tablero donde se va a atacar
tablero_ataque_jugador = crear_tablero()
tablero_ataque_maquina = crear_tablero()

# Disparando gestiona los turnos del jugador y el contrincante. True: jugador, False: maquina
disparando = True
# Partida continua para saber si entrar en el bucle de jugar la partida o no.
partida_continua = True

vidas_jugador = 20
vidas_maquina = 20