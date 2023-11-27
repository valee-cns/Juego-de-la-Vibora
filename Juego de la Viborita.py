import pygame
from diseño import *
from funciones import *
from snake import *
from manzanas import *

run = True

#Creación de la tabla para la base de datos

crear_tabla()

#Crear clase nivel para elegir la velocidad del nivel (dificultad)
dificultad = 10

#Empieza el juego
pygame.init()

# defino la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Snake game')

#Defino el timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)

#Defino la fuente
fuente = pygame.font.SysFont('Karma Future', 20)
fuente_2 = pygame.font.SysFont('Karma Future', 40)
fuente_titulo = pygame.font.SysFont('Karma Future', 90)
fuente_titulo_2 = pygame.font.SysFont('Karma Future', 60)

#Defino las imágenes

pantalla_inicio_imagen = definir_imagen("serpiente.jpg", IMAGEN_INICIO)

#Defino la musica

pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("musica.mp3")
sonido_fondo.set_volume(volumen)
sonido_fondo.play(-1)

# Control de FPS
FPS = pygame.time.Clock()

#Defino al personaje

snake = Snake(snake_pos, FOOD_POS, FOOD_SPAWN)
manzana = Manzana()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.USEREVENT:
            if juego == True:
                if event.type == timer_segundos:
                    if fin_timer == False:
                        segundos = int(segundos) - 1

                        if int(segundos) == 0:
                            fin_timer = True
                            fin_del_juego = True
                            segundos = 60

        # Eventos de los botones para el movimiento
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                cambiar_direc = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                cambiar_direc = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                cambiar_direc = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                cambiar_direc = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                run = False
            
            # Eventos de los botones para el nombre de usuario
            if event.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]  # Método slice
            elif event.key == pygame.K_RETURN:
                usuario = ingreso_aux
                ingreso = ""
            else:
                ingreso += event.unicode 
                ingreso_aux = ingreso # Da el texto que se presiona en el teclado
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = list(event.pos)
            if(click[0] > 268 and click[0] < 418) and (click[1] > 273 and click[1] < 297):
                #Pasar a la pantalla niveles
                if pantalla_inicio == True:
                    pantalla_inicio = False
                    ranking = False
                    niveles = True
                    juego = False
                    fin_del_juego = False

            
            if (click[0] > 283 and click[0] < 408) and (click[1] > 323 and click[1] < 347):
                #Pasar a la pantalla ranking
                if pantalla_inicio == True:
                    pantalla_inicio = False
                    ranking = True
                    niveles = False
                    juego = False
                    fin_del_juego = False
            
            if (click[0] > 10 and click[0] < 105) and (click[1] > 430 and click[1] < 460):
                #Boton de volver a la pantalla de inicio desde ranking o niveles
                if ranking == True or niveles == True or fin_del_juego == True:
                    pantalla_inicio = True
                    ranking = False
                    niveles = False
                    juego = False
                    fin_del_juego = False
            
            if (click[0] > 135 and click[0] < 225) and (click[1] > 126 and click[1] < 176):
                #Dificultad facil, pasa a la pantalla el juego
                if niveles == True:
                    dificultad = facil
                    pantalla_inicio = False
                    ranking = False
                    niveles = False
                    juego = True
                    fin_del_juego = False

            if (click[0] > 375 and click[0] < 530) and (click[1] > 126 and click[1] < 176):
                #Dificultad normal, pasa a la pantalla el juego
                if niveles == True:
                    dificultad = normal
                    pantalla_inicio = False
                    ranking = False
                    niveles = False
                    juego = True
                    fin_del_juego = False

            if (click[0] > 135 and click[0] < 290) and (click[1] > 226 and click[1] < 276):
                #Dificultad dificil, pasa a la pantalla el juego
                if niveles == True:
                    dificultad = dificil
                    pantalla_inicio = False
                    ranking = False
                    niveles = False
                    juego = True
                    fin_del_juego = False

            if (click[0] > 375 and click[0] < 585) and (click[1] > 226 and click[1] < 276):
                #Dificultad imposible, pasa a la pantalla el juego
                if niveles == True:
                    dificultad = imposible
                    pantalla_inicio = False
                    ranking = False
                    niveles = False
                    juego = True
                    fin_del_juego = False
            
            if (click[0] > 310 and click[0] < 385) and (click[1] > 370 and click[1] < 400):
                run = False

    #Comienza la distribución del contenido dependiendo de la pantalla en la que se encuentre
    #Pantalla de inicio
    if pantalla_inicio == True:
        pantalla.fill(BLANCO)
        colocar_elemento(pantalla, pantalla_inicio_imagen, POS_IMAGEN_INICIO)
        crear_boton(pantalla, fuente_titulo, "Snake game", FONDO_1_TIT, FONDO_2_TIT, POS_TITULO)
        crear_boton(pantalla, fuente, "Nueva Partida", FONDO_1_NUEVA, FONDO_2_NUEVA, POS_NUEVA)
        crear_boton(pantalla, fuente, "Ver Ranking", FONDO_1_SCORE, FONDO_2_SCORE, POS_SCORE)
        crear_boton(pantalla, fuente, "Salir", FONDO_1_SALIR, FONDO_2_SALIR, POS_SALIR)
        score_mostrado = True
        mostrar_usuario = True
        agregar_contenido = True
        mostrar_contenido = True
        colocar_texto = True
        ingreso_aux = ""
        usuario = ""
        nombre_de_usuario = ""
        score_de_usuario = ""
    
    
    if niveles == True:
        pantalla.fill(BLANCO)
        colocar_elemento(pantalla, pantalla_inicio_imagen, POS_IMAGEN_INICIO)
        crear_boton(pantalla, fuente_titulo_2, "Nivel de Dificultad", FONDO_1_DIFICULTAD, FONDO_2_DIFICULTAD, POS_DIFICULTAD)
        crear_boton(pantalla, fuente_2, "Facil", FONDO_1_FACIL, FONDO_2_FACIL, POS_FACIL)
        crear_boton(pantalla, fuente_2, "Normal", FONDO_1_NORMAL, FONDO_2_NORMAL, POS_NORMAL)
        crear_boton(pantalla, fuente_2, "Dificil", FONDO_1_DIFICIL, FONDO_2_DIFICIL, POS_DIFICIL)
        crear_boton(pantalla, fuente_2, "Imposible", FONDO_1_IMPOSIBLE, FONDO_2_IMPOSIBLE, POS_IMPOSIBLE)
        crear_boton(pantalla, fuente, "Volver", FONDO_1_VOLVER, FONDO_2_VOLVER, POS_VOLVER)
    
    
    if ranking == True:
        pantalla.fill(BLANCO)
        colocar_elemento(pantalla, pantalla_inicio_imagen, POS_IMAGEN_INICIO)
        crear_boton(pantalla, fuente_titulo_2, "Mejores Puntajes", FONDO_1_MEJOR, FONDO_2_MEJOR, POS_MEJOR)
        crear_boton(pantalla, fuente, "Volver", FONDO_1_VOLVER, FONDO_2_VOLVER, POS_VOLVER)

        if mostrar_contenido == True:
            lista_mensajes = mostrar_contenido_de_la_tabla()
            print(lista_mensajes)
            mostrar_contenido = False
        
        for mensaje in lista_mensajes:
            nombre_score = mensaje["datos"]
            posicion_txt = mensaje["posicion_txt"]
            for elemento_1 in nombre_score:
                for elemento_2 in posicion_txt:
                    ranking_txt = elemento_1
                    texto_ranking = crear_texto(fuente_2, ranking_txt, NEGRO)
                    colocar_elemento(pantalla, texto_ranking, (120, elemento_2))

    #Pantalla del juego
    if juego == True:

        if empezo_juego == True:
            snake = Snake(snake_pos, FOOD_POS, FOOD_SPAWN)
            SCORE = 0
            empezo_juego = False
        
        snake_pos, direccion = snake.movimientoSnake(cambiar_direc, direccion)

        snake_cuerpo, SCORE, pos_manzana = snake.crecimientoSerpiente(snake_cuerpo, snake_pos, SCORE)


        pantalla.fill(NEGRO)
        manzana.update(pos_manzana)
        # draw del cuerpo de la serpiente
        snake.draw(pantalla, snake_cuerpo)
        # draw de la comida
        manzana.draw(pantalla)
        # muestro en pantalla el timer
        show_SCORE(pantalla, 1, BLANCO, "Karma Future", 20, SCORE) #Cuando haga las cosas que se muestran o no en pantalla tengo que hacer que este score se muestre sólo durante el juego
        segundos_texto = crear_texto(fuente, "Tiempo: " + str(segundos), BLANCO)
        colocar_elemento(pantalla, segundos_texto, (140, 15))

        # Condiciones del Game Over
        # Colision con los bordes de la pantalla
        if snake_pos[0] < 0 or snake_pos[0] > ANCHO_PANTALLA-10:
            fin_del_juego = True
            juego = False
        if snake_pos[1] < 0 or snake_pos[1] > ALTO_PANTALLA-10:
            fin_del_juego = True
            juego = False
        # Colision con el cuerpo de la serpiente
        snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)  # Rectángulo alrededor de la cabeza
        for block in snake_cuerpo[1:]:
            block_rect = pygame.Rect(block[0], block[1], 10, 10)  # Rectángulo alrededor de cada parte del cuerpo
            if snake_rect.colliderect(block_rect):
                fin_del_juego = True
                juego = False

    if fin_del_juego == True:
        game_over(pantalla, SCORE, ingreso)
        if score_mostrado == True:
            score_de_usuario = str(SCORE)
            score_mostrado = False

        if usuario != "" and mostrar_usuario == True:
            nombre_de_usuario = str(usuario)
            mostrar_usuario = False
        
        if score_mostrado == False and mostrar_usuario == False:
            if agregar_contenido == True:
                agregar_datos_de_usuario(nombre_de_usuario, score_de_usuario)
                agregar_contenido = False
        juego = False
        niveles = False
        pantalla_inicio = False
        ranking = False
        empezo_juego = True
        snake_pos = [100, 50]
        snake_cuerpo = [[100, 50], [100-10, 50], [100-(2*10), 50]]

        direccion = 'RIGHT'
        cambiar_direc = direccion

        #Variables de la comida

        FOOD_POS = [random.randrange(1, (ANCHO_PANTALLA//10)) * 10, random.randrange(1, (ALTO_PANTALLA//10)) * 10]
        FOOD_SPAWN = True

        #Timer

        segundos = "10"
        fin_timer = False

    #print(pantalla_inicio, niveles, juego, fin_del_juego)
    # Define la dificualtad del nivel con los FPS
    FPS.tick(dificultad)

    pygame.display.flip()

sonido_fondo.stop()

pygame.quit()
