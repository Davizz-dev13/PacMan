import pyxel, time
from personajes import Personajes
from constantes import (
    ListaImagenes, ListaImagenesInky, velocidad_fantasmas, ListaBloques, 
    velocidad
    )
from pacman import PacMan

class Inky(Personajes):
    '''
    Clase de Inky 
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
        self.sprite_actual = ListaImagenesInky[0]
        self.velocidad = velocidad_fantasmas
    
    def asustado(self):
        '''
        Método que nos permite modificar el sprite de Inky si está asustado
        '''
        if not self.pacman.inky_asustado:
            self.ListaImagenes = ListaImagenesInky
        else:
            self.ListaImagenes = ListaImagenes