from doctest import FAIL_FAST
from pickle import TRUE
from time import sleep
from Fisica import *

entidad = Entidad(x=0, y=5, velocidad=0, masa=1)

posicion_inicial = entidad.pos.y
velocidad_inicial = entidad.velocidad
xd = TRUE
while(True):
    t = time.time() - START_TIME
        
    entidad.pos.y = mrua.ecuaciones_horarias.posicion(tiempo=t, aceleracion=GRAVEDAD_TIERRA_NEGATIVO, posicion_inicial=posicion_inicial, velocidad_inicial=velocidad_inicial)
    entidad.velocidad = mrua.ecuaciones_horarias.velocidad(tiempo=t, aceleracion=GRAVEDAD_TIERRA_NEGATIVO, velocidad_inicial=velocidad_inicial)

    print(round(t, 1),"altura:", round(entidad.pos.y, 2), round(entidad.velocidad, 2))

    if(entidad.pos.y <= 0 and t != 0 and xd): 
        posicion_inicial = entidad.pos.y
        velocidad_inicial = 5
        START_TIME = time.time()
        
    
    entidad.calcular_maxima_posicion_y()
    entidad.calcular_maxima_velocidad()
    
    sleep(0.1)

print("max_pos_y:", entidad.max_pos_y)
print("max_velocidad:", entidad.max_velocidad)