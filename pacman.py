import pyxel, time
from personajes import Personajes
from constantes import (
    ListaPuntos, ListaImagenesPacMan, velocidad_pacman, ListaBloques, 
    velocidad, ListaImagenes, Constantes
    )

class PacMan(Personajes):
    '''
    Clase de PacMan 
    '''
    def __init__(self, x: int, y: int):
        '''
        Este método crea el objeto

        Atributos:
            x (int): la x donde inicia el personaje
            y (int): la y donde inicia el personaje
        '''
        super().__init__(x,y)
        
        self.tiempo = 300
        self.puntuacion = 0
        self.velocidad = velocidad_pacman
        self.poderes = False
        
        self.blinky_asustado, self.inky_asustado = False, False
        self.clyde_asustado, self.pinky_asustado = False, False
        self.blinky_normal, self.inky_normal = False, False
        self.clyde_normal, self.pinky_normal = False, False
        
        self.sprite_actual = ListaImagenesPacMan[0] 
        self.ListaImagenes = ListaImagenesPacMan
    
    def colision_puntos(self):
        '''
        Verifica si PacMan ha colisionado con un punto y lo elimina de la 
        lista de puntos.
        '''
        self.poderes_activos()
        self.restablecer_color()

        for punto in ListaPuntos[self.constantes.nivel]:
            punto_x, punto_y, tipo = punto

            if punto_x == self.x and punto_y == self.y:
                if tipo == 'PuntoPequeño':
                    self.puntuacion += 50

                elif tipo == 'PuntoGrande':
                    self.puntuacion += 125
                    self.poderes = True
                    self.blinky_asustado, self.inky_asustado = True, True
                    self.clyde_asustado, self.pinky_asustado = True, True
                    self.blinky_normal, self.inky_normal = False, False
                    self.clyde_normal, self.pinky_normal = False, False
                    self.tiempo = 300

                ListaPuntos[self.constantes.nivel].remove(punto)
    
    def poderes_activos(self):
        '''
        Método que asusta a los fantasmas cuando los poderes están activos
        '''
        if self.poderes == True:
            self.tiempo -= 1

            if self.tiempo == 0:
                self.poderes = False
                self.blinky_asustado, self.inky_asustado = False, False
                self.clyde_asustado, self.pinky_asustado = False, False
        
        else:
            self.tiempo = 300
    
    def restablecer_color(self):
        '''
        Método que permite restablecer el color de los fantasmas cuando son 
        comidos
        '''
        if self.blinky_normal: 
            self.blinky_asustado = False

        elif self.inky_normal:
            self.inky_asustado = False

        elif self.clyde_normal:
            self.clyde_asustado = False 

        elif self.pinky_normal:
            self.pinky_asustado = False