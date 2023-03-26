import math

class Transform():
    """
    ...
        Uma classe estática para calcular transformações em pontos.
    ...
    
    Métodos
    -------
        translation(list: points, float: dx, float: dy) -> List:
            Retorna matriz com os pontos transladados.
            
        scale(list: points, float: sx, float: sy) -> List:
            Retorna matriz com os pontos escalonados.

        rotation(points, grau, x, y) -> List:
            Retorna matriz com os pontos rotacionados.
        
    """
    def translation(points, dx, dy):
        #Matriz de translação
        matrix_transition = [
                  [1,0,0],
                  [0,1,0],
                  [dx,dy,1]
                  ]
        
        #points x matrix_transition
        result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition)] 
                                for A_row in points] 
   
        return result
    
    def scale(points, sx, sy):
        cx = sum(point[0]/len(points) for point in points)
        cy = sum(point[1]/len(points) for point in points)
        
        #Matriz de translação que move o centro do objeto para origem.
        matrix_transition_origin = [
                  [1,0,0],
                  [0,1,0],
                  [-1*cx,-1*cy,1]
                  ]
        
        #Matriz de escalonamento.
        matrix_scaling = [
                  [sx,0,0],
                  [0,sy,0],
                  [0,0,1]
                  ]
        
        #Matriz de translação que move o centro do objeto para o seu ponto inicial.
        matrix_transition_initial = [
                  [1,0,0],
                  [0,1,0],
                  [cx,cy,1]
                  ]
        
        #points x matrix_transition_origin
        matriz_1_2 = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition_origin)] 
                                for A_row in points] 
        
        #points x matrix_transition_origin x matrix_scaling X 
        matriz_1_2_3 = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_scaling)] 
                                for A_row in matriz_1_2] 
        
        #points x matrix_transition_origin x matrix_scaling X matrix_transition_initial
        result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition_initial)] 
                                for A_row in matriz_1_2_3]
        
        return result
    
    def rotation(points, grau, x, y):
        dx = x - 0
        dy = y - 0
        
        #Matriz de translação que move objeto para um ponto qualquer.
        matrix_transition_point = [
                  [1,0,0],
                  [0,1,0],
                  [-1*dx,-1*dy,1]
                  ]
        #Matriz de rotação.
        matrix_rotation = [
                  [math.cos(math.radians(grau)),-1*math.sin(math.radians(grau)),0],
                  [math.sin(math.radians(grau)),math.cos(math.radians(grau)),0],
                  [0,0,1]
                  ]
        
        #Matriz de translação que move o objeto para o seu ponto inicial.
        matrix_transition_initial = [
                  [1,0,0],
                  [0,1,0],
                  [dx,dy,1]
                  ]
        
        #points x matrix_transition_point
        matriz_1_2 = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition_point)] 
                                for A_row in points] 
        
        #points x matrix_transition_point x matrix_rotation
        matriz_1_2_3 = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_rotation)] 
                                for A_row in matriz_1_2] 
        
        #points x matrix_transition_point x matrix_rotation x matrix_transition_initial
        result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition_initial)] 
                                for A_row in matriz_1_2_3]
   
        return result
