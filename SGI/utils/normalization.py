from globals import *
from utils.transform import Transform
from utils.object import Object
from utils.clipping import Clipping
from utils.curves import Curves

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
    def matrixSWNtoSCN(window_points):
        #Centro da window.
        cx = sum(point[0]/len(window_points) for point in window_points)
        cy = sum(point[1]/len(window_points) for point in window_points)

        #Angulo que a window está rotacionada em relação ao mundo.
        angle = window.getAngle()
        
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
    
    def normalize(objects, window_points):
        #Dicionario para adicionar objetos normalizados.
        CN = []

        #Matriz de normalização.
        matrixSWNtoSCN = Normalization.matrixSWNtoSCN(window_points)

        #Normaliza objetos.
        for object in objects:
            type  = object[0]
            points = object[1]

            new_points = [[sum(a * b for a, b in zip([A_row[0],A_row[1],1], B_col))  
                                for B_col in zip(*matrixSWNtoSCN)] 
                                    for A_row in points]
            
        
            if type == 0:
                new_points = Clipping.point(new_points)
                if new_points: 
                    CN.append([0, new_points])

            elif type == 1:
                if Mode_clipping['value'] == 'Liang Barsky':
                    new_points = Clipping.Liang_Barsky(new_points)
                else: 
                    new_points = Clipping.Cohen_Sutherland(new_points)
                
                if new_points: 
                    CN.append([1, new_points])
        
            elif type == 2:
                new_polygns = Clipping.Weiler_atherton(new_points)
                if new_polygns:
                    for polygn in new_polygns:
                        CN.append([2, polygn])

            elif type == 3:
                new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([3, curve])

            elif type == 4:
                new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([4, curve])
                    
            elif type == 5:
                new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([5, curve])
                    
            elif type == 6:
                new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([6, curve])

        displayfile['CN'] = CN



        
        
        
