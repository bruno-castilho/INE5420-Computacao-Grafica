from tkinter import *
from globals import *
from utils.normalization import Normalization
from utils.projection import Projection

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
        creatBoard() -> None:
            Desenha a borda da viewport.
            
        draw() -> None:
            Desenha os ojetos no canvas.

        transform() -> Tuple:
            Calcula transformada de viewport.
    """
    
    def __init__(self, mainframe):
        Canvas.__init__(self,mainframe, 
                        width=710, 
                        height=480)
        
        #Pontos da viewport
        self.x_vp_min = 10
        self.y_vp_min = 10
        self.x_vp_max = 700
        self.y_vp_max = 470

        self.creatBoard()

    def creatBoard(self):
        self.create_line(self.x_vp_min,self.y_vp_min,self.x_vp_min,self.y_vp_max,fill="RED")
        self.create_line(self.x_vp_min,self.y_vp_max,self.x_vp_max,self.y_vp_max,fill="RED")
        self.create_line(self.x_vp_max,self.y_vp_max,self.x_vp_max,self.y_vp_min,fill="RED")
        self.create_line(self.x_vp_max,self.y_vp_min,self.x_vp_min,self.y_vp_min,fill="RED")
        
    def draw(self):
        #Projeta objetos.
        objects, window_points = Projection.project()
        #Normaliza objetos.
        Normalization.normalize(objects, window_points)
        
        #Apaga os objetos atuais.
        self.delete("all")

        #Desenha borda.
        self.creatBoard()

        #Desenha novos objetos.
        for object in displayfile['CN']:
            type = object[0]
            points = object[1]


            #Ponto
            if type == 0:
                x, y = self.transform(points[0])
                self.create_oval(x,y,x,y, width=1)
            
            #Linha
            elif type == 1:
                x1,y1 = self.transform(points[0])
                x2,y2 = self.transform(points[1])
                
                self.create_line(x1,y1,x2,y2)

            #Wireframe
            elif type == 2:
                for i in range(len(points)-1):
                    x1,y1 = self.transform(points[i])
                    x2,y2 = self.transform(points[i+1])

                    self.create_line(x1,y1,x2,y2)

            #Curvas e superficies
            elif type == 3 or type == 4 or type == 5 or type == 6:
                for i in range(len(points)-1):
                    
                    x1,y1 = self.transform(points[i])
                    x2,y2 = self.transform(points[i+1])

                    self.create_line(x1,y1,x2,y2)


                
    def transform(self, point):
        x_w = point[0]
        y_w = point[1]
        x_w_min = -1
        y_w_min = -1
        x_w_max = 1
        y_w_max = 1

        #Calcula transformada de viewport.
        x_vp = (x_w - x_w_min)*(self.x_vp_max - self.x_vp_min)/(x_w_max - x_w_min) + 10
        y_vp = (1 - (y_w - y_w_min)/(y_w_max - y_w_min))*(self.y_vp_max - self.y_vp_min) + 10

        return (x_vp, y_vp)