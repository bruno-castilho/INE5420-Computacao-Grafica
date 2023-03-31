from tkinter import *
from globals import *

class Viewport(Canvas):
    """
    ...
        Uma classe para criar um canvas Viewport.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde a viewport será alocada.

    Atributos
    ---------
        _x_vp_min: Float
            x do menor ponto da viewport.

        _y_vp_min: Float
            y do menor ponto da viewport.

        _x_vp_max: Float
            x do maior ponto da viewport.

        _y_vp_max: Float
            y do maior ponto da viewport.

    Métodos
    -------
        draw() -> None
            Desenha os ojetos no canvas.

        transform() -> Tuple
            Calcula transformada de viewport.
    """
    
    def __init__(self, mainframe):
        Canvas.__init__(self,mainframe, 
                        width=710, 
                        height=480)
        
        #Pontos da viewport
        self.x_vp_min = 0
        self.y_vp_min = 0
        self.x_vp_max = 710
        self.y_vp_max = 480

    def draw(self):
        #Apaga os objetos atuais.
        self.delete("all")

        #Desenha novos objetos.
        for key in displayfile.keys():
            object = displayfile[key]
            points = object.getPoints()
            color = object.getColor()
            type = object.getType()

            #Ponto
            if type == 0:
                x, y = self.transform(points[0])

                self.create_oval(x,y,x,y,fill=color, width=1)
            
            #Linha
            elif type == 1:
                x1,y1 = self.transform(points[0])
                x2,y2 = self.transform(points[1])
                
                self.create_line(x1,y1,x2,y2,fill=color)

            #Wireframe
            elif type == 2:
                for i in range(len(points)-1):
                    x1,y1 = self.transform(points[i])
                    x2,y2 = self.transform(points[i+1])
    
                    self.create_line(x1,y1,x2,y2,fill=color)

                if object.isClosed():
                    x1,y1 = self.transform(points[len(points)-1])
                    x2,y2 = self.transform(points[0])

                    self.create_line(x1,y1,x2,y2,fill=color)
                
    def transform(self, point):
        x_w = point[0]
        y_w = point[1]
        x_w_min = window.getXmin()
        y_w_min = window.getYmin()
        x_w_max = window.getXmax()
        y_w_max = window.getYmax()

        #Calcula transformada de viewport.
        x_vp = (x_w - x_w_min)*(self.x_vp_max - self.x_vp_min)/(x_w_max - x_w_min) 
        y_vp = (1 - (y_w - y_w_min)/(y_w_max - y_w_min))*(self.y_vp_max - self.y_vp_min)

        return (x_vp, y_vp)