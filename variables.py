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