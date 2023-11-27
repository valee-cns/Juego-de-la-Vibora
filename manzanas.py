import pygame
from diseño import *
from funciones import *

class Manzana:
    def __init__(self):
        self.movimiento_manzana = obtener_superficie_desde_sprite("manzana.png", 3, 1)
        self.frame = 0
        self.animacion = self.movimiento_manzana
        self.imagen = self.animacion[self.frame]
        self.manzana_pos = FOOD_POS

    def aparicion_comida(self, food_spawn):
        if not food_spawn:
            self.manzana_pos = (random.randrange(1, ANCHO_PANTALLA // 17) * 17, random.randrange(1, ALTO_PANTALLA // 15) * 15)
            food_spawn = True

        return self.manzana_pos, food_spawn
    
    def update(self, nueva_posicion):
        if(self.frame < len(self.animacion) - 1):
            self.frame = self.frame + 1
            
        else:
            self.frame = 0

        self.manzana_pos = nueva_posicion

    def draw(self, pantalla):
        self.animacion = self.movimiento_manzana
        self.imagen = self.animacion[self.frame]
        pantalla.fill((0, 0, 0), pygame.Rect(self.manzana_pos[0], self.manzana_pos[1], self.imagen.get_width(), self.imagen.get_height()))
        pantalla.blit(self.imagen, self.manzana_pos)