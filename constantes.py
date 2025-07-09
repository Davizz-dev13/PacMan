import pyxel
# Datos del mapa
class Constantes:
    def __init__(self):
        self.nivel = 0 

velocidad = 1
ListaImagenes = (
    (0,0,128,16,16),(0,16,128,16,16),
    (0,32,128,16,16),(0,48,128,16,16),
    (0,0,128,16,16),(0,16,128,16,16),
    (0,32,128,16,16),(0,48,128,16,16)
    )
PacManSprite = (96,0,0,16,16)
SpriteMuroV  = (144,32,0,16,16)
SpriteMuroH  = (128,16,0,16,16)
SpriteMuroE1 = (160,0,0,16,16)
SpriteMuroE2 = (144,48,0,16,16)
SpriteMuroE3 = (160,48,0,16,16)
SpriteMuroE4 = (144,16,0,16,16)
PuntoPequeño = (64,0,0,16,16)
PuntoGrande = (64,16,0,16,16)
cereza = (64,32,0,16,16)
platano = (80,128,0,16,16)
sandia = (112,128,0,16,16)
pera = (112,112,0,16,16)
fresa = (96,128,0,16,16)

ListaBloques = ((
   (0, 0, "MuroE1"), (16, 0, "MuroH"), (32, 0, "MuroH"),
   (48, 0, "MuroH"), (64, 0, "MuroH"), (80, 0, "MuroH"),
   (96, 0, "MuroH"), (112, 0, "MuroH"), (128, 0, "MuroH"),
   (144, 0, "MuroH"), (160, 0, "MuroH"), (176, 0, "MuroH"),
   (192, 0, "MuroH"), (208, 0, "MuroH"), (224, 0, "MuroH"),
   # Lista de muros horizontales cara superior y esquina superior izquierda
   (240, 0, "MuroE4"), (240, 16, "MuroV"), (240, 32, "MuroV"),
   (240, 48, "MuroV"), (240, 64, "MuroV"), (240, 80, "MuroV"),
   (240, 96, "MuroV"), (240, 112, "MuroV"), (240, 128, "MuroV"),
   (240, 144, "MuroV"), (240, 160, "MuroV"), (240, 176, "MuroV"),
   (240, 192, "MuroV"), (240, 208, "MuroV"), (240, 224, "MuroV"),
   # Lista de muros verticales cara derecha y esquina superior derecha
   (240, 240, "MuroE3"), (16, 240, "MuroH"), (32, 240, "MuroH"),
   (48, 240, "MuroH"), (64, 240, "MuroH"), (80, 240, "MuroH"),
   (96, 240, "MuroH"), (112, 240, "MuroH"), (128, 240, "MuroH"),
   (144, 240, "MuroH"), (160, 240, "MuroH"), (176, 240, "MuroH"),
   (192, 240, "MuroH"), (208, 240, "MuroH"), (224, 240, "MuroH"),
   #Lista de muros horizontales cara inferior y esquina inferior derecha
   (0, 240, "MuroE2"), (0, 16, "MuroV"), (0, 32, "MuroV"),
   (0, 48, "MuroV"), (0, 64, "MuroV"), (0, 80, "MuroV"),
   (0, 96, "MuroV"), (0, 112, "MuroV"), (0, 128, "MuroV"),
   (0, 144, "MuroV"), (0, 160, "MuroV"), (0, 176, "MuroV"),
   (0, 192, "MuroV"), (0, 208, "MuroV"), (0, 224, "MuroV"),
   #Lista de muros verticales cara izquierda y esquina inferior izquierda




    (32, 32, "MuroV"), (32, 48, "MuroV"), (32, 64, "MuroE2"), (48, 64, "MuroH"),
    (64, 64, "MuroE3"), (64, 48, "MuroV"), (64, 32, "MuroV"),
    # U
    (32, 104, "MuroV"), (32, 88, "MuroV"), (56, 72, "MuroH"),(64, 72, "MuroH"), (32, 72, "MuroE1"),
    (48, 72, "MuroH"),(48, 120, "MuroH"), (32, 120, "MuroE2"), (64, 120, "MuroH"), (56, 120, "MuroH"),
    # C
    (192, 80, "MuroH"), (176, 80, "MuroH"), (208, 80, "MuroE4"), (208, 96, "MuroV"), (208, 112, "MuroV"), (
    208, 128, "MuroV"), (208, 144, "MuroE3"), (192, 144, "MuroH"), (176, 144, "MuroH"), (192, 112, "MuroH"),(176, 112, "MuroH"),
    # 3
    (208, 184, "MuroV"), (208, 168, "MuroV"), (208, 152, "MuroE4"), (192, 152, "MuroH"), (176, 152, "MuroH"), (
    160, 152, "MuroE1"), (160, 168, "MuroV"),(160, 184, "MuroV"),  (184, 162, "MuroV"),
    # M




    # Redondeles
    (144, 64, "MuroE3"),(128,64,"MuroH"), (96, 64, "MuroE2"),
    (128, 110, "MuroH"),(96, 120, "MuroE2"), (128, 120, "MuroH"),(144, 120, "MuroE3"),
    (96, 48, "MuroE1"), (128, 48, "MuroH"),(144, 48, "MuroE4"),
    (96, 96, "MuroE1"), (128, 96, "MuroH"),(144, 96, "MuroE4"),(144, 108, "MuroV"),(96, 108, "MuroV"),




    #Resto Mapa:
    (64, 208, "MuroH"),(80,208,"MuroE3"),(80,200,"MuroV"),(80,184,"MuroE4"),(64,184,"MuroH"), (48, 184, "MuroE3"),
    (32, 184, "MuroE1"),(32,200,"MuroV"),(32,208,"MuroE2"),(48,208,"MuroH"),(48, 168, "MuroV"), (16, 152, "MuroH"),
    (32, 152, "MuroH"),(48, 152, "MuroE4"),(80,152,"MuroH"),(96,152,"MuroH"),(112,152,"MuroH"),(128,152,"MuroH"),
    (112,168,"MuroV"),(128,200,"MuroV"),(112,200,"MuroV"),(128,208,"MuroV"),(112,208,"MuroV"),(160,224,"MuroV"),
    (160,216,"MuroV"),(192,208,"MuroV"),(192,194,"MuroV"),(224,224,"MuroV"),(224,216,"MuroV"),(96,16,"MuroV"),
    (128,32,"MuroV"),(160,16,"MuroV"),(192,48,"MuroH"),(176,48,"MuroH"),(208,48,"MuroH"),(192,32,"MuroV"),(224,16,"MuroE2"),
    (0, 0, "MuroE1"), (16, 0, "MuroH"), (32, 0, "MuroH"),
    (48, 0, "MuroH"), (64, 0, "MuroH"), (80, 0, "MuroH"),
    (96, 0, "MuroH"), (112, 0, "MuroH"), (128, 0, "MuroH"),
    (144, 0, "MuroH"), (160, 0, "MuroH"), (176, 0, "MuroH"),
    (192, 0, "MuroH"), (208, 0, "MuroH"), (224, 0, "MuroH"),
    # Lista de muros horizontales cara superior y esquina superior izquierda

    (240, 0, "MuroE4"), (240, 16, "MuroV"), (240, 32, "MuroV"),
    (240, 48, "MuroV"), (240, 64, "MuroV"), (240, 80, "MuroV"),
    (240, 96, "MuroV"), (240, 112, "MuroV"), (240, 128, "MuroV"),
    (240, 144, "MuroV"), (240, 160, "MuroV"), (240, 176, "MuroV"),
    (240, 192, "MuroV"), (240, 208, "MuroV"), (240, 224, "MuroV"),
    # Lista de muros verticales cara derecha y esquina superior derecha

    (240, 240, "MuroE3"), (16, 240, "MuroH"), (32, 240, "MuroH"),
    (48, 240, "MuroH"), (64, 240, "MuroH"), (80, 240, "MuroH"),
    (96, 240, "MuroH"), (112, 240, "MuroH"), (128, 240, "MuroH"),
    (144, 240, "MuroH"), (160, 240, "MuroH"), (176, 240, "MuroH"),
    (192, 240, "MuroH"), (208, 240, "MuroH"), (224, 240, "MuroH"),
    # Lista de muros horizontales cara inferior y esquina inferior derecha

    (0, 240, "MuroE2"), (0, 16, "MuroV"), (0, 32, "MuroV"),
    (0, 48, "MuroV"), (0, 64, "MuroV"), (0, 80, "MuroV"),
    (0, 96, "MuroV"), (0, 112, "MuroV"), (0, 128, "MuroV"),
    (0, 144, "MuroV"), (0, 160, "MuroV"), (0, 176, "MuroV"),
    (0, 192, "MuroV"), (0, 208, "MuroV"), (0, 224, "MuroV"),
    # Lista de muros verticales cara izquierda y esquina inferior izquierda

    (32, 32, "MuroV"), (32, 48, "MuroV"), (32, 64, "MuroE2"), (48, 64, "MuroH"),
    (64, 64, "MuroE3"), (64, 48, "MuroV"), (64, 32, "MuroV"),
    # U
    (32, 104, "MuroV"), (32, 88, "MuroV"), (56, 72, "MuroH"), (64, 72, "MuroH"), (32, 72, "MuroE1"),
    (48, 72, "MuroH"), (48, 120, "MuroH"), (32, 120, "MuroE2"), (64, 120, "MuroH"), (56, 120, "MuroH"),
    # C
    (192, 80, "MuroH"), (176, 80, "MuroH"), (208, 80, "MuroE4"), (208, 96, "MuroV"),
    (208, 112, "MuroV"), (208, 128, "MuroV"), (208, 144, "MuroE3"), (192, 144, "MuroH"), (176, 144, "MuroH"),
    (192, 112, "MuroH"), (176, 112, "MuroH"),
    # 3
    (208, 184, "MuroV"), (208, 168, "MuroV"), (208, 152, "MuroE4"), (192, 152, "MuroH"),
    (176, 152, "MuroH"), (160, 152, "MuroE1"), (160, 168, "MuroV"), (160, 184, "MuroV"), (184, 162, "MuroV"),
    # M

    # Redondeles
    (144, 64, "MuroE3"), (128, 64, "MuroH"), (96, 64, "MuroE2"),
    (128, 110, "MuroH"), (96, 120, "MuroE2"), (128, 120, "MuroH"), (144, 120, "MuroE3"),
    (96, 48, "MuroE1"), (128, 48, "MuroH"), (144, 48, "MuroE4"),
    (96, 96, "MuroE1"), (128, 96, "MuroH"), (144, 96, "MuroE4"), (144, 108, "MuroV"),
    (96, 108, "MuroV"),

    # Resto Mapa:
    (64, 208, "MuroH"), (80, 208, "MuroE3"), (80, 200, "MuroV"), (80, 184, "MuroE4"),
    (64, 184, "MuroH"), (48, 184, "MuroE3"),
    (32, 184, "MuroE1"), (32, 200, "MuroV"), (32, 208, "MuroE2"), (48, 208, "MuroH"),
    (48, 168, "MuroV"), (16, 152, "MuroH"),
    (32, 152, "MuroH"), (48, 152, "MuroE4"), (80, 152, "MuroH"), (96, 152, "MuroH"),
    (112, 152, "MuroH"), (128, 152, "MuroH"),
    (112, 168, "MuroV"), (128, 200, "MuroV"), (112, 200, "MuroV"), (128, 208, "MuroV"),
    (112, 208, "MuroV"), (160, 224, "MuroV"),
    (160, 216, "MuroV"), (192, 208, "MuroV"), (192, 194, "MuroV"), (224, 224, "MuroV"),
    (224, 216, "MuroV"), (96, 16, "MuroV"),
    (128, 32, "MuroV"), (160, 16, "MuroV"), (192, 48, "MuroH"), (176, 48, "MuroH"), (208, 48, "MuroH"),
    (192, 32, "MuroV"), (224, 16, "MuroE2")),

    (
    (0, 0, "MuroE1"), (16, 0, "MuroH"), (32, 0, "MuroH"),
    (48, 0, "MuroH"), (64, 0, "MuroH"), (80, 0, "MuroH"),
    (96, 0, "MuroH"), (112, 0, "MuroH"), (128, 0, "MuroH"),
    (144, 0, "MuroH"), (160, 0, "MuroH"), (176, 0, "MuroH"),
    (192, 0, "MuroH"), (208, 0, "MuroH"), (224, 0, "MuroH"),
    # Lista de muros horizontales cara superior y esquina superior izquierda

    (240, 0, "MuroE4"), (240, 16, "MuroV"), (240, 32, "MuroV"),
    (240, 48, "MuroV"), (240, 64, "MuroV"), (240, 80, "MuroV"),
    (240, 96, "MuroV"), (240, 112, "MuroV"), (240, 128, "MuroV"),
    (240, 144, "MuroV"), (240, 160, "MuroV"), (240, 176, "MuroV"),
    (240, 192, "MuroV"), (240, 208, "MuroV"), (240, 224, "MuroV"),
    # Lista de muros verticales cara derecha y esquina superior derecha

    (240, 240, "MuroE3"), (16, 240, "MuroH"), (32, 240, "MuroH"),
    (48, 240, "MuroH"), (64, 240, "MuroH"), (80, 240, "MuroH"),
    (96, 240, "MuroH"), (112, 240, "MuroH"), (128, 240, "MuroH"),
    (144, 240, "MuroH"), (160, 240, "MuroH"), (176, 240, "MuroH"),
    (192, 240, "MuroH"), (208, 240, "MuroH"), (224, 240, "MuroH"),
    # Lista de muros horizontales cara inferior y esquina inferior derecha

    (0, 240, "MuroE2"), (0, 16, "MuroV"), (0, 32, "MuroV"),
    (0, 48, "MuroV"), (0, 64, "MuroV"), (0, 80, "MuroV"),
    (0, 96, "MuroV"), (0, 112, "MuroV"), (0, 128, "MuroV"),
    (0, 144, "MuroV"), (0, 160, "MuroV"), (0, 176, "MuroV"),
    (0, 192, "MuroV"), (0, 208, "MuroV"), (0, 224, "MuroV"),
    # Lista de muros verticales cara izquierda y esquina inferior izquierda

    (32, 32, "MuroV"), (32, 48, "MuroV"), (32, 64, "MuroE2"), (48, 64, "MuroH"),
    (64, 64, "MuroE3"), (64, 48, "MuroV"), (64, 32, "MuroV"),
    # U
    (32, 104, "MuroV"), (32, 88, "MuroV"), (56, 72, "MuroH"), (64, 72, "MuroH"), (32, 72, "MuroE1"),
    (48, 72, "MuroH"), (48, 120, "MuroH"), (32, 120, "MuroE2"), (64, 120, "MuroH"), (56, 120, "MuroH"),
    # C
    (192, 80, "MuroH"), (176, 80, "MuroH"), (208, 80, "MuroE4"), (208, 96, "MuroV"),
    (208, 112, "MuroV"), (
        208, 128, "MuroV"), (208, 144, "MuroE3"), (192, 144, "MuroH"), (176, 144, "MuroH"),
    (192, 112, "MuroH"), (176, 112, "MuroH"),
    # 3
    (208, 184, "MuroV"), (208, 168, "MuroV"), (208, 152, "MuroE4"), (192, 152, "MuroH"),
    (176, 152, "MuroH"), (
        160, 152, "MuroE1"), (160, 168, "MuroV"), (160, 184, "MuroV"), (184, 162, "MuroV"),
    # M

    # Redondeles
    (128, 64, "MuroH"), (144, 64, "MuroE3"), (112, 64, "MuroH"), (96, 64, "MuroE2"),
    (128, 108, "MuroH"), (96, 120, "MuroE2"), (128, 120, "MuroH"), (144, 120, "MuroE3"),
    (112, 48, "MuroH"), (96, 48, "MuroE1"), (128, 48, "MuroH"), (144, 48, "MuroE4"),
    (96, 96, "MuroE1"), (128, 96, "MuroH"), (144, 96, "MuroE4"), (112, 96, "MuroH"),
    (112, 120, "MuroH"), (112, 108, "MuroH"), (144, 108, "MuroV"), (96, 108, "MuroV"),

    # Resto Mapa:
    (64, 208, "MuroH"), (80, 208, "MuroE3"), (80, 200, "MuroV"), (80, 184, "MuroE4"),
    (64, 184, "MuroH"), (48, 184, "MuroE3"),
    (32, 184, "MuroE1"), (32, 200, "MuroV"), (32, 208, "MuroE2"), (48, 208, "MuroH"),
    (48, 168, "MuroV"), (16, 152, "MuroH"),
    (32, 152, "MuroH"), (48, 152, "MuroE4"), (80, 152, "MuroH"), (96, 152, "MuroH"),
    (112, 152, "MuroH"), (128, 152, "MuroH"),
    (112, 168, "MuroV"), (128, 200, "MuroV"), (112, 200, "MuroV"), (128, 208, "MuroV"),
    (112, 208, "MuroV"), (160, 224, "MuroV"),
    (160, 216, "MuroV"), (192, 208, "MuroV"), (192, 194, "MuroV"), (224, 224, "MuroV"),
    (224, 216, "MuroV"), (96, 16, "MuroV"),
    (128, 32, "MuroV"), (160, 16, "MuroV"), (192, 48, "MuroH"), (176, 48, "MuroH"), (208, 48, "MuroH"),
    (192, 32, "MuroV"), (224, 16, "MuroE2")
    ))
