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

        create_object(str: object, list: points, Combobox: color) -> 
            Desenha um objeto na window conforme o seu tipo 'object(point, line, wireframe)'.
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

    def create_object(self, object, points, color):

        if object == 'point':
            #Desenha o ponto e adiciona no displayfile.
            x, y = (points[0][0].get(),points[0][1].get())
            self.displayfile.append(self.create_oval(x,y,x,y,fill=color.get(), width=1))
        elif object == 'line':
            #Desenha a linha e adiciona no displayfile.
            x1, y1 = (points[0][0].get(),points[0][1].get())
            x2, y2 = (points[1][0].get(),points[1][1].get())
            self.displayfile.append(self.create_line(x1,y1,x2,y2,fill=color.get()))

        elif object == 'wireframe':
            #Desenha o wireframe e adiciona no displayfile.
            x1, y1 = (points[0][0].get(),points[0][1].get())
            x2, y2 = (points[1][0].get(),points[1][1].get())
            x3, y3 = (points[2][0].get(),points[2][1].get())
            x4, y4 = (points[3][0].get(),points[3][1].get())
            self.displayfile.append(self.create_line(x1,y1,x2,y2,fill=color.get()))
            self.displayfile.append(self.create_line(x1,y1,x3,y3,fill=color.get()))
            self.displayfile.append(self.create_line(x2,y2,x4,y4,fill=color.get()))
            self.displayfile.append(self.create_line(x3,y3,x4,y4,fill=color.get()))
