from utils.transform import Transform

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

      def __init__(self, x_win_min, y_win_min, x_win_max, y_win_max):
            #Pontos maximo e minimo.
            self.x_win_min =  x_win_min
            self.y_win_min = y_win_min
            self.x_win_max = x_win_max
            self.y_win_max = y_win_max
            
            #Centro da window.
            self.x_center = (self.x_win_max - self.x_win_min)/2
            self.y_center = (self.y_win_max - self.y_win_min)/2

            #Pontos da window no mundo.
            self.points = [[x_win_min,y_win_min, 1], [x_win_min,y_win_max, 1], [x_win_max,y_win_max,1], [x_win_max,y_win_min,1]]
            
            #Angulo que a window esta rotacionada em relação ao mundo.
            self.angle = 0
            
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
      
      def getCenter(self):
            return (self.x_center, self.y_center)
      
      def getPoints(self):
            return self.points
      
      def zomIn(self):          
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation(-1*self.x_center,-1*self.y_center)

            #Gera matriz de escalonamento.
            matrix_scaling = Transform.scale(2, 2)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation(self.x_center,self.y_center)



            #matrix_transition_origin x matrix_scaling
            matriz_origin_scaling = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_scaling)] 
                                            for A_row in matrix_transition_origin] 

            #matrix_transition_origin x matrix_scaling X matrix_transition_initial
            matriz_origin_scaling_initial = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matriz_origin_scaling] 

            #self.points x matriz_origin_scaling_initial
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matriz_origin_scaling_initial)] 
                            for A_row in self.points] 

            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)

      def zomOut(self):
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation(-1*self.x_center,-1*self.y_center)

            #Gera matriz de escalonamento.
            matrix_scaling = Transform.scale(0.5, 0.5)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation(self.x_center,self.y_center)



            #matrix_transition_origin x matrix_scaling
            matriz_origin_scaling = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_scaling)] 
                                            for A_row in matrix_transition_origin] 

            #matrix_transition_origin x matrix_scaling X matrix_transition_initial
            matriz_origin_scaling_initial = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matriz_origin_scaling] 

            #self.points x matriz_origin_scaling_initial
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matriz_origin_scaling_initial)] 
                            for A_row in self.points] 

            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)

      def moveUp(self):
            #Gera matriz de translação.
            matrix_transition = Transform.translation(0, 10)


            #self.points x matrix_transition
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition)] 
                                    for A_row in self.points] 
            

            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)

            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)


            print(self.points)

      def moveLeft(self):
            #Gera matriz de translação.
            matrix_transition = Transform.translation(-10, 0)


            #self.points x matrix_transition
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition)] 
                                for A_row in self.points] 
            
            
            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)


            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)

      def moveRight(self):
            #Gera matriz de translação.
            matrix_transition = Transform.translation(10, 0)


            #self.points x matrix_transition
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition)] 
                                for A_row in self.points] 
            

            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)

            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)
    
      def moveDown(self):
            #Gera matriz de translação.
            matrix_transition = Transform.translation(0, -10)


            #self.points x matrix_transition
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition)] 
                                for A_row in self.points] 
            

            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)


            #Econtra ponto central da window.
            self.x_center = sum(point[0]/len(self.points) for point in self.points)
            self.y_center = sum(point[1]/len(self.points) for point in self.points)

      def rotation(self, angle):
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation(-1*self.x_center,-1*self.y_center)

            #Gera matriz de rotação.
            matrix_rotation = Transform.rotation(angle)
            self.angle = (self.angle + angle) % 360

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation(self.x_center,self.y_center)
            

            #matrix_transition_origin x matrix_scaling
            matriz_origin_rotation = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation)] 
                                            for A_row in matrix_transition_origin] 

            #matrix_transition_origin x matrix_scaling X matrix_transition_initial
            matriz_origin_rotation_initial = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matriz_origin_rotation] 


            #self.points x matriz_origin_scaling_initial
            self.points = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matriz_origin_rotation_initial)] 
                            for A_row in self.points] 
            

            #Set novos valores min e max
            self.x_win_min = min(point[0] for point in self.points)
            self.x_win_max = max(point[0] for point in self.points)
            self.y_win_min = min(point[1] for point in self.points)
            self.y_win_max = max(point[1] for point in self.points)