# Puntos:
ListaPuntos = [[
        (112, 48, "PuntoPequeño"),(112, 64, "PuntoPequeño"),
        (48,32,"PuntoPequeño"),(48,16,"PuntoPequeño"),
        (32,16,"PuntoPequeño"),(16,16,"PuntoPequeño"),
        (16,32,"PuntoPequeño"),(16,52,"PuntoPequeño"),
        (16,70,"PuntoPequeño"),(16,86,"PuntoPequeño"),
        (16,102,"PuntoPequeño"),(16,118,"PuntoPequeño"),
        (16,136,"PuntoPequeño"),(32,136,"PuntoPequeño"),
        (48,136,"PuntoPequeño"),(64,136,"PuntoPequeño"),
        (80,136,"PuntoPequeño"),(96,136,"PuntoPequeño"),
        (112,118,"PuntoPequeño"),(112,98,"PuntoPequeño"),
        (112,80,"PuntoPequeño"),(128,80,"PuntoPequeño"),
        (144,80,"PuntoPequeño"),(112,136,"PuntoPequeño"),
        (128,136,"PuntoPequeño"),(144,136,"PuntoPequeño"),
        (160,136,"PuntoPequeño"),(160,120,"PuntoPequeño"),
        (160,100,"PuntoPequeño"),(160,80,"PuntoPequeño"),
        (16,168,"PuntoPequeño"),(32,168,"PuntoGrande"),
        (64,16,"PuntoPequeño"),(80,16,"PuntoGrande"),
        (80,32,"PuntoPequeño"),(96,32,"PuntoPequeño"),
        (112,32,"PuntoPequeño"),(80,32,"PuntoPequeño"),
        (80,48,"PuntoPequeño"),(80,64,"PuntoPequeño"),
        (80,80,"PuntoPequeño"),(96,80,"PuntoPequeño"),
        (144,32,"PuntoPequeño"),(80,98,"PuntoPequeño"),
        (80,118,"PuntoPequeño"),(64,152,"PuntoPequeño"),
        (64,168,"PuntoPequeño"),(80,168,"PuntoPequeño"),
        (96,168,"PuntoPequeño"),(96,184,"PuntoPequeño"),
        (96,206,"PuntoPequeño"),(96,224,"PuntoPequeño"),
        (80,224,"PuntoPequeño"),(64,224,"PuntoPequeño"),
        (48,224,"PuntoPequeño"),(32,224,"PuntoPequeño"),
        (16,224,"PuntoPequeño"),(16,206,"PuntoPequeño"),
        (16,186,"PuntoPequeño"),(112,224,"PuntoPequeño"),
        (128,224,"PuntoPequeño"),(144,224,"PuntoPequeño"),
        (144,200,"PuntoPequeño"),(144,184,"PuntoPequeño"),
        (144,168,"PuntoPequeño"),(144,152,"PuntoPequeño"),
        (128,184,"PuntoPequeño"),(112,184,"PuntoPequeño"),
        (128,168,"PuntoPequeño"),(160,200,"PuntoPequeño"),
        (176,200,"PuntoPequeño"),(176,224,"PuntoPequeño"),
        (176,178,"PuntoPequeño"),(192,178,"PuntoGrande"),
        (208,224,"PuntoPequeño"),(192,224,"PuntoPequeño"),
        (208,200,"PuntoPequeño"),(224,200,"PuntoPequeño"),
        (224,184,"PuntoPequeño"),(224,168,"PuntoPequeño"),
        (224,152,"PuntoPequeño"),(224,136,"PuntoPequeño"),
        (224,120,"PuntoPequeño"),(224,104,"PuntoPequeño"),
        (224,88,"PuntoPequeño"),(224,64,"PuntoPequeño"),
        (208,64,"PuntoPequeño"),(192,64,"PuntoPequeño"),
        (160,64,"PuntoPequeño"),(176,64,"PuntoPequeño"),
        (224,48,"PuntoPequeño"),(224,32,"PuntoPequeño"),
        (208,32,"PuntoGrande"),(208,16,"PuntoPequeño"),
        (192,16,"PuntoPequeño"),(176,16,"PuntoPequeño"),
        (176,32,"PuntoPequeño"),(160,32,"PuntoPequeño"),
        (112,16,"PuntoPequeño"),(144,16,"PuntoPequeño"),
        (128,16,"PuntoPequeño"),(160,48,"PuntoPequeño")
        ],

        [
        (48, 32, "PuntoPequeño"), (48, 16, "PuntoPequeño"),
        (32, 16, "PuntoPequeño"), (16, 16, "PuntoPequeño"),
        (16, 32, "PuntoPequeño"), (16, 52, "PuntoPequeño"),
        (16, 70, "PuntoPequeño"), (16, 86, "PuntoPequeño"),
        (16, 102, "PuntoPequeño"), (16, 118, "PuntoPequeño"),
        (16, 136, "PuntoPequeño"), (32, 136, "PuntoPequeño"),
        (48, 136, "PuntoPequeño"), (64, 136, "PuntoPequeño"),
        (80, 136, "PuntoPequeño"), (96, 136, "PuntoPequeño"),
        (112, 118, "PuntoPequeño"), (112, 98, "PuntoPequeño"),
        (112, 80, "PuntoPequeño"), (128, 80, "PuntoPequeño"),
        (144, 80, "PuntoPequeño"), (112, 136, "PuntoPequeño"),
        (128, 136, "PuntoPequeño"), (144, 136, "PuntoPequeño"),
        (160, 136, "PuntoPequeño"), (160, 120, "PuntoPequeño"),
        (160, 100, "PuntoPequeño"), (160, 80, "PuntoPequeño"),
        (16, 168, "PuntoPequeño"), (32, 168, "PuntoGrande"),
        (64, 16, "PuntoPequeño"), (80, 16, "PuntoGrande"),
        (80, 32, "PuntoPequeño"), (96, 32, "PuntoPequeño"),
        (112, 32, "PuntoPequeño"), (80, 32, "PuntoPequeño"),
        (80, 48, "PuntoPequeño"), (80, 64, "PuntoPequeño"),
        (80, 80, "PuntoPequeño"), (96, 80, "PuntoPequeño"),
        (144, 32, "PuntoPequeño"), (80, 98, "PuntoPequeño"),
        (80, 118, "PuntoPequeño"), (64, 152, "PuntoPequeño"),
        (64, 168, "PuntoPequeño"), (80, 168, "PuntoPequeño"),
        (96, 168, "PuntoPequeño"), (96, 184, "PuntoPequeño"),
        (96, 206, "PuntoPequeño"), (96, 224, "PuntoPequeño"),
        (80, 224, "PuntoPequeño"), (64, 224, "PuntoPequeño"),
        (48, 224, "PuntoPequeño"), (32, 224, "PuntoPequeño"),
        (16, 224, "PuntoPequeño"), (16, 206, "PuntoPequeño"),
        (16, 186, "PuntoPequeño"), (112, 224, "PuntoPequeño"),
        (128, 224, "PuntoPequeño"), (144, 224, "PuntoPequeño"),
        (144, 200, "PuntoPequeño"), (144, 184, "PuntoPequeño"),
        (144, 168, "PuntoPequeño"), (144, 152, "PuntoPequeño"),
        (128, 184, "PuntoPequeño"), (112, 184, "PuntoPequeño"),
        (128, 168, "PuntoPequeño"), (160, 200, "PuntoPequeño"),
        (176, 200, "PuntoPequeño"), (176, 224, "PuntoPequeño"),
        (176, 178, "PuntoPequeño"), (192, 178, "PuntoGrande"),
        (208, 224, "PuntoPequeño"), (192, 224, "PuntoPequeño"),
        (208, 200, "PuntoPequeño"), (224, 200, "PuntoPequeño"),
        (224, 184, "PuntoPequeño"), (224, 168, "PuntoPequeño"),
        (224, 152, "PuntoPequeño"), (224, 136, "PuntoPequeño"),
        (224, 120, "PuntoPequeño"), (224, 104, "PuntoPequeño"),
        (224, 88, "PuntoPequeño"), (224, 64, "PuntoPequeño"),
        (208, 64, "PuntoPequeño"), (192, 64, "PuntoPequeño"),
        (160, 64, "PuntoPequeño"), (176, 64, "PuntoPequeño"),
        (224, 48, "PuntoPequeño"), (224, 32, "PuntoPequeño"),
        (208, 32, "PuntoGrande"), (208, 16, "PuntoPequeño"),
        (192, 16, "PuntoPequeño"), (176, 16, "PuntoPequeño"),
        (176, 32, "PuntoPequeño"), (160, 32, "PuntoPequeño"),
        (112, 16, "PuntoPequeño"), (144, 16, "PuntoPequeño"),
        (128, 16, "PuntoPequeño"), (160, 48, "PuntoPequeño")
        ],

        [   
        (48, 32, "PuntoPequeño"), (48, 16, "PuntoPequeño"),
        (32, 16, "PuntoPequeño"), (16, 16, "PuntoPequeño"),
        (16, 32, "PuntoPequeño"), (16, 52, "PuntoPequeño"),
        (16, 70, "PuntoPequeño"), (16, 86, "PuntoPequeño"),
        (16, 102, "PuntoPequeño"), (16, 118, "PuntoPequeño"),
        (16, 136, "PuntoPequeño"), (32, 136, "PuntoPequeño"),
        (48, 136, "PuntoPequeño"), (64, 136, "PuntoPequeño"),
        (80, 136, "PuntoPequeño"), (96, 136, "PuntoPequeño"),
        (112, 118, "PuntoPequeño"), (112, 98, "PuntoPequeño"),
        (112, 80, "PuntoPequeño"), (128, 80, "PuntoPequeño"),
        (144, 80, "PuntoPequeño"), (112, 136, "PuntoPequeño"),
        (128, 136, "PuntoPequeño"), (144, 136, "PuntoPequeño"),
        (160, 136, "PuntoPequeño"), (160, 120, "PuntoPequeño"),
        (160, 100, "PuntoPequeño"), (160, 80, "PuntoPequeño"),
        (16, 168, "PuntoPequeño"), (32, 168, "PuntoGrande"),
        (64, 16, "PuntoPequeño"), (80, 16, "PuntoGrande"),
        (80, 32, "PuntoPequeño"), (96, 32, "PuntoPequeño"),
        (112, 32, "PuntoPequeño"), (80, 32, "PuntoPequeño"),
        (80, 48, "PuntoPequeño"), (80, 64, "PuntoPequeño"),
        (80, 80, "PuntoPequeño"), (96, 80, "PuntoPequeño"),
        (144, 32, "PuntoPequeño"), (80, 98, "PuntoPequeño"),
        (80, 118, "PuntoPequeño"), (64, 152, "PuntoPequeño"),
        (64, 168, "PuntoPequeño"), (80, 168, "PuntoPequeño"),
        (96, 168, "PuntoPequeño"), (96, 184, "PuntoPequeño"),
        (96, 206, "PuntoPequeño"), (96, 224, "PuntoPequeño"),
        (80, 224, "PuntoPequeño"), (64, 224, "PuntoPequeño"),
        (48, 224, "PuntoPequeño"), (32, 224, "PuntoPequeño"),
        (16, 224, "PuntoPequeño"), (16, 206, "PuntoPequeño"),
        (16, 186, "PuntoPequeño"), (112, 224, "PuntoPequeño"),
        (128, 224, "PuntoPequeño"), (144, 224, "PuntoPequeño"),
        (144, 200, "PuntoPequeño"), (144, 184, "PuntoPequeño"),
        (144, 168, "PuntoPequeño"), (144, 152, "PuntoPequeño"),
        (128, 184, "PuntoPequeño"), (112, 184, "PuntoPequeño"),
        (128, 168, "PuntoPequeño"), (160, 200, "PuntoPequeño"),
        (176, 200, "PuntoPequeño"), (176, 224, "PuntoPequeño"),
        (176, 178, "PuntoPequeño"), (192, 178, "PuntoGrande"),
        (208, 224, "PuntoPequeño"), (192, 224, "PuntoPequeño"),
        (208, 200, "PuntoPequeño"), (224, 200, "PuntoPequeño"),
        (224, 184, "PuntoPequeño"), (224, 168, "PuntoPequeño"),
        (224, 152, "PuntoPequeño"), (224, 136, "PuntoPequeño"),
        (224, 120, "PuntoPequeño"), (224, 104, "PuntoPequeño"),
        (224, 88, "PuntoPequeño"), (224, 64, "PuntoPequeño"),
        (208, 64, "PuntoPequeño"), (192, 64, "PuntoPequeño"),
        (160, 64, "PuntoPequeño"), (176, 64, "PuntoPequeño"),
        (224, 48, "PuntoPequeño"), (224, 32, "PuntoPequeño"),
        (208, 32, "PuntoGrande"), (208, 16, "PuntoPequeño"),
        (192, 16, "PuntoPequeño"), (176, 16, "PuntoPequeño"),
        (176, 32, "PuntoPequeño"), (160, 32, "PuntoPequeño"),
        (112, 16, "PuntoPequeño"), (144, 16, "PuntoPequeño"),
        (128, 16, "PuntoPequeño"), (160, 48, "PuntoPequeño")
        ]]

