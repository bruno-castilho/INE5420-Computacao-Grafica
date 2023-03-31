import math

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
    
    def rotation(grau):
        #Cria matriz de rotação.
        matrix_rotation = [
                  [math.cos(math.radians(grau)),-1*math.sin(math.radians(grau)),0],
                  [math.sin(math.radians(grau)),math.cos(math.radians(grau)),0],
                  [0,0,1]
                  ]
           
        return matrix_rotation
