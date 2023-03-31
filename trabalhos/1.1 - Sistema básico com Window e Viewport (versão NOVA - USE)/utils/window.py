

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
                  
      """

      def __init__(self, x_win_min, y_win_min, x_win_max, y_win_max):
            self.x_win_min =  x_win_min
            self.y_win_min = y_win_min
            self.x_win_max = x_win_max
            self.y_win_max = y_win_max

            self.x_center = (self.x_win_max - self.x_win_min)/2
            self.y_center = (self.y_win_max - self.y_win_min)/2

      def getXmin(self):
          return self.x_win_min
    
      def getXmax(self):
          return self.x_win_max
    
      def getYmin(self):
          return self.y_win_min
    
      def getYmax(self):
          return self.y_win_max
    
      def zomIn(self):
          dx = self.x_win_max - self.x_win_min
          dy = self.y_win_max - self.y_win_min

          self.x_win_min = self.x_center - dx
          self.x_win_max = self.x_center + dx
          self.y_win_min = self.y_center - dy 
          self.y_win_max = self.y_center + dy

      def zomOut(self):
          dx = self.x_win_max - self.x_win_min
          dy = self.y_win_max - self.y_win_min

          self.x_win_min = self.x_center - dx/4
          self.x_win_max = self.x_center + dx/4
          self.y_win_min = self.y_center - dy/4
          self.y_win_max = self.y_center + dy/4
 
      def moveUp(self):
        self.y_center += 50

        self.y_win_max += 50
        self.y_win_min += 50

      def moveLeft(self):
        self.x_center -= 50
        self.x_win_max -= 50
        self.x_win_min -= 50
    
      def moveRight(self):
        self.x_center += 50
        self.x_win_max += 50
        self.x_win_min += 50
    
      def moveDown(self):
        self.y_center -= 50

        self.y_win_max -= 50
        self.y_win_min -= 50