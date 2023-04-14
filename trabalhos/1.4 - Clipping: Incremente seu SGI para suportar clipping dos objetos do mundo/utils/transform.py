import math
from globals import *

class Transform():
    """
    ...
        Uma classe estática para gerar as matrizes de transformação.
    ...
    
    Métodos
    -------
        translation(float: dx, float: dy) -> List:
            Retorna matriz de translação.
            
        scale(float: sx, float: sy) -> List:
            Retorna matriz de escalonamento.

        rotation(float: grau) -> List:
            Retorna matriz de rotação.
        
    """
    def translation(dx, dy):
        #Cria matriz de translação.
        matrix_transition = [
                  [1,0,0],
                  [0,1,0],
                  [dx,dy,1]
                  ]
           
        return matrix_transition
    
    def scale(sx, sy):        
        #Cria matriz de escalonamento.
        matrix_scaling = [
                  [sx,0,0],
                  [0,sy,0],
                  [0,0,1]
                  ]
        
        return matrix_scaling
    
    def rotation(angle):
        #Cria matriz de rotação.
        matrix_rotation = [
                  [math.cos(math.radians(angle)),-1*math.sin(math.radians(angle)),0],
                  [math.sin(math.radians(angle)),math.cos(math.radians(angle)),0],
                  [0,0,1]
                  ]
        
        return matrix_rotation

        

        