# Datos de los personajes

velocidad_pacman = 2
ListaImagenesPacMan = (
    (0, 96, 32, 16, 16), (0, 96, 48, 16, 16),
    # Derecha 
    (0, 96, 0, 16, 16), (0, 96, 16, 16, 16),
    # Izquierda
    (0, 96, 64, 16, 16), (0, 96, 80, 16, 16),
    # Arriba
    (0, 96, 96, 16, 16), (0, 96, 112, 16, 16),
    # Abajo
)

velocidad_fantasmas = 2
ListaMovimientos = ('derecha', 'izquierda', 'arriba', 'abajo')

ListaImagenesBlinky = (
    (0, 0, 64, 16, 16), (0, 0, 80, 16, 16),
    (0, 0, 0, 16, 16), (0, 0, 16, 16, 16),
    (0, 0, 96, 16, 16), (0, 0, 112, 16, 16),
    (0, 0, 32, 16, 16), (0, 0, 48, 16, 16),
)

ListaImagenesInky = (
    (0, 16, 64, 16, 16), (0, 16, 80, 16, 16),
    (0, 16, 0, 16, 16), (0, 16, 16, 16, 16),
    (0, 16, 96, 16, 16), (0, 16, 112, 16, 16),
    (0, 16, 32, 16, 16), (0, 16, 48, 16, 16),
)

ListaImagenesClyde = (
    (0, 32, 64, 16, 16), (0, 32, 80, 16, 16),
    (0, 32, 0, 16, 16), (0, 32, 16, 16, 16),
    (0, 32, 96, 16, 16), (0, 32, 112, 16, 16),
    (0, 32, 32, 16, 16), (0, 32, 48, 16, 16),
)

ListaImagenesPinky = (
    (0, 48, 64, 16, 16), (0, 48, 80, 16, 16),
    (0, 48, 0, 16, 16), (0, 48, 16, 16, 16),
    (0, 48, 96, 16, 16), (0, 48, 112, 16, 16),
    (0, 48, 32, 16, 16), (0, 48, 48, 16, 16),
)