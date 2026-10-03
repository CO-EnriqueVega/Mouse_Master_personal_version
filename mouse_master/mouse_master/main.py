from game import start_game
from components.help_player import resumen

def main():
    # Titulo, Instrucciones y reglas
    resumen()

    # Pregunta al usuario comenzar el juego
    power = input(' Empezar "Mouse maestro": si(escribe "on") o no(escrbibe "off"). \n Power: ').lower()
    while True:
        if power == 'on':
            start_game()
            power = input(' Volver a jugar: si(escribe "on") o no(escrbibe "off"). \n Power: ').lower()
        elif power == 'off':
            print('''
*********** *********** *********** ***********
\n 
*********** Programa terminado      ***********
\n 
*********** *********** *********** ***********
            ''')
            break
        else:
            power = input('\n\n Intenta de nuevo. \n Escribe "on" para jugar, o "off" para salir del programa. \n Power: ').lower()


if __name__ == "__main__":
    main()
