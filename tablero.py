import pyxel, random
from constantes import (
    ListaBloques, SpriteMuroV, SpriteMuroH, SpriteMuroE1, SpriteMuroE2, 
    SpriteMuroE3, SpriteMuroE4, ListaPuntos, PuntoPequeño, PuntoGrande, 
    cereza, platano, sandia, pera, fresa, ListaMovimientos, Constantes
    )
from pacman import PacMan
from clyde import Clyde
from blinky import Blinky
from inky import Inky
from pinky import Pinky


class Tablero:
    '''
    Clase que contiene el tablero
    '''
    def __init__(self, ancho:int, alto:int):
        '''
        Este método crea el objeto tablero

        Atributos:
                ancho (int): píxeles que mide el ancho del tablero
                alto (int): píxeles que mide el lardo del tablero 
        '''
        self.vidas = 3
        self.__ancho = ancho
        self.__alto = alto
        self.constantes = Constantes()

        self.pacman = PacMan(48, 48)
        self.clyde = Clyde(192, 128, self.pacman)
        self.blinky = Blinky(192, 96, self.pacman)
        self.inky = Inky(48, 88, self.pacman)
        self.pinky = Pinky(48,104, self.pacman)
        pyxel.init(self.ancho, self.alto, title="Pac-Man")

        pyxel.load("assets.pyxres")
        self.camera_x = 0  # Posición inicial de la cámara
        self.camera_y = 0
        pyxel.run(self.update, self.pintar_bloque)
        


    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, newAncho:int):
        if not isinstance(newAncho, int):
            raise TypeError ('El ancho debe de ser de tipo entero')
        elif newAncho < 0:
            raise ValueError ('El ancho no puede tener valores negativos')
        else:
            self.__ancho = newAncho
    
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, newAlto:int):
        if not isinstance(newAlto, int):
            raise TypeError ('El alto debe de ser de tipo entero')
        elif newAlto < 0:
            raise ValueError ('El alto no puede tener valores negativos')
        else:
            self.__alto = newAlto

    def update(self):
        self.actualizar_pacman()
        self.actualizar_fantasmas()

        if self.colision_fantasmas():
            self.reiniciar_posicion()
        if len(ListaPuntos[self.constantes.nivel]) == 0:
            self.pasar_nivel()

    def actualizar_pacman(self):
        '''
        Actualiza el estado del juego, incluyendo entrada del usuario.
        '''
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        # Nueva dirección basada en la entrada del usuario
        nueva_direccion = None
        if pyxel.btn(pyxel.KEY_RIGHT):
            nueva_direccion = 'derecha'
        elif pyxel.btn(pyxel.KEY_LEFT):
            nueva_direccion = 'izquierda'
        elif pyxel.btn(pyxel.KEY_DOWN):
            nueva_direccion = 'abajo'
        elif pyxel.btn(pyxel.KEY_UP):
            nueva_direccion = 'arriba'

        # Verificar colisión para la nueva dirección antes de cambiar
        if nueva_direccion:
            if not self.pacman.direccion_causara_colision(
                nueva_direccion, ListaBloques[self.constantes.nivel]
                ):
                self.pacman.direccion_activa = nueva_direccion

        # Actualizar movimiento continuo de Pac-Man
        self.pacman.actualizar_movimiento(self.ancho, self.alto)
        self.pacman.colision_puntos()
    
    def actualizar_fantasmas(self):
        '''
        Método que actualiza el movimiento de los fantasmas 
        '''
        fantasmas = (self.clyde, self.blinky, self.inky, self.pinky)

        for i in fantasmas:
            if i.direccion_causara_colision(
                i.direccion_activa, ListaBloques[self.constantes.nivel]
                ):
                # Elegir una nueva dirección aleatoria de la lista
                nueva_direccion = random.choice(
                    ('derecha', 'izquierda', 'arriba', 'abajo')
                    )
                i.direccion_activa = nueva_direccion

            else:
                if random.uniform(0, 2) > 1.99:
                    nueva_direccion = random.choice(
                        ('derecha', 'izquierda', 'arriba', 'abajo')
                        )
                    i.direccion_activa = nueva_direccion
                    i.actualizar_movimiento(self.ancho, self.alto)

                else:
                    # Si no hay colisión, continuar moviéndose
                    i.actualizar_movimiento(self.ancho, self.alto)
        
        self.blinky.asustado()
        self.clyde.asustado()
        self.pinky.asustado()
        self.inky.asustado()

    def pintar_bloque(self):
        '''
        Método que pinta los bloques en el tablero
        '''
        if self.vidas > 0:
            pyxel.cls(0)  # Limpia la pantalla

            if len(ListaPuntos[self.constantes.nivel]) == 0:
                self.constantes.nivel += 1
        
            for x, y, tipo in ListaBloques[self.constantes.nivel]:
                sprite = self.obtener_sprite(tipo)
                if sprite:
                    sx, sy, _, sw, sh = sprite
                    pyxel.blt(x, y, 0, sx, sy, sw, sh, 0)

            for x, y, tipo in ListaPuntos[self.constantes.nivel]:
                sprite = self.obtener_sprite(tipo)
                if sprite:
                    sx, sy, _, sw, sh = sprite
                    pyxel.blt(x, y, 0, sx, sy, sw, sh, 0)

            for i in range(self.vidas):
                x = 8
                x += i*16
                pyxel.blt(x, 276, 0, 96, 48, 16, 16, 0)
            
            pyxel.text(
                8, 264, 'Puntuacion: %i'
                %self.pacman.puntuacion, pyxel.COLOR_WHITE
                )

            self.pacman.dibujar()    
    
        else:
            pyxel.cls(0)
            pyxel.text(
                100, 152, 'Game Over\n\nPuntuacion: %i'
                %self.pacman.puntuacion, pyxel.COLOR_RED
                )
        
        self.clyde.dibujar()
        self.blinky.dibujar()
        self.inky.dibujar()
        self.pinky.dibujar()
        
        if self.constantes.nivel == 1:
            pyxel.cls(0)
            pyxel.text(
                100, 152, 'You win\n\nPuntuacion: %i'
                %self.pacman.puntuacion, pyxel.COLOR_GREEN
                )
        
            self.clyde.dibujar()
            self.blinky.dibujar()
            self.inky.dibujar()
            self.pinky.dibujar()    
    
    def obtener_sprite(self, tipo: str):
        '''
        Método que permite obtener el sprite

        Parámetros:
            tipo (str): tipo de objeto a pintar
        '''
        ListaSprite = (
            SpriteMuroV, SpriteMuroH, SpriteMuroE1, SpriteMuroE2, SpriteMuroE3, 
            SpriteMuroE4, PuntoPequeño, PuntoGrande,cereza, platano, sandia, 
            pera, fresa
                       )
        ListaCosas = (
            'MuroV', 'MuroH', 'MuroE1', 'MuroE2', 'MuroE3', 'MuroE4', 
            'PuntoPequeño', 'PuntoGrande'
                    )
        for i in range(len(ListaCosas)):
            if tipo == ListaCosas[i]:

                return ListaSprite[i]
    
    
    def colision_fantasmas(self):
        '''
        Verifica si PacMan clisiona con cualquiera de los fantasmas.
        Si hay colisión, reinicia el juego
        '''
        # Obtener la posición de PacMan
        siguiente_x = self.pacman.x
        siguiente_y = self.pacman.y
        devolver = None
        # Lista de fantasmas
        fantasmas = (self.clyde, self.blinky, self.inky, self.pinky)
       
       # Comprobar la colisión con cada fantasma
        for fantasma in fantasmas:
            # Obtener las posiciones de los fantasmas
            fantasma_x = fantasma.x
            fantasma_y = fantasma.y

            # Verificar si las coordenadas de PacMan y el fantasma se solapan
            if (
                siguiente_x < fantasma_x + 16 and siguiente_x + 16 > fantasma_x 
                and
                siguiente_y < fantasma_y + 16 and siguiente_y + 16 > fantasma_y
                ):
                devolver = fantasma  # Colisión detectada

        return devolver  # No hay colisión

    def reiniciar_posicion(self):
        '''
        Método que nos permite reiniciar a los fantasmas si son comidos por 
        PacMan mientras tiene los poderes ativos a sus posiciones iniciales, 
        quitandoles la carcaterística de asustados. Y en caso de que no tenga 
        los poderes activos, reiniciar la posición de PacMan y quitarle una 
        vida
        '''
        if not self.pacman.poderes:    
            self.pacman.direccion_activa = None
            self.pacman.x, self.pacman.y = 48, 48
            self.vidas -= 1

        elif self.pacman.blinky_normal and self.colision_fantasmas() == self.blinky:
            self.pacman.direccion_activa = None
            self.pacman.x, self.pacman.y = 48, 48
            self.vidas -= 1
        
        elif self.pacman.inky_normal and self.colision_fantasmas() == self.inky:
            self.pacman.direccion_activa = None
            self.pacman.x, self.pacman.y = 48, 48
            self.vidas -= 1
        
        elif self.pacman.pinky_normal and self.colision_fantasmas() == self.pinky:
            self.pacman.direccion_activa = None
            self.pacman.x, self.pacman.y = 48, 48
            self.vidas -= 1
        
        elif self.pacman.clyde_normal and self.colision_fantasmas() == self.clyde:
            self.pacman.direccion_activa = None
            self.pacman.x, self.pacman.y = 48, 48
            self.vidas -= 1

        else:
            if self.colision_fantasmas() == self.clyde:
                self.clyde.x, self.clyde.y = 192, 128
                self.pacman.clyde_normal = True

            elif self.colision_fantasmas() == self.blinky:
                self.blinky.x, self.blinky.y = 192, 96
                self.pacman.blinky_normal = True

            elif self.colision_fantasmas() == self.inky:
                self.inky.x, self.inky.y = 48, 88
                self.pacman.inky_normal = True
                
            elif self.colision_fantasmas() == self.pinky:
                self.pinky.x, self.pinky.y = 48, 104
                self.pacman.pinky_normal = True
    
    def pasar_nivel(self):
        '''
        Método que reinicia la posición de los personajes al pasar de nivel
        '''
        self.pacman.direccion_activa = 'izquierda'
        self.pacman.x, self.pacman.y = 48, 48
        self.clyde.x, self.clyde.y = 192, 128
        self.blinky.x, self.blinky.y = 192, 96
        self.inky.x, self.inky.y = 48, 88
        self.pinky.x, self.pinky.y = 48, 104