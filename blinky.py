import pyxel, time
from personajes import Personajes
from constantes import (
    ListaImagenes, ListaImagenesBlinky, velocidad_fantasmas, ListaBloques, 
    velocidad, Constantes
    )
from pacman import PacMan

class Blinky(Personajes):
    '''
    Clase de Blinky 
    '''
    def __init__(self, x: int, y: int, pacman: PacMan):
        '''
        Este método crea el objeto Blinky

        Atributos:
            x (int): la x donde inicia el personaje
            y (int): la y donde inicia el personaje
        '''
        super().__init__(x,y)
        
        self.pacman = pacman
        self.sprite_actual = ListaImagenesBlinky[0]
        self.velocidad = velocidad_fantasmas

    def asustado(self):
        '''
        Método que nos permite modificar el sprite de Blinky si está asustado
        '''
        if not self.pacman.blinky_asustado:
            self.ListaImagenes = ListaImagenesBlinky
        else:
            self.ListaImagenes = ListaImagenes