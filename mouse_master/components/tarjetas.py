from random import choices, choice

class card:
    def __init__(self, contenido, tipo, clase):
        self.clase = clase              # Ejemplo: "reto" ":"
        self.contenido = contenido      # Ejemplo: "esta prohibido reirse"
        self.tipo = tipo                # Ejemplo: "(todos)"

    def mostrar(self):
        return f'\n [{self.clase.upper()}] ({self.tipo}) \n {self.contenido} \n'

from random import choices, choice

# Ejemplo de MAZO
verdad = [
    'Es cierto o falso que “__________”.'
]

reto = [
    '''1.	Categoría: el jugador que saque esta carta deberá nombrar una categoría (por ejemplo, actores famosos).
        A continuación, cada participante, incluido quien nombró la categoría, mencionará un elemento que pertenezca
        a ella (ejemplo: Keanu Reeves, Demi Lovato, etc.). El reto continúa hasta que alguien no pueda aportar un
        nuevo elemento en menos de 15 segundos.''',
    '''2.	Secuencia de acciones: el jugador que saque esta carta iniciará realizando una acción (por ejemplo,
        aplaudir). El siguiente jugador repetirá todas las acciones anteriores y añadirá una nueva. El reto continúa
        en secuencia, acumulando acciones, hasta que alguien se equivoque o no pueda recordar la secuencia 
        completa.\n''',
    '''3.	Historia: el jugador que saque esta carta iniciará una historia diciendo una palabra (por ejemplo, “El”). 
        El siguiente jugador repetirá todas las palabras anteriores y añadirá una nueva formando una historia. El
        reto se acaba cuando alguien se equivoque.''',
    '''4.	Push up: cada jugador deberá realizar 10 lagartijas. Quien no logre completarlas o se detenga antes de 
        terminar perderá un punto.''',
    '''5.	Palabras por letras: cada jugador deberá decir una palabra que comience con la letra correspondiente a su 
        turno (ejemplo: el primero con A, el siguiente con B, y así sucesivamente hasta llegar a Z; luego se reinicia
        el ciclo). 
        \n •	Las palabras no pueden repetirse.
        \n •	Cada jugador tiene un máximo de 5 segundos para responder.
        \n •	El reto continúa hasta que alguien no pueda aportar una palabra válida dentro del tiempo.'''
]

castigo = [
    '1.	No puedes llamar a alguien por su primer nombre.',
    '2.	Al empezar tu turno, debes decir “Por favor”.',
    '3.	No puedes usar tu mano derecha.',
    '4.	No puedes usar los pulgares.',
    '5.	No puedes apuntar con el dedo.',
    '6.	No puedes mostrar los dientes al hablar.',
    '7.	Debes hacer una reverencia antes de empezar el turno.',
    '8.	No puedes alzar la voz.',
    '9.	No se puede reírse.',
    '10. Todos deben __________________.'
]

mouse_master = [
    '1.	Echo: el jugador que saque la carta “Mouse Maestro Echo” deberá elegir a otro participante. \n '
    '   Ese jugador repetirá una palabra, frase u oración corta cada vez que el Mouse Maestro Echo la repita.',
    '2.	Mimo: el jugador que saque la carta “Mouse Maestro Mimo” seleccionará a otro participante. \n '
    '   Ese jugador imitará la acción que realice el Mouse Maestro Mimo, repitiéndola cada vez que este la ejecute.',
    '''3.	Maestro: el jugador que saque la carta “Mouse Maestro Maestro” elegirá una acción que todos \n 
        los participantes deberán realizar. Los jugadores repetirán la acción cada vez que el Mouse Maestro \n 
        Maestro la ejecute. Esta dinámica continuará hasta que el Maestro sea eliminado; en ese momento, otro \n 
        jugador podría asumir el rol de Mouse Maestro Maestro si vuelve a sacar la carta.
        Ejemplo: “Todos deberán rascarse la cabeza cuando yo me rasque la cabeza”. '''
]

# Diccionario con clases y sus listas
clases = {
    "verdad": verdad,
    "reto": reto,
    "castigo": castigo,
    "mouse maestro": mouse_master
}

# Pesos basados en cantidad de cartas
nombres_clases = list(clases.keys())
pesos = [len(clases[c]) for c in nombres_clases]  # más cartas = más probabilidad

def tarjeta():

    # Elegir clase según pesos
    clase_elegida = choices(nombres_clases, weights=pesos, k=1)[0]
    
    # Elegir contenido dentro de esa clase
    contenido = choice(clases[clase_elegida])
    
    # Crear objeto Card
    return card(clase_elegida, contenido, "todos")

