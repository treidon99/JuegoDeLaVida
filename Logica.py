import pygame
import sys
import time
from copy import deepcopy
play = True

#Paleta de colores
negro =(86,86,86)
verde = (255,255,255)
blanco = (255,255,255)


#Creacion del tablero
Ancho = 20
Largo = 20
Matriz = []
for i in range(Largo):
    Matriz.append([])
    for j in range(Ancho):
        Matriz[i].append(0)

#Creacion ventana
pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Juego de la vida')

#Color fondo
ventana.fill(blanco)

#Pintado
def ActualizarPantalla ():
    for i in range(Largo):
        for j in range(Ancho):
            if Matriz[i][j]==1:
                pygame.draw.rect(ventana, verde, (i*30,j*30,30,30))
                pygame.draw.rect(ventana, negro, (i*30,j*30,30,30),1)
            elif Matriz[i][j]==0:
                pygame.draw.rect(ventana, negro, (i*30,j*30,30,30))
                pygame.draw.rect(ventana, blanco, (i*30,j*30,30,30),1)

def reglas():
    Matriz2 = deepcopy(Matriz)
    for i in range(Largo):
        for j in range(Ancho):
            suma_vecinos = 0
            suma_vecinos = Matriz2[(i-1)%20][(j-1)%20] + Matriz2[(i-1)%20][(j)%20] + Matriz2[(i-1)%20][(j+1)%20] \
            + Matriz2[(i)%20][(j-1)%20] + Matriz2[(i)%20][(j+1)%20] + Matriz2[(i+1)%20][(j-1)%20]\
            + Matriz2[(i+1)%20][(j)%20] +Matriz2[(i+1)%20][(j+1)%20]  

            if Matriz[i][j] == 1:   
                if suma_vecinos == 2 or suma_vecinos == 3:
                    Matriz[i][j] = 1
                elif suma_vecinos > 3 or suma_vecinos < 2:
                    Matriz[i][j] = 0
            if Matriz[i][j] == 0:   
                if suma_vecinos == 3:
                    Matriz[i][j] = 1

# def debug():
#     for i in range(Largo):
#         for j in range(Ancho):
#             suma_vecinos = 0
#             suma_vecinos = Matriz[(i-1)%20 ][(j-1)%20] + Matriz[(i-1)%20][(j)%20] + Matriz[(i-1)%20][(j+1)%20] + Matriz[(i)%20][(j-1)%20] + Matriz[(i)%20][(j+1)%20] + Matriz[(i+1)%20][(j-1)%20] + Matriz[(i+1)%20][(j)%20] +Matriz[(i+1)%20][(j+1)%20]  
#             if suma_vecinos != 0:
#                 print(suma_vecinos,i,j)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                play = not play
            # elif evento.key == pygame.K_UP:
            #     debug()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Clic izquierdo del mouse
            x, y = evento.pos
            # Calcular los índices de matriz según las coordenadas del clic
            j = y // 30
            i = x // 30
            if Matriz[i][j] == 1:
                Matriz[i][j] = 0
                pygame.draw.rect(ventana, negro, (i*30,j*30,30,30))
                pygame.draw.rect(ventana, blanco, (i*30,j*30,30,30),1)
            elif Matriz[i][j] == 0:
                Matriz[i][j] = 1
                pygame.draw.rect(ventana, verde, (i*30,j*30,30,30))
                pygame.draw.rect(ventana, negro, (i*30,j*30,30,30),1)


    if play:        
        ActualizarPantalla()
        reglas()
    pygame.display.update()
    time.sleep(0.05)


