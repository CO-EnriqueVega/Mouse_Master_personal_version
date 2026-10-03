import os

def header():
    print('''
*********** *********** *********** ***********
\n 
***********      Mouse Maestro      ***********
\n 
*********** *********** *********** ***********
        ''')

def marcador(list_players):
    print('''
 ==== ====  ==== ====  ==== ====  ==== ====
\n ==== ====     Marcador Final  ==== ====
\n ==== ====  ==== ====  ==== ====  ==== ====
''')
    for jugador in list_players:
        print(f' {jugador.nombre} {jugador.apellido} - Puntos restantes: {jugador.puntos_restantes}, Estado: {jugador.estado}')

    # Buscar ganador
    ganadores = [j for j in list_players if j.estado == 'in game']
    if len(ganadores) == 1:
        ganador = ganadores[0]
        if os.name == 'nt':
                os.system('cls')
                os.system('cls')
        else:
            os.system('clear')
            os.system('clear')
        print("\n !!!!! GANADOR !!!!!")
        print(f'{ganador.nombre} {ganador.apellido} con {ganador.puntos_restantes} puntos')
    else:
        print('\n No hubo un único ganador.')

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
        os.system('cls')
    else:
        os.system('clear')
        os.system('clear')