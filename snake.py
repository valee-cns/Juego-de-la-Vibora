import pygame
from manzanas import *

class Snake:
    def __init__(self, snake_pos, food_pos, food_spawn):
        self.snake_pos = snake_pos
        self.manzana_pos = food_pos
        self.food_spawn = food_spawn
        self.manzana = Manzana()

    def movimientoSnake(self, cambiar_direc, direccion):
        # Verificación de que la serpiente no se mueva para dos lados opuestos
        if cambiar_direc == 'UP' and direccion != 'DOWN':
            direccion = 'UP'
        if cambiar_direc == 'DOWN' and direccion != 'UP':
            direccion = 'DOWN'
        if cambiar_direc == 'LEFT' and direccion != 'RIGHT':
            direccion = 'LEFT'
        if cambiar_direc == 'RIGHT' and direccion != 'LEFT':
            direccion = 'RIGHT'

        # movimiento de la serpiente
        if direccion == 'UP':
            self.snake_pos[1] -= 10
        if direccion == 'DOWN':
            self.snake_pos[1] += 10
        if direccion == 'LEFT':
            self.snake_pos[0] -= 10
        if direccion == 'RIGHT':
            self.snake_pos[0] += 10

        return self.snake_pos, direccion
    
    def crecimientoSerpiente(self, snake_cuerpo, snake_pos, score):
        snake_cuerpo.insert(0, list(snake_pos))
        snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)  # Rectángulo alrededor de la cabeza
        food_rect = pygame.Rect(self.manzana.manzana_pos[0], self.manzana.manzana_pos[1], self.manzana.imagen.get_width(), self.manzana.imagen.get_height())  # Rectángulo alrededor de la comida
        if snake_rect.colliderect(food_rect):
            score += 1
            self.food_spawn = False
        else:
            snake_cuerpo.pop()
        
        self.manzana_pos, self.food_spawn = self.manzana.aparicion_comida(self.food_spawn)

        return snake_cuerpo, score, self.manzana_pos

    def draw(self, pantalla, snake_cuerpo):
        for pos in snake_cuerpo:
            pygame.draw.rect(pantalla, VERDE, pygame.Rect(pos[0], pos[1], 10, 10))