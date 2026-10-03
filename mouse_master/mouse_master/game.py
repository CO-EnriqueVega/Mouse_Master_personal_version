from components.players import c_player
from components.tarjetas import tarjeta
from components.structure import header, marcador, limpiar_consola
from components.help_player import resumen, mas_ayuda, most_used_commands
import os

def event_listener(player_response, list_players):
    while player_response == 'listening':
        player_response = input('\n Comando: ').lower()

        if player_response == 'next':
            break
    
        # Ver los progreso del juego
        if player_response == 'status':
            for i in list_players:
                print(i.nombre, i.apellido, i.puntos_restantes, i.estado) 
                player_response = 'listening'
    
        # Revisar ayuda del juego
        elif player_response == 'help':
            resumen()
            player_response = input('\n Presiona "help +" para mas ayuda, "comandos" para ver todos los comandos existentes. \n Comando: ').lower()
            if player_response == 'help +':
                mas_ayuda()
            elif player_response == 'comandos':
                most_used_commands()
                player_response = 'listening'
    
        # Jugador pierde puntos al ser nombrado   
        elif player_response in [f"{j.nombre.lower()} {j.apellido.lower()}" for j in list_players]:
    
            # Buscar el jugador correspondiente
            jugador = next(
                j for j in list_players 
                if f"{j.nombre.lower()} {j.apellido.lower()}" == player_response
                )
    
            confirm = input(
                f'\n Nombrar a "{jugador.nombre} {jugador.apellido}" significa que perderia 1 punto.'
                '\n ¿Estas seguro de querer realizar esta accion? (si / no) \n\t R= '
                ).lower()
    
            if confirm == 'si':
                jugador.perder_puntos(1)
    
        # Abandonar el juego
        elif player_response == 'quit game':
            marcador(list_players)
            break
        
        else:
            print('\n Comando no reconocido. ')
            player_response = 'listening'
        
    return player_response

def start_game():

    limpiar_consola()

    # Muestra el nombre del juego en la parte superior de la pantalla
    header()

    # Ask for number of players
    list_players = []
    while True:
        amount_players = input(' Numero de jugadores: ')
        try:
            amount_players = int(amount_players)
            break
        except ValueError:
            print('\n Escribe un numero válido. \n')
    
    # Create new player, and add to list
    for i in range(amount_players):
        print('\n Jugador ' + str(i + 1))
        nombre = input('\t Primer nombre: ')
        apellido = input('\t Primer apellido: ')

        player = c_player(nombre, apellido)
        list_players.append(player)
    
    # Mostrar jugadores creados
    print("\n===== Lista de jugadores =====")
    print(f"{'Nombre':<10} {'Apellido':<10} {'Puntos':<7} {'Estado':<10}")
    print("-" * 40)
    for jugador in list_players:
        print(f"{jugador.nombre:<10} {jugador.apellido:<10} {jugador.puntos_restantes:<7} {jugador.estado:<10}")
    print('\n\n')

    '''
    Main Loop: bucle que se repite hasta terminar el juego, y el juego solo se puede 
    terminar si el jugador presiona el comando correspondiente, o Ctrl + C
    '''
    # Inicializar parametros
    player_response = 'next'
        
    while True:
        limpiar_consola()

        # Muestra el nombre del juego en la parte superior de la pantalla
        header()
        still_in_game = 0
        
        # Si solo hay un jugador "in game", se utiliza la funcion "marcador"
        for i in list_players:
            if i.estado == 'in game':
                still_in_game += 1
                            
        if still_in_game <= 1:
            marcador(list_players)
            break
        
        if player_response == 'quit game':
            break

        current_index = 0  
        
        # Current player: si un jugador termina su turno, y hay mas de 1 jugador, el juego continua, así que se
        #               la variable "current_player" cambia al siguiente jugador en la lista "list_players"
        while player_response == 'next':

            player_response = 'listening'
            
            # Jugador actual
            current_player = list_players[current_index]
            if current_player.estado == 'game over':
                print(f'\n {current_player.nombre} está eliminado')
            else:
                print('''
# == == == ==  == == == ==  == == == ==  == == == == 
# -- -- -- -- -- --  Nuevo turno   -- -- -- -- -- --  
# == == == ==  == == == ==  == == == ==  == == == ==
                ''')
                print(f'\n Turno de "{current_player.nombre} {current_player.apellido}".')
                print(f'\n Puntos restantes: {current_player.puntos_restantes}')

                player_card = tarjeta()
                print(player_card.mostrar())
                
                # Inicializar parametros
                player_response = 'listening'


            # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
            # -- -- -- -- -- --  Event Listener:  -- -- -- -- -- -- -- -- 
            # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            player_response = event_listener(player_response, list_players)

            if player_response == 'quit game':
                break
            elif player_response != 'quit game':
                # Pasar al siguiente jugador
                current_index = (current_index + 1) % len(list_players)
    
    return 0