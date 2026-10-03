class c_player:
    player_states = ['in game', 'game over']

    def __init__(self, primer_nombre, primer_apellido, puntos = 10, player_state = 'in game'):
        self.nombre = primer_nombre
        self.apellido = primer_apellido
        self.puntos_restantes = puntos
        self.estado = player_state

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Puntos: {self.puntos_restantes}, Estado: {self.estado}'

    def __repr__(self):
        return self.__str__()

    def status(self):
        return f"{self.nombre} {self.apellido} - Puntos: {self.puntos_restantes}, Estado: {self.estado}"
        
    def perder_puntos(self, cantidad):
        self.puntos_restantes -= cantidad
        if self.puntos_restantes <= 0:
            self.puntos_restantes = 0
            print(' *********** *********** *********** *********** ')
            print(f' {self.nombre} {self.apellido} esta eliminado')
            print(' *********** *********** *********** *********** ')
            self.estado = 'game over'
        else:
            print(f"\n\n {self.nombre} {self.apellido} perdió {cantidad} punto. \n Ahora tiene {self.puntos_restantes}.")

    def actualizar_estado_player(self, nuevo_estado):
        if nuevo_estado.lower() in self.player_states:
            self.estado = nuevo_estado
        else:
            print('Estado inválido. Usa "in game" o "game over".')