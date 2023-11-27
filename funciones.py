import pygame
from diseño import *
import sqlite3

#Funciones para elementos gráficos

def crear_texto(fuente, texto:str, color:tuple):
    texto = fuente.render(texto, True, color)

    return texto

def definir_imagen(ruta_de_acceso:str, tamaño_imagen:tuple):
    imagen = pygame.image.load(ruta_de_acceso)
    imagen = pygame.transform.scale(imagen, tamaño_imagen)

    return imagen

def colocar_elemento(pantalla, elemento, posicion:tuple):
    pantalla.blit(elemento, posicion)

def dibujar_rectangulo(pantalla, color:tuple, posicion:tuple, radio:int):
    pygame.draw.rect(pantalla, color, posicion, border_radius=radio)

#Botones

def crear_boton(pantalla, fuente, texto:str, pos_rec_1:tuple, pos_rec_2:tuple, pos_texto:tuple):
    dibujar_rectangulo(pantalla, VERDE, pos_rec_1, 3)
    dibujar_rectangulo(pantalla, BLANCO, pos_rec_2, 2)
    texto_nueva_partida = crear_texto(fuente, texto, NEGRO)
    colocar_elemento(pantalla, texto_nueva_partida, pos_texto)

def obtener_superficie_desde_sprite(nombre_archivo:str, columnas:int, filas:int, flip=False):
    lista = []
    imagen = pygame.image.load(nombre_archivo)
    imagen = pygame.transform.scale(imagen, (104, 30))
    fotograma_ancho = int(imagen.get_width()/columnas)
    fotograma_alto = int(imagen.get_height()/filas)
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            fotograma = imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            fotograma = pygame.transform.flip(fotograma, flip, False)
            lista.append(fotograma)
    return lista

#Mostrar pantalla de que perdió

def game_over(pantalla, score, nombre):
    fuente_titulo = pygame.font.SysFont('Karma Future', 90)
    fuente = pygame.font.SysFont('Karma Future', 20)
    texto = fuente_titulo.render('YOU DIED', True, ROJO)
    game_over_rect = texto.get_rect()
    game_over_rect.midtop = (ANCHO_PANTALLA/2, ALTO_PANTALLA/4)
    pantalla.fill(NEGRO)
    pantalla.blit(texto, game_over_rect)
    show_SCORE(pantalla, 0, ROJO, 'Karma Future', 20, score)
    crear_boton(pantalla, fuente, "Salir", FONDO_1_SALIR, FONDO_2_SALIR, POS_SALIR)
    crear_boton(pantalla, fuente, "Volver", FONDO_1_VOLVER, FONDO_2_VOLVER, POS_VOLVER)

    dibujar_rectangulo(pantalla, BLANCO, INGRESO_RECT, 2)
    nombre_txt = crear_texto(fuente, nombre, ROJO)
    colocar_elemento(pantalla, nombre_txt, POS_TEXTO)

#Mostrar por pantalla el score

def show_SCORE(pantalla, choice, color, tipofuente, tamaño, score):
    fuente = pygame.font.SysFont(tipofuente, tamaño)
    score = fuente.render('SCORE : ' + str(score), True, color)
    score_rect = score.get_rect()
    if choice == 1:
        score_rect.midtop = (ANCHO_PANTALLA/10, 15)
    else:
        score_rect.midtop = (ANCHO_PANTALLA/2, ALTO_PANTALLA/2)
    pantalla.blit(score, score_rect)

#Funciones para crear base de datos

def crear_tabla():
    with sqlite3.connect("Datos de Usuario.db") as conexion:
        try:
            sentencia = ''' create table usuarios
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            score real
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla usuarios")
        except sqlite3.OperationalError:
            print("La tabla usuarios ya existe")


#Función para agregar contenido a tabla (nombre y score)

def agregar_datos_de_usuario(nombre, score):
    with sqlite3.connect("Datos de Usuario.db") as conexion:
        try:
            conexion.execute("insert into usuarios(nombre, score) values (?,?)", (nombre, score))
            conexion.commit() # Actualiza los datos realmente en la tabla
        except:
            print("Error")


#Mostrar lo que hay en la tabla

def mostrar_contenido_de_la_tabla():
    lista_mensajes = []
    bandera = True
    with sqlite3.connect("Datos de Usuario.db") as conexion:
        cursor=conexion.execute("SELECT nombre, score FROM usuarios")
        for fila in cursor:
            mensaje_final = ""
            dic = {}
            if bandera == True:
                POS_Y = 100
                bandera = False
            
            else:
                POS_Y = POS_Y + 50
            datos = list(fila)
            print(datos)

            if len(datos) > 0:
                for elemento in datos:
                    mensaje = "{0}".format(elemento)
                    mensaje_final = mensaje_final + mensaje
                dic["datos"] = [mensaje_final]
                dic["posicion_txt"] = [POS_Y]
                lista_mensajes.append(dic)
            
            else:
                lista_mensajes = []
    
    return lista_mensajes

