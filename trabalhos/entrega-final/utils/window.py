from utils.transform import Transform
import math
class Window():
      """
        ...
                Uma classe que representa uma window no mundo.
        ...
        
        Args
        ---------
            _x_win_min: Float
                  x do menor ponto da window.

            _y_win_min: Float
                  y do menor ponto da window.
                  
            _x_win_max: Float
                  x do maior ponto da window.

            _y_win_max: Float
                  y do maior ponto da window.

        Atributos
        ---------
            _x_win_min: Float
                  x do menor ponto da window.

            _y_win_min: Float
                  y do menor ponto da window.
                  
            _x_win_max: Float
                  x do maior ponto da window.

            _y_win_max: Float
                  y do maior ponto da window.
            
            _x_center: Float
                  x do ponto central da windo.

            _y_center: Float  
                  y do ponto central da windo.

            _points: List
                  lista de pontos da window no mundo.

            _self.angle: Float
                  angulo que a window está rotacionada em relação ao mundo.
        Métodos
        -------
            getXmin() -> Float:
                  Retorna o x do menor ponto da window.

            getXmax() -> Float:
                  Retorna o x do maior ponto da window.

            getYmin() -> FLoat
                  Retorna o y do menor ponto da window.

            getYmax() -> Float
                  Retorna o y do maior ponto da window.

            getAngle() -> float
                  Retorna o angulo que a window está em relação ao mundo.

            getCenter() -> Tuple
                  Retorna ponto central da window.

            zomIn() -> None
                  Dobra o tamanho da window.

            zomOut() -> None
                  Divide o tamanho da window.

            moveUp() -> None
                  Move a window para cima.

            moveLeft() -> None
                  Move a window para esquerda.

            moveRight() -> None
                  Move a window para direita.

            moveDown() -> None
                  Move a window para baixo.
            
            rotation_left() -> None
                  Roda a window 30º

            rotation_right() -> None
                  Roda a window -30º

      """

      def __init__(self, x_win_min, y_win_min, z_win_min, x_win_max, y_win_max, z_win_max):
            #Pontos maximo e minimo.
            self.x_win_min =  x_win_min
            self.y_win_min = y_win_min
            self.z_win_min = z_win_min
            self.x_win_max = x_win_max
            self.y_win_max = y_win_max
            self.z_win_max = z_win_max
            


            #Pontos da window no mundo.
            self.points = [[x_win_min,y_win_min, self.z_win_min], [x_win_min,y_win_max, self.z_win_min], [x_win_max,y_win_max,self.z_win_max], [x_win_max,y_win_min,self.z_win_max]]
            
            #Centro da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)
            
            #Angulo que a window esta rotacionada em relação ao mundo.
            self.angle = 0

            
            self.VRP = [self.x_center, self.y_center, self.z_center]
            
      def getXmin(self):
            return self.x_win_min
    
      def getXmax(self):
            return self.x_win_max
    
      def getYmin(self):
            return self.y_win_min
    
      def getYmax(self):
            return self.y_win_max
      
      def getAngle(self):
            return self.angle
      
      def getVRP(self):
            return self.VRP
      
      def getPoints(self):
            return self.points
       
      def zomIn(self):          
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation3D(-1*self.x_center,-1*self.y_center, -1*self.z_center)


            #Gera matriz de escalonamento.
            matrix_scaling = Transform.scale3D(2, 2, 2)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation3D(self.x_center,self.y_center, self.z_center)
            
            #Gera matriz final.
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_scaling)] 
                                            for A_row in matrix_transition_origin] 


            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matrix] 

            

            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto


            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 

            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points
            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)
                                  
      def zomOut(self):
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation3D(-1*self.x_center,-1*self.y_center, -1*self.z_center)

            #Gera matriz de escalonamento.
            matrix_scaling = Transform.scale3D(0.5, 0.5, 0.5)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation3D(self.x_center,self.y_center,self.z_center)

            #Gera matriz final.
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_scaling)] 
                                            for A_row in matrix_transition_origin] 


            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matrix] 

            
            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points
            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)
            
      def moveUp(self,d):
            #Gera matriz de translação.
            matrix = Transform.translation3D(0, d, 0)
            
            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points
      
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)
            
            
            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)
            
            self.VRP = [self.x_center, self.y_center, self.z_center]

      def moveLeft(self, d):
            #Gera matriz de translação.
            matrix = Transform.translation3D(-1*d, 0, 0)


            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points

            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)
                        
            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)

            self.VRP = [self.x_center, self.y_center, self.z_center]
 
      def moveRight(self,d):
            #Gera matriz de translação.
            matrix = Transform.translation3D(d, 0, 0)


            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points
            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)

            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)
    
            self.VRP = [self.x_center, self.y_center, self.z_center]
            
      def moveDown(self,d):
            #Gera matriz de translação.
            matrix = Transform.translation3D(0, -1*d, 0)


            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points
            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)            
            
            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)
            
            self.VRP = [self.x_center, self.y_center, self.z_center]

      def rotationZ(self, angle): 
            a = [self.VRP[0] - self.points[1][0], 
                 self.VRP[1] - self.points[1][1], 
                 self.VRP[2] - self.points[1][2]
                 ]
            
            b = [self.points[2][0] - self.VRP[0], 
                 self.points[2][1] - self.VRP[1], 
                 self.points[2][2] - self.VRP[2]
                 ]
            
            #Determina VPN
            cx = a[1]*b[2] - a[2]*b[1]
            cy = a[2]*b[0] - a[0]*b[2]
            cz = a[0]*b[1] - a[1]*b[0]
            
            #Determina angulos.
            anglex = math.degrees(math.atan(cy/cz))
            angley = math.degrees(math.atan(cx/cz))
            
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation3D(-1*self.x_center,-1*self.y_center, -1*self.z_center)

            #Gera matriz de rotação em torno do eixo X.
            matrix_rotation_x = Transform.rotation3D_X(anglex)
            
            #Gera matriz de rotação em torno do eixo Y.
            matrix_rotation_y = Transform.rotation3D_Y(angley)
            
            #Gera matriz de rotação em torno do eixo Z
            matrix_rotation_Z = Transform.rotation3D_Z(angle)
            
            #Gera matriz de rotação em torno do eixo Y.
            matrix_rotation_y_b = Transform.rotation3D_Y(-1*angley)
            
            #Gera matriz de rotação em torno do eixo X.
            matrix_rotation_x_b = Transform.rotation3D_X(-1*anglex)
            
            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation3D(self.x_center,self.y_center, self.z_center)
            

            #Gera matriz final
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_x)] 
                                            for A_row in matrix_transition_origin] 

            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_y)] 
                                            for A_row in matrix] 
            
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_Z)] 
                                            for A_row in matrix] 
            
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_y_b)] 
                                            for A_row in matrix] 
            
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_x_b)] 
                                            for A_row in matrix]   

            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_transition_initial)] 
                                            for A_row in matrix]             
            
            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points      

            
            self.angle =  (self.angle + angle)%360
            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)


            #Centro da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)
            
            self.VRP = [self.x_center, self.y_center, self.z_center]
            
      def rotationY(self, angle):             
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation3D(-1*self.x_center,-1*self.y_center, -1*self.z_center)

            #Gera matriz de rotação em torno do eixo X.
            matrix_rotation_x = Transform.rotation3D_X(-1*self.anglex)
            
            #Gera matriz de rotação em torno do eixo Y.
            matrix_rotation_z = Transform.rotation3D_Z(-1*self.angle)
            
            #Gera matriz de rotação em torno do eixo Z
            matrix_rotation_y = Transform.rotation3D_Y(angle)
            
            #Gera matriz de rotação em torno do eixo Y.
            matrix_rotation_z_b = Transform.rotation3D_Z(self.angle)
            
            #Gera matriz de rotação em torno do eixo X.
            matrix_rotation_x_b = Transform.rotation3D_X(self.anglex)
            
            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation3D(self.x_center,self.y_center, self.z_center)
            

            #Gera matriz final
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_x)] 
                                            for A_row in matrix_transition_origin] 

            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_z)] 
                                            for A_row in matrix] 
            
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_y)] 
                                            for A_row in matrix] 
            
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_z_b)] 
                                            for A_row in matrix] 
            
            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation_x_b)] 
                                            for A_row in matrix]   

            matrix = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_transition_initial)] 
                                            for A_row in matrix]             
            
            #points x matrix
            points = [point+[1] for point in self.points] #Adiciona 1 como um 4 elemento de cada ponto
            points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix)] 
                            for A_row in points] 
            
            
            self.points = [point[:-1] for point in points] #Remove o 1 de cada ponto e adiciona em self.points      
                        
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)
            self.z_win_min = min(point[2] for point in self.points)
            self.z_win_max = max(point[2] for point in self.points)


            #Centro da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
            self.z_center = sum(point[2]/len(self.points) for point in self.points)
            
            self.VRP = [self.x_center, self.y_center, self.z_center]