from cmath import sqrt
import time
from traceback import print_tb
import matplotlib.pyplot as plt
import math 

START_TIME = time.time()

GRAVEDAD_TIERRA_POSITIVO = 9.807 # m/s
GRAVEDAD_TIERRA_NEGATIVO= -9.807 # m/s

AUMENTO_APLICADO = 1

GRAVEDAD_TIERRA_POSITIVO *= AUMENTO_APLICADO
GRAVEDAD_TIERRA_NEGATIVO *= AUMENTO_APLICADO

class mrua():
    
    
    """
    Las ecuaciones horarias son siempre las de posición, velocidad y aceleración en función
    del tiempo.
    """
    class ecuaciones_horarias():  
    
        def posicion(
                    tiempo, 
                    aceleracion = float, # m/s^2 
                    posicion_inicial = float, # m
                    velocidad_inicial = .0): # m/s
            posicion = posicion_inicial + velocidad_inicial * tiempo + (1/2) * aceleracion * (tiempo*tiempo)
            return posicion # m
         
        def velocidad(
                    tiempo = float, 
                    aceleracion = float, # m/s^2 
                    velocidad_inicial = .0, # m/s
                    velocidad_positiva=False): # m/s
            vel = velocidad_inicial + aceleracion * tiempo
            
            # if(vel < 0 and velocidad_positiva):
            #   vel *= -1
                        
            return vel # m/s
        
class cinematica():
        
        def energia_cinetica(masa = float, # kg
                             velocidad = float): # m/s
            
            ec = (1/2)*masa*(velocidad*velocidad)
            return ec # J
        
        def energia_potencial(masa = float, # kg
                              gravedad = GRAVEDAD_TIERRA_POSITIVO, # m/s^2                           
                              altura = float): # m
            
            ep = masa * gravedad * altura
            return ep # J
        
        '''
        def velocidad(masa = float, # kg
                      energia_cinetica = float # J
                      ):
            
            vel = math.sqrt((2*energia_cinetica) / masa)
            return vel
        '''
        
        def velocidad_antes_del_choque(altura, # m
                               aceleracion = GRAVEDAD_TIERRA_POSITIVO,
                               velocidad = 0
                               ): # m/s^2
            u1 = math.sqrt((2*aceleracion*altura))
            return u1

        def energia_mecanica(energia_potencial, # J
                            energia_cinetica): # J
            em = energia_potencial + energia_cinetica
            return em # J ???
