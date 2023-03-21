from tkinter import *

class Window(Canvas):
    """
    ...
        Uma classe para criar um canvas Window.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o canvas será alocado.

    Atributos
    ---------
        _displayfile: List
            lista de objetos desenhados na window.

    Métodos
    -------
        zoomIn() -> None:
            Aumenta o tamanho da window.

        zoomOut() -> None
            Diminui o tamanho da window.

        drawn_point(tuple: point, str: color) -> None
            Desenha um ponto na window.

        drawn_line(list: points, str: color) -> None
            Desenha uma linha na window.

        drawn_wireframe(list: points,str: color,boolean: closed) -> None
            Desenha um wireframe na window.

    """

    def __init__(self, mainframe):
        self.mainframe = mainframe
        Canvas.__init__(self, mainframe, bg='white', width=700, height=480)

        #Lista de objetos desenhados
        self.displayfile = []

    def zoomIn(self):
        #Configura novo tomanho da window.
        width = self.winfo_width()*2
        height = self.winfo_height()*2
        self.configure(width=width, height=height)

        #Configura novo tamanho dos objetos
        self.scale('all', 0, 0, 2, 2)
        self.mainframe.configure(scrollregion=self.mainframe.bbox("all"))
        
    def zoomOut(self):
        #Configura novo tomanho da window.
        width = self.winfo_width()*0.5
        height = self.winfo_height()*0.5
        self.configure(width=width, height=height)

        #Configura novo tamanho dos objetos
        self.scale('all', 0, 0, 0.5, 0.5)
        self.mainframe.configure(scrollregion=self.mainframe.bbox("all"))

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
