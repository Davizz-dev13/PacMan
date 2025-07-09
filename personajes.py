from constantes import ListaBloques, velocidad, ListaImagenes, Constantes
import pyxel
class Personajes:
    '''
    Clase de los personajes, actúa como clase padre para evitar duplicar código 
    de forma innecesaria en cada uno de los fantasmas
    '''
    def __init__(self, x:int, y:int):
        '''
        Este método crea el objeto

        Atributos:
            x (int): la x donde inicia el personaje
            y (int): la y donde inicia del personaje
        '''
        self.x = x
        self.y = y

        self.constantes = Constantes()  # Crear una instancia de Constantes
        self.ListaImagenes = ListaImagenes
        self.animacion_indice = 0
        self.contador_animacion = 0
        self.en_movimiento = False
        self.direccion_activa = 'izquierda'  # Dirección actual ('derecha', 'izquierda', 'arriba', 'abajo')

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, newX:int):
        if not isinstance(newX, int):
            raise TypeError ('La x debe de ser de tipo entero')
        elif newX < 0:
            raise ValueError ('La x no puede tener valores negativos')
        else:
            self.__x = newX
    
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, newY:int):
        if not isinstance(newY, int):
            raise TypeError ('La y debe de ser de tipo entero')
        elif newY < 0:
            raise ValueError ('La y no puede tener valores negativos')
        else:
            self.__y = newY
    
    def colisiones(self):
        '''
        Verifica si Pac-Man colisiona con un bloque en la dirección activa.
        Retorna True si hay colisión, de lo contrario False.
        '''
        # Determinar las coordenadas del próximo paso según la dirección activa
        devolver = False
        siguiente_x = self.x
        siguiente_y = self.y
        
        if self.direccion_activa == 'derecha':
            siguiente_x = self.x
            siguiente_y = self.y

        elif self.direccion_activa == 'izquierda':
            siguiente_x = self.x
            siguiente_y = self.y

        elif self.direccion_activa == 'arriba':
            siguiente_x = self.x
            siguiente_y = self.y

        elif self.direccion_activa == 'abajo':
            siguiente_x = self.x
            siguiente_y = self.y
            
        else: 
            devolver = False

        # Verificar colisión en la dirección calculada
        for bloque_x, bloque_y, _ in ListaBloques[self.constantes.nivel]:
            if (
                siguiente_x < bloque_x + 16 and siguiente_x + 16 > bloque_x and
                siguiente_y < bloque_y + 16 and siguiente_y + 16 > bloque_y
            ):
                devolver = True  # Hay colisión en la dirección activa

        return devolver 

    def direccion_causara_colision(self, direccion: str, bloques: tuple):
        '''
        Verifica si la dirección especificada causará una colisión.
        Retorna True si hay colisión, False en caso contrario.

        Parámetros:
            direccion (str): dirección en la que se esté moviendo
            bloques (tuple): tupla con los bloques del mapa 
        '''
        siguiente_x = self.x
        siguiente_y = self.y
        devolver = False

        if direccion == 'derecha':
            siguiente_x += self.velocidad

        elif direccion == 'izquierda':
            siguiente_x -= self.velocidad

        elif direccion == 'abajo':
            siguiente_y += self.velocidad

        elif direccion == 'arriba':
            siguiente_y -= self.velocidad

        for bloque_x, bloque_y, _ in bloques:
            if (
                siguiente_x < bloque_x + 16 and siguiente_x + 16 > bloque_x and
                siguiente_y < bloque_y + 16 and siguiente_y + 16 > bloque_y
            ):
                devolver = True  # Hay colisión
        
        return devolver
    
    def actualizar_movimiento(self, limite_ancho: int, limite_alto: int):
        '''
        Actualiza el movimiento continuo de Pac-Man y verifica colisiones.

        Parámetros:
            limite_ancho (int): limite definido por el ancho del mapa 
            limite_alto (int): limite definido por el alto del mapa
        '''
        # Guardar posición previa
        posicion_previa_x = self.x
        posicion_previa_y = self.y

        # Intentar mover a Pac-Man en la dirección activa
        if self.direccion_activa == 'derecha' and self.x + 16 < limite_ancho:
            self.x += self.velocidad

        elif self.direccion_activa == 'izquierda' and self.x > 0:
            self.x -= self.velocidad

        elif self.direccion_activa == 'abajo' and self.y + 16 < limite_alto:
            self.y += self.velocidad

        elif self.direccion_activa == 'arriba' and self.y > 0:
            self.y -= self.velocidad

        # Verificar colisiones
        if self.colisiones():
            # Si hay colisión, revertir posición y detener animación
            self.x = posicion_previa_x
            self.y = posicion_previa_y
            self.en_movimiento = False
            
        else:
            # Si no hay colisión, permitir animación
            self.en_movimiento = True
            self.actualizar_sprite()
    
    def dibujar(self):
        '''
        Dibuja a PacMan en su posición actual usando el sprite correspondiente
        '''
        _, sx, sy, sw, sh = self.sprite_actual
        
        pyxel.blt(self.x, self.y, 0, sx, sy, sw, sh, 0)  # Dibuja el sprite

    def actualizar_sprite(self):
        '''
        Método que nos permite ir cambiando al sprite de los personajes 
        mientras ests se mueven
        '''
        self.contador_animacion += 1
        if self.contador_animacion % 5 == 0:
            if self.direccion_activa == 'derecha':
                self.animacion_indice = (self.animacion_indice + 1) % 2
                self.sprite_actual = self.ListaImagenes[self.animacion_indice]
       
            elif self.direccion_activa == 'izquierda':
                self.animacion_indice = (self.animacion_indice + 1) % 2 + 2
                self.sprite_actual = self.ListaImagenes[self.animacion_indice]
      
            elif self.direccion_activa == 'arriba':
                self.animacion_indice = (self.animacion_indice + 1) % 2 + 4
                self.sprite_actual = self.ListaImagenes[self.animacion_indice]
           
            elif self.direccion_activa == 'abajo':
                self.animacion_indice = (self.animacion_indice + 1) % 2 + 6
                self.sprite_actual = self.ListaImagenes[self.animacion_indice]