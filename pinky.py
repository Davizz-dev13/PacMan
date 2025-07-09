import pyxel, time
from personajes import Personajes
from constantes import (
    ListaImagenes,ListaImagenesPinky, velocidad_fantasmas, ListaBloques, 
    velocidad
    )
from pacman import PacMan

class Pinky(Personajes):
    '''
    Clase de Pinky 
    '''
    def __init__(self, x: int, y: int, pacman: PacMan):
        '''
        Este método crea el objeto

        Atributos:
            x (int): la x donde inicia el personaje
            y (int): la y donde inicia el personaje
        '''
        super().__init__(x,y)
        
        self.pacman = pacman
        self.sprite_actual = ListaImagenesPinky[0]
        self.velocidad = velocidad_fantasmas

    def asustado(self):
        '''
        Método que nos permite modificar el sprite de Pinky si está asustado
        '''
        if not self.pacman.pinky_asustado:
            self.ListaImagenes = ListaImagenesPinky
        else:
            self.ListaImagenes = ListaImagenes