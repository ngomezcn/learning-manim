
class Posicion():
    
    x = None
    y = None
    
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        
class Entidad():
    
    pos = None
    velocidad = None 
    masa = None
    coeficiente_restitución = None
    
    en_caida = False
    
    def __init__(self, 
                 x=0, 
                 y=0, 
                 velocidad=0, 
                 masa=0, 
                 coeficiente_restitución = 1,
                 en_caida = False):
        self.pos = Posicion(x,y)
        self.velocidad = velocidad
        self.masa = masa
        self.coeficiente_restitución = coeficiente_restitución
        self.en_caida = en_caida
        
    max_pos_y = None
    def calcular_maxima_posicion_y(self):
        if(self.max_pos_y == None):
            self.max_pos_y = self.pos.y
        else:
            if(self.pos.y > self.max_pos_y):
                self.max_pos_y = self.pos.y
                
    max_velocidad = None
    def calcular_maxima_velocidad(self):
        if(self.max_velocidad == None):
            self.max_velocidad = self.velocidad
        else:
            if(self.velocidad > self.max_velocidad):
                self.max_velocidad = self.velocidad
   
        
    
    
    