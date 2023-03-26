from tkinter import *


class Viewport(Canvas):
    """
    ...
        Uma classe para criar um canvas Viewport.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o canvas será alocado.

    Atributos
    ---------
        _displayfile: List
            lista de objetos desenhados na viewport.

        

    Métodos
    -------
        move_up() -> None:
            move os objetos para cima.

        move_left() -> None:
            move os objetos para esquerda.

        move_right() -> None:
            move os objetos para direta.

        move_down() -> None:
            move os objetos para baixo.

        zoomIn() -> None:
            Aumenta o tamanho dos objetos.

        zoomOut() -> None
            Diminui o tamanho dos objetos.

        drawn_point(tuple: point, str: color) -> None
            Desenha um ponto na viewport.

        drawn_line(list: points, str: color) -> None
            Desenha uma linha na viewport.

        drawn_wireframe(list: points,str: color,boolean: closed) -> None
            Desenha um wireframe na viewport.

    """
    
    def __init__(self, mainframe):
        Canvas.__init__(self,mainframe, 
                        width=710, 
                        height=480,
                        borderwidth=2, 
                        relief=SUNKEN)

        #Lista de objetos desenhados
        self.displayfile = []

    def move_up(self):
        #move os objetos para cima
        for object in self.displayfile:
            self.move(object, 0, -10)
        self.update()

    def move_left(self):
        #move os objetos para esquerda
        for object in self.displayfile:
            self.move(object, -10, 0)
        self.update()

    def move_right(self):
        #move os objetos para direita
        for object in self.displayfile:
            self.move(object, 10, 0)
        self.update()

    def move_down(self):
        #move os objetos para baixo
        for object in self.displayfile:
            self.move(object, 0, 10)
        self.update()
        
    def zoomIn(self):
        #Configura novo tamanho dos objetos
        self.scale('all', 360, 240, 2, 2)
        
    def zoomOut(self):
        #Configura novo tamanho dos objetos
        self.scale('all', 360, 240, 0.5, 0.5)

    def drawn_point(self, point, color):
        #Desenha o ponto e adiciona no displayfile.
        x, y = (point[0].get(),point[1].get())
        self.displayfile.append(self.create_oval(x,y,x,y,fill=color, width=1))

    def drawn_line(self, points, color):
        #Desenha a linha e adiciona no displayfile.
        x1, y1 = (points[0][0].get(),points[0][1].get())
        x2, y2 = (points[1][0].get(),points[1][1].get())
        self.displayfile.append(self.create_line(x1,y1,x2,y2,fill=color))

    def drawn_wireframe(self, points, color, closed):

        wireframe_lines = []

        #Desenha o wireframe e adiciona no displayfile.
        for i in range(len(points)-1):
            x1, y1 = (points[i][0].get(),points[i][1].get())
            x2, y2 = (points[i+1][0].get(),points[i+1][1].get())
            wireframe_lines.append(self.create_line(x1,y1,x2,y2,fill=color))
        
        if closed:
            x1, y1 = (points[len(points)-1][0].get(),points[len(points)-1][1].get())
            x2, y2 = (points[0][0].get(),points[0][1].get())
            wireframe_lines.append(self.create_line(x1,y1,x2,y2,fill=color))
            
        self.displayfile.append(wireframe_lines)
