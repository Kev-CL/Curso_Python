import pygame
import math
import random
from pygame import mixer
# *******************************************************************
# Inicializar pygame
pygame.init()
# Variables
# Crear ventana
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('icono.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('espacio.jpg')

# Audio
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
puntaje_x = 10
puntaje_y = 10

# Game Over
fuente_GameOver = pygame.font.Font('freesansbold.ttf',40)

# Jugador (nave)
imagen_jugador = pygame.image.load('nave_espacial.png')
jugador_x = 368 # Valor x inicial
jugador_y = 526 # Valor y inicial
velocidad_nave = 0.5
jugador_x_cambio = 0

# Enemigo
velocidad_enemigo = 1
imagen_enemigo = []
enemigo_x = [] # Valor x inicial
enemigo_y = [] # Valor y inicial
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8
for e in range(cantidad_enemigos):
    imagen_enemigo.append(pygame.image.load('nave_enemiga.png'))
    enemigo_x.append(random.randint(0, 736)) # Valor x inicial
    enemigo_y.append(random.randint(0, 200))# Valor y inicial
    enemigo_x_cambio.append(velocidad_enemigo)
    enemigo_y_cambio.append(50)

# Bala
imagen_bala = pygame.image.load('bala.png')
bala_x = 0 # Valor x inicial
bala_y = 500 # Valor y inicial
velocidad_bala = 5
bala_x_cambio = 0
bala_y_cambio = velocidad_bala
bala_visible = False


# ****************************************************************
# Funcion jugador
def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))


# Funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(imagen_enemigo[ene], (x, y))


# Funcion bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(imagen_bala, (x + 16, y + 10))


# Detectar colisiones
def colision(x1,y1,x2,y2):
    distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Mostrar puntaje
def marcador(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def game_over():
    texto_gameOver = fuente_GameOver.render('GAME OVER', True, (255, 255, 255))
    pantalla.blit(texto_gameOver, (300, 200))
# **************************************************************
# Loop del juego
salir = True    # Boton salir (X)

while salir:
    #pantalla.fill((146, 74, 189))       # RGB de pantalla
    pantalla.blit(fondo, (0, 0))
    # Iteración de eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:  # Hasta que se presione salir terminará.
            salir = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1 * velocidad_nave
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = velocidad_nave
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación de jugador
    jugador_x += jugador_x_cambio
    #   Mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 736:
        jugador_x = 736
    jugador(jugador_x, jugador_y)

    # Modificar ubicación de enemigo
    for e in range(cantidad_enemigos):
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            game_over()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
        #   Mantener dentro de bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = velocidad_enemigo
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1*velocidad_enemigo
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        hay_colision = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if hay_colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    # Actualización
    marcador(puntaje_x,puntaje_y)
    pygame.display.update()
