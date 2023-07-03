from globals import *
from utils.transform import Transform
from utils.object import Object
from utils.clipping import Clipping
from utils.curves import Curves
from utils.surfaces import Surfaces
import math

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
    
    
    def perspectiveProjection():
        #Centro da window.
        vrp = window.getVRP()
        cop = [vrp[0],vrp[1], vrp[2] - 200]
        points = window.getPoints()
                
        a = [vrp[0] - points[1][0], 
             vrp[1] - points[1][1], 
             vrp[2] - points[1][2]
            ]
            
        b = [points[2][0] - vrp[0], 
             points[2][1] - vrp[1], 
             points[2][2] - vrp[2]
            ]
            
        #Determina VPN
        cx = a[1]*b[2] - a[2]*b[1]
        cy = a[2]*b[0] - a[0]*b[2]
        cz = a[0]*b[1] - a[1]*b[0]
            
        #Determina angulos.
        anglex = math.degrees(math.atan(cy/cz))
        angley = math.degrees(math.atan(cx/cz))
        
        #Gera matriz de translação para a origem.
        matrix_transition_origin = Transform.translation3D(-1*vrp[0],-1*vrp[1], -1*vrp[2])
        
        #Gera matriz de rotação em torno do eixo X.
        matrix_rotation_x = Transform.rotation3D_X(anglex)
        
        #Gera matriz de rotação em torno do eixo Y.
        matrix_rotation_y = Transform.rotation3D_Y(angley)
        
        #Gera matriz de translação para o ponto inicial.
        matrix_transition_initial = Transform.translation3D(-1*vrp[0],-1*vrp[1], -1*vrp[2])
        
        #Gera matriz de translação COP para origem.
        matrix_transition_COP = Transform.translation3D(-1*cop[0],-1*cop[1], -1*cop[2])
        
        #Gera matriz final
        matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrix_transition_origin)] 
                                    for A_row in matrix_transition_COP] 
        
        
        matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrix_rotation_x)] 
                                    for A_row in matrix] 
        
        matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrix_rotation_y)] 
                                    for A_row in matrix] 
        
        matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrix_transition_initial)] 
                                    for A_row in matrix] 
        

        
        return matrix
    
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
    
    def normalize():
        #Dicionario para adicionar objetos normalizados.
        CN = []

        #Matriz de projeção
        matrix_projection = Normalization.perspectiveProjection()
        
        #pontos da window no mundo.
        window_points = window.getPoints()
        window_points = [point+[1] for point in window_points] #Adiciona 1 como um 4 elemento de cada ponto
    
        window_points = [[sum(a * b for a, b in zip(A_row, B_col))  
                            for B_col in zip(*matrix_projection)] 
                                for A_row in window_points]
        
        window_points = [point[:-1] for point in window_points] #Remove o 1 de cada ponto e adiciona em self.points  
        
        #Matriz de normalização.
        matrixSWNtoSCN = Normalization.matrixSWNtoSCN(window_points)

        #Normaliza objetos.
        for object_name in displayfile['CW'].keys():
            object = displayfile['CW'][object_name]
            type  = object.getType()
            points = [[point[0],point[1],point[2],1] for point in object.getPoints()]
            color = object.getColor()

            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrix_projection)] 
                                    for A_row in points]
            
            points = [[point[0]/(point[2]/200),point[1]/(point[2]/200),point[3]] for point in points] #Faz projeção em pespectiva.

            
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                                for B_col in zip(*matrixSWNtoSCN)] 
                                    for A_row in points]
            
            new_points = [point[:-1] for point in points]

            if type == 0:
                new_points = Clipping.point(new_points)
                if new_points: 
                    CN.append([0,  color, new_points])

            elif type == 1:
                if Mode_clipping['value'] == 'Liang Barsky':
                    new_points = Clipping.Liang_Barsky(new_points)
                else: 
                    new_points = Clipping.Cohen_Sutherland(new_points)
                
                if new_points: 
                    CN.append([1, color, new_points])
        
            elif type == 2:
                new_polygns = Clipping.Weiler_atherton(new_points)
                if new_polygns:
                    for polygn in new_polygns:
                        CN.append([2, color, polygn])

            elif type == 3:
                new_points = Curves.bezier(new_points)
                new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([3, color, curve])

            elif type == 4:
                new_points = Curves.B_Spline(new_points)
                new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([4, color, curve])
                    
            elif type == 5:
                new_points = Surfaces.bezier(new_points)
                new_curves = Clipping.curves(new_points)
                #new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([5, color, curve])
            elif type == 6:

                new_points = Surfaces.surfaceFwdDiff(new_points)
                
                new_curves = Clipping.curves(new_points)
                #new_curves = Clipping.curves(new_points)
                for curve in new_curves:
                    CN.append([5, color, curve])
                
                

        displayfile['CN'] = CN



        
        
        
