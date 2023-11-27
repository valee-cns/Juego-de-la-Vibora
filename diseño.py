import random
import pygame

#Pantalla

ANCHO_PANTALLA = 720
ALTO_PANTALLA = 480

#Imagenes

IMAGEN_INICIO = (720, 480)
POS_IMAGEN_INICIO = (0, 0)

#Volumen

volumen = 0.12

#Titulo
POS_TITULO = (100, 100)
FONDO_1_TIT = (95, 115, 535, 105)
FONDO_2_TIT = (100, 120, 525, 95)

#Botones
POS_NUEVA = (270, 270)
FONDO_1_NUEVA = (265, 270, 155, 30)
FONDO_2_NUEVA = (268, 273, 150, 24)

POS_SCORE = (285, 320) 
FONDO_1_SCORE = (280, 320, 130, 30) 
FONDO_2_SCORE = (283, 323, 125, 24)

POS_SALIR = (320, 370) 
FONDO_1_SALIR = (310, 370, 75, 30) 
FONDO_2_SALIR = (313, 373, 70, 24)

POS_MEJOR = (95, 10) 
FONDO_1_MEJOR = (90, 20, 555, 70) 
FONDO_2_MEJOR = (93, 22, 550, 64)

POS_VOLVER = (15, 430) 
FONDO_1_VOLVER = (10, 430, 85, 30) 
FONDO_2_VOLVER = (13, 432, 80, 24)

POS_DIFICULTAD = (85, 10) 
FONDO_1_DIFICULTAD = (80, 20, 605, 70) 
FONDO_2_DIFICULTAD = (83, 22, 600, 64)

POS_FACIL = (140, 120) 
FONDO_1_FACIL = (135, 126, 120, 50) 
FONDO_2_FACIL = (137, 128, 115, 44)

POS_NORMAL = (380, 120) 
FONDO_1_NORMAL = (375, 126, 155, 50) 
FONDO_2_NORMAL = (377, 128, 150, 44)

POS_DIFICIL = (140, 220) 
FONDO_1_DIFICIL = (135, 226, 155, 50) 
FONDO_2_DIFICIL = (137, 228, 150, 44)

POS_IMPOSIBLE = (380, 220) 
FONDO_1_IMPOSIBLE = (375, 226, 210, 50) 
FONDO_2_IMPOSIBLE = (377, 228, 205, 44)

#Dificultad del Juego

facil = 10
normal = 25
dificil = 40
imposible = 60

#Colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Variables de la serpiente

snake_pos = [100, 50]
snake_cuerpo = [[100, 50], [100-10, 50], [100-(2*10), 50]]

direccion = 'RIGHT'
cambiar_direc = direccion

#Variables de la comida

FOOD_POS = [random.randrange(1, (ANCHO_PANTALLA//10)) * 10, random.randrange(1, (ALTO_PANTALLA//10)) * 10]
FOOD_SPAWN = True

#score

SCORE = 0

#Timer

segundos = "10"
fin_timer = False

#Inicialización de las pantallas

pantalla_inicio = True
ranking = False
niveles = False
fin_del_juego = False
juego = False
empezo_juego = False
score_mostrado = True
mostrar_usuario = True
agregar_contenido = True
mostrar_contenido = True
colocar_texto = True

#Inicialización de los elementos del nombre de usuario

ingreso = ""
usuario = ""
ingreso_aux = ""
INGRESO_RECT = (210,300,300,40)
POS_TEXTO = (215, 305)

nombre_de_usuario = ""
score_de_usuario = ""

renglon = 50

POS_Y = 100