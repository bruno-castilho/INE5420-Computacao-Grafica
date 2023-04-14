import numpy as np

class Clipping():
    
    def point(points):
        point = points[0]
        if (point[0] >= -1 and point[0] <= 1) and (point[1] >= -1 and point[1] <= 1):
            return points
        
    def Cohen_Sutherland(points):
        def codeOfPoint(point):
            codigo = 0

            #Ponto a direta.
            if point[0] > 1:
                codigo += 2

            #Ponto a esquerda.
            elif point[0] < -1:
                codigo += 1
            
            #Ponto a cima.
            if point[1] > 1:
                codigo += 8

            #Ponto a baixo.
            elif point[1] < -1:
                codigo += 4

            return codigo

        def setPoint(REcode, point, m):
            #Intersecção esquerda.
            if REcode & 1 == 1:
                y = m*(-1 - point[0]) + point[1]
                if y >= -1 and y <= 1: 
                    return [-1,y,1]
            
            #Intersecção direita.
            if REcode & 2 == 2:
                y = m*(1 - point[0]) + point[1]
                if y >= -1 and y <= 1: 
                    return [1,y,1]

            #Intersecção baixo.
            if REcode & 4 == 4:
                if m == 0 and m != None:
                    x = point[0] + (-1 - point[1])/m
                    if x >= -1 and x <= 1:
                        return [x,-1,1]
                    
                if m == None:
                    return [point[0],-1,1]
                    
            #Intersecção cima.
            if REcode & 8 == 8:
                if  m != 0 and m != None:
                    x = point[0] + (1 - point[1])/m
                    if x >= -1 and x <= 1:
                        return [x,1,1]
                if m == None:
                    return [point[0],1,1]

        
        #Codigo dos pontos.
        REcode1 = codeOfPoint(points[0])
        REcode2 = codeOfPoint(points[1])

        #And de um par de vertice.
        if REcode1 & REcode2 == 0:
            #Or de um par de vertice.
            if REcode1 | REcode2 == 0:
                return points
            else:
                #Calcula coeficiente angular.
                dx = points[1][0] - points[0][0]
                dy = points[1][1] - points[0][1]
                m = None
                if dx != 0: m = dy/dx
                
                new_points = [points[0], points[1]]
                #Descobre novo ponto1
                if REcode1 != 0: 
                    point1 = setPoint(REcode1, points[0], m)
                    if point1 == None: return
                    new_points[0] = point1
                    

                #Descobre novo ponto2
                if REcode2 != 0: 
                    point2 = setPoint(REcode2, points[1], m)
                    if point2 == None: return
                    new_points[1] = point2
                
                return new_points

    def Liang_Barsky(points):
        p1 = -1*(points[1][0] - points[0][0])
        p2 = points[1][0] - points[0][0]
        p3 = -1*(points[1][1] - points[0][1])
        p4 = points[1][1] - points[0][1]
        q1 = points[0][0] - (-1)
        q2 =  1 - points[0][0]
        q3 = points[0][1] - (-1)
        q4 = 1 - points[0][1]

        u1 = 0
        u2 = 1

        if (p1 == 0 and p2 == 0) and (q1 < 0 or q2 < 0): return
        if (p3 == 0 and p3 == 0) and (q3 < 0 or q4 < 0): return

        if p1 < 0:
            r1 = q1/p1
            r2 = q2/p2
            u1 = max(u1, r1)
            u2 = min(u2, r2)
        elif p2 < 0:
            r1 = q1/p1
            r2 = q2/p2
            u1 = max(u1, r2)
            u2 = min(u2, r1)
        
        if p3 < 0:
            r3 = q3/p3
            r4 = q4/p4
            u1 = max(u1, r3)
            u2 = min(u2, r4)

        elif p4 < 0:
            r3 = q3/p3
            r4 = q4/p4
            u1 = max(u1, r4)
            u2 = min(u2, r3)
        
        
        if u1 > u2:
            return
                
        new_points = [points[0], points[1]]

        if u1 != 0:
            x = points[0][0] + u1*p2
            y = points[0][1] + u1*p4
            new_points[0] = [x, y, 1]

        if u2 != 1:
            x = points[0][0] + u2*p2
            y = points[0][1] + u2*p4
            new_points[1] = [x, y, 1]

        return new_points
        
    def Weiler_atherton(points):

        def is_polygon_outside_window():
            for point in points:
                if Clipping.point([point]) != None:
                    return False
                
            return True
        

        def is_polygon_inside_window():
            for point in points:
                if Clipping.point([point]) == None:
                    return False
                
            return True
        


        if is_polygon_outside_window():
            return None
        
        if is_polygon_inside_window():
            return [points]
        
        
        points_window = [([-1,-1,1], -1), ([-1,1,1], -1),([1,1,1], -1), ([1,-1,1], -1)]
        polygon_clipped_points = []
        entrantes = []

        def set_point_window(point):
            for i in range(len(points_window)):
                point1 = points_window[i][0]
                point2 = points_window[0][0]
                if i != (len(points_window) -1): point2 = points_window[i+1][0]

                if point[0][0] == point1[0]:
                    if point1[0] == -1 and point2[0] == -1 and point[0][1] < point2[1]:
                        points_window.insert(i+1, point)
                        break
                    elif point1[0] == 1 and point2[0] == 1 and point[0][1] > point2[1]:
                        points_window.insert(i+1, point)
                        break

                if point[0][1] == point1[1]:
                    if point1[1] == -1 and point2[1] == -1 and point[0][0] > point2[0]:
                        points_window.insert(i+1, point)
                        break

                    elif point1[1] == 1 and point2[1] == 1 and point[0][0] < point2[0]:
                        points_window.insert(i+1, point)
                        break
        

        for i in range(len(points)-1):
            point1 = points[i]
            point2 = points[i+1]

            new_points = Clipping.Liang_Barsky([point1, point2])
            polygon_clipped_points.append((point1, -1))

            if new_points != None: 
                #Ponto de entrada
                if new_points[0] != point1:
                    polygon_clipped_points.append((new_points[0], 0))
                    entrantes.append((new_points[0], 0))
                    set_point_window((new_points[0], 0))

                #Ponto de saida
                if new_points[1] != point2:
                    polygon_clipped_points.append((new_points[1], 1))
                    set_point_window((new_points[1], 1))
            

        polygons = []
        pontos_marcados_polygon_clipped_points = [False]*len(polygon_clipped_points)
        pontos_marcados_polygon_points_window = [False]*len(points_window)
        while len(entrantes) != 0:
            #Pega um ponto entrante.
            point = entrantes.pop(0)
            p_i = polygon_clipped_points.index(point) 
            
            #Se ponto entrante não estiver marcado
            if not pontos_marcados_polygon_clipped_points[p_i ]:
                #Marca ponto entrante na lista de pontos vistos do poligno.
                pontos_marcados_polygon_clipped_points[p_i ] = True
                
                #Marca ponto entrante na lista de pontos vistos da window.
                w_i = points_window.index(point)
                pontos_marcados_polygon_points_window[w_i] = True
                
                #Cria uma lista para receber pontos de um novo poligno.
                new_polygn = []
                #Adiciona ponto, como primeiro ponto do poligno.
                new_polygn.append(point[0])


                closed =  False
                #Enquanto não fechar um poligno
                while not closed:
                    #Vai para o proximo ponto da lista do poligno.
                    p_i = (p_i + 1)%len(polygon_clipped_points)
                    current__point = polygon_clipped_points[p_i]

                    #Se ponto já marcado anteriormente
                    if pontos_marcados_polygon_clipped_points[p_i]:
                        #Fecha poligno.
                        closed = True
                    #Se nã0
                    else:
                        #Marca ponto na lista de pontos vistos do poligno
                        pontos_marcados_polygon_clipped_points[p_i ] = True

                    #Adiciona ponto na lista do novo poligno.
                    new_polygn.append(current__point[0])

                    #Se o ponto for uma intersecção e poligno não estiver fechado
                    if (current__point [1] == 0 or current__point [1] == 1) and not closed:
                        #Busca index do ponto na lista de pontos da window.
                        w_i = points_window.index(current__point)
                        
                        #Marca ponto na lista de pontos vistos da window.
                        pontos_marcados_polygon_points_window[w_i] = True

                        while True:
                            #Busca proximo ponto da lista de pontos da window.
                            w_i = (w_i + 1)%len(points_window)
                            curren_window_point = points_window[w_i]
                            
                            #Adiciona ponto na lista do novo poligno.
                            new_polygn.append(curren_window_point [0])

                            #Se ponto já marcado anteriormente
                            if pontos_marcados_polygon_points_window[w_i]:
                                #Fecha poligno.
                                closed = True
                                break

                            #Marca ponto na lista de pontos vistos da window.
                            pontos_marcados_polygon_points_window[w_i] = True
                            
                            #Se o ponto for uma intersecção
                            if curren_window_point[1] == 0 or curren_window_point[1] == 1:
                                #Busca index do ponto na lista de pontos de poligno.
                                p_i  = polygon_clipped_points.index(curren_window_point)
                                #Marca ponto na lista de pontos vistos do poligno
                                pontos_marcados_polygon_clipped_points[p_i] = True
                                break
                           
                polygons.append(new_polygn)            
                        
                            

        return polygons

