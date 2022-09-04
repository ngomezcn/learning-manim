import sys, pygame
from turtle import circle
from pygame import gfxdraw
import time
from Fisica import *
from Fisica import AUMENTO_APLICADO
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

pygame.init()

def to_pygame(coords, height, obj_height):
    """Convert an object's coords into pygame coordinates (lower-left of object => top left in pygame coords)."""
    return (coords[0], height - coords[1] - obj_height)

size = width, height = 300, 800
screen = pygame.display.set_mode(size)

# Entidad fisica
entidad = Entidad(x=130*AUMENTO_APLICADO, y=3*AUMENTO_APLICADO, velocidad=0, masa=1, coeficiente_restitución=0.9, en_caida=True)
posicion_inicial = entidad.pos.y
velocidad_inicial = entidad.velocidad


START_TIME = time.time()
GLOBAl_TIME = START_TIME

altura_arr = []
tiempo_arr = []

sonido = True
while 1:
    t = time.time() - START_TIME
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    if(entidad.en_caida):
        
        altura_arr.append(entidad.pos.y)
        tiempo_arr.append(time.time() - GLOBAl_TIME)
        
        entidad.pos.y = mrua.ecuaciones_horarias.posicion(tiempo=t, aceleracion=GRAVEDAD_TIERRA_NEGATIVO, posicion_inicial=posicion_inicial, velocidad_inicial=velocidad_inicial)
        entidad.velocidad = mrua.ecuaciones_horarias.velocidad(tiempo=t, aceleracion=GRAVEDAD_TIERRA_NEGATIVO, velocidad_inicial=velocidad_inicial)
   
        #collide = rect.collidepoint((0, to_pygame((200,entidad.pos.y), 800, 10)[1]))
        if(entidad.pos.y <= 0 and t > 0.005):
            
            ep = cinematica.energia_potencial(entidad.masa, GRAVEDAD_TIERRA_NEGATIVO, entidad.pos.y)
            ec = cinematica.energia_cinetica(entidad.masa, entidad.velocidad)
            em = cinematica.energia_mecanica(ep, ec)

            u1 = cinematica.velocidad_antes_del_choque(entidad.max_pos_y, GRAVEDAD_TIERRA_POSITIVO, entidad.velocidad) # Velocidad de la pelota antes del choque

            v1 = entidad.coeficiente_restitución*u1 # Velocidad de la pelota despues del choque
        
            posicion_inicial = 0
            velocidad_inicial = v1
            
            #print( "t", t, "ep", round(ep, 2), "ec", round(ec, 2), "em", round(em, 2), "u1", round(u1, 2), "v1", round(v1, 2), "velocidad:", round(entidad.velocidad, 2))
            START_TIME = time.time()
            entidad.max_pos_y = 0
            
            if(v1 > 3 and sonido):
                crash_sound = pygame.mixer.Sound("D:\GitRepos\learning-manim\Physics\clack.wav")
                crash_sound.set_volume(100*(v1/100000))
                #pygame.mixer.Sound.play(crash_sound)
            else:
                sonido = False
                
            if(v1 < 1.5 or u1 < 1):
                entidad.en_caida = False
                
                fig, ax = plt.subplots()
                ax.plot(tiempo_arr, altura_arr)

                ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
                ax.grid()

                fig.savefig("test.png")
                plt.show()
        
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(0, 799, 300, 1))
    pygame.draw.circle(screen, (255,0,0), to_pygame((200,entidad.pos.y), 800, 50), 50)
    pygame.display.flip()
    
    entidad.calcular_maxima_posicion_y()
    entidad.calcular_maxima_velocidad()
    
