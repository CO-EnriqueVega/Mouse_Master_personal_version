from components.structure import header

def resumen():
    header()
    print('''

Reglas:
    •	Las cartas se distinguen por tipos y clases. Tipos son: Verdad, Reto, Castigo o Mouse Maestro. 
        Y clases son: Definida, Libre, Selectiva.
        o	Definida: Las cartas ya muestran un reto, o preguntas de “cierto/falso” establecida.
        o	Libre: Los retos o las preguntas de “cierto/falso” establecida las crea el jugador
    •	Los desafíos o retos impuestos entre jugadores no pueden ser demasiado extremos e ilegales (no 
        sería apropiado, y sería bajo el riesgo de los mismos jugadores, aunque siempre es mejor abandonar 
        el juego cuando eres obligado a hacer algo que no quieres hacer).
    •	Un turno es cuando un jugador obtiene una tarjeta.
    •	Un ciclo es cuando todos los jugadores han jugado la misma cantidad de turnos.

Instrucciones:
    1.	Iniciar juego al establecer los jugadores.
    2.	Cada jugador empieza con 10 puntos, y para sobrevivir, el jugador tiene que intentar no perder 
        puntos.
    3.	Durante el turno de un jugador, ese jugador sacar una carta.
    4.	El jugador que al fallar, incumplir, o negarse a un reto o no cumplir con el castigo, pierde 1 
        punto.
    5.	El jugador que llegue a 0, pierde el juego.
    6.	El último sobreviviente gana.

        ''')

def most_used_commands():
    print('''\n\n
    • "next": otorgar turno al siguiente jugador para sacar una carta. 
    • "status": para revisar el marcador actual del Juego.
    • "help": despliega las reglas e instrucciones.
    • "name last_name": by providing "name" and "last_name", the player as variable will lose 1 point. 
        Since is a pretty big deal, you must confirm that every player agree. Ejemplo de uso: 
        "enrique vega"
    • "quit game": Para salir del juego, escribe "quit", o presiona las teclas "Control + C"
    ''')

def mas_ayuda():
    print(' Visita: _______')