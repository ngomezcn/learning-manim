from Fisica import *




# Iniciamos Entidad
entidad = Entidad(x=0, y=3, velocidad=0, masa=1)

e = 0.9 # Coeficiente de restitucion
ep = cinematica.energia_potencial(entidad.masa, GRAVEDAD_TIERRA_POSITIVO, entidad.pos.y)
ec = cinematica.energia_cinetica(entidad.masa, entidad.velocidad)
em = cinematica.energia_mecanica(ep, ec)

u1 = cinematica.velocidad_antes_del_choque(entidad.pos.y) # Velocidad de la pelota antes del choque

v1 = e*u1 # Velocidad de la pelota despues del choque

print(v1)
