from globals import *
from utils.transform import Transform
from utils.object import Object

class Normalization():
    """
    ...
        Uma classe estática para converter o SCW para SCN.
    ...
    
    Métodos
    -------
        matrixSWNtoSCN() -> List:
            Gera matriz de normalização.
            
        normalize() -> None:
            Normaliza objetos e adiciona no displayfile.        
    """
    def matrixSWNtoSCN():
        #Centro da window.
        cx, cy = window.getCenter()

        #Angulo que a window está rotacionada em relação ao mundo.
        angle = window.getAngle()
        
        #pontos da window no mundo.
        window_points = window.getPoints()
        
        #Tamanho da window.
        xw = ((window_points[0][0]-window_points[3][0])**2 + (window_points[0][1]-window_points[3][1])**2)**0.5
        yw = ((window_points[0][0]-window_points[1][0])**2 + (window_points[0][1]-window_points[1][1])**2)**0.5
        
        #Matriz de translação.
        matrix_translation = Transform.translation(-cx,-cy)

        #Matriz de rotação.
        matrix_rotation = Transform.rotation(angle)

        #Matriz de escala.
        matrix_scaling = Transform.scale(2/xw, 2/yw)
        
        #Matriz de translação x matrix_rotation
        matrix_translation_rotation = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation)] 
                                            for A_row in matrix_translation] 

        #Matriz de translação x matrix_rotation x matrix_scaling
        matrix_translation_rotation_scaling =  [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_scaling)] 
                                                    for A_row in matrix_translation_rotation] 
        
        return matrix_translation_rotation_scaling
    
    def normalize():
        #Dicionario para adicionar objetos normalizados.
        CN = {}

        #Matriz de normalização.
        matrixSWNtoSCN = Normalization.matrixSWNtoSCN()

        #Normaliza objetos.
        for object_name in displayfile['CW'].keys():
            object = displayfile['CW'][object_name]
            type  = object.getType()
            points = object.getPoints()
            color = object.getColor()
            closed = object.isClosed()

            new_points = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrixSWNtoSCN)] 
                                    for A_row in points]
            
            
            CN[object_name] = Object(object_name,type,new_points,color,closed)

        #Adiciona objetos normalizados no displayfile.
        displayfile['CN'] = CN

        

        
        
        
