import math
from utils.transform import Transform
from globals import *
from utils.curves import Curves
from utils.surfaces import Surfaces

class Projection():
    def matrixPerspective():
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
    
    def project():
        objects = []
        matrixPerspective = Projection.matrixPerspective()
        for object_name in displayfile['CW'].keys():
            object = displayfile['CW'][object_name]
            type  = object.getType()
            points = object.getPoints()
            
            if type == 3:
                points = Curves.bezier(points)
            if type == 4:
                points = Curves.B_Spline(points)
            if type == 5:
                points = Surfaces.bezier(points)
            if type == 6:
                points = Surfaces.surfaceFwdDiff(points)
            

            #Faz projeção em pespectiva.
            points = [[sum(a * b for a, b in zip([A_row[0],A_row[1],A_row[2],1], B_col))  
                            for B_col in zip(*matrixPerspective)] 
                                for A_row in points]
            
            points = [[point[0]/(point[2]/200),point[1]/(point[2]/200), point[2]] for point in points] 
            
            objects.append([type, points])
        
        #pontos da window no mundo.
        window_points = window.getPoints()

        w_points = [[sum(a * b for a, b in zip([A_row[0],A_row[1],A_row[2],1], B_col))  
                            for B_col in zip(*matrixPerspective)] 
                                for A_row in window_points]
        
        w_points = [point[:-1] for point in w_points]
        
        return objects, w_points
        