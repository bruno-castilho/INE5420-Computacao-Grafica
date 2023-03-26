from tkinter import *
from utils.transform import Transform

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

        transformObject(objectName, transformType, dx=0, dy=0, sx=0, sy=0, angle=0, x=0, y=0) -> None
            Faz transfomação escolhida em um objeto.

    """
    
    def __init__(self, mainframe):
        self.workspace = mainframe
        Canvas.__init__(self,mainframe, 
                        width=710, 
                        height=480)

        #Lista de objetos desenhados
        self.displayfile = {}

    def move_up(self):
        #move os objetos para cima
        for name in self.displayfile:
            self.move(self.displayfile[name], 0, -10)
        self.update()

    def move_left(self):
        #move os objetos para esquerda
        for name in self.displayfile:
            self.move(self.displayfile[name], -10, 0)
        self.update()

    def move_right(self):
        #move os objetos para direita
        for name in self.displayfile:
            self.move(self.displayfile[name], 10, 0)
        self.update()

    def move_down(self):
        #move os objetos para baixo
        for name in self.displayfile:
            self.move(self.displayfile[name], 0, 10)
        self.update()
        
    def zoomIn(self):
        #Configura novo tamanho dos objetos
        self.scale('all', 360, 240, 2, 2)
        
    def zoomOut(self):
        #Configura novo tamanho dos objetos
        self.scale('all', 360, 240, 0.5, 0.5)

    def drawn_point(self,name, point, color):
        #Desenha o ponto e adiciona no displayfile.
        x, y = (point[0].get(),point[1].get())
        self.displayfile[name] = [self.create_oval(x,y,x,y,fill=color, width=1)]

        #Busca objeto CurrentObjects
        interface = self.workspace.getInterface()
        menu = interface.getMenu()
        objects = menu.getObjects()
        currentObjects = objects.getCurrentObjects()
        
        #Atualiza boxList com os objetos existentes.
        currentObjects.updateObjects(self.displayfile)

    def drawn_line(self,name, points, color):
        #Desenha a linha e adiciona no displayfile.
        x1, y1 = (points[0][0].get(),points[0][1].get())
        x2, y2 = (points[1][0].get(),points[1][1].get())
        self.displayfile[name] = [self.create_line(x1,y1,x2,y2,fill=color)]

        #Busca objeto CurrentObjects
        interface = self.workspace.getInterface()
        menu = interface.getMenu()
        objects = menu.getObjects()
        currentObjects = objects.getCurrentObjects()
        
        #Atualiza boxList com os objetos existentes.
        currentObjects.updateObjects(self.displayfile)

    def drawn_wireframe(self,name, points, color, closed):

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
            
        self.displayfile[name] = wireframe_lines

        #Busca objeto CurrentObjects
        interface = self.workspace.getInterface()
        menu = interface.getMenu()
        objects = menu.getObjects()
        currentObjects = objects.getCurrentObjects()
        
        #Atualiza boxList com os objetos existentes.
        currentObjects.updateObjects(self.displayfile)

    def getDisplayfile(self):
        return self.displayfile

    def transformObject(self, objectName, transformType, dx=0, dy=0, sx=0, sy=0, angle=0, x=0, y=0):
        #Busca objeto no displayfile
        object = self.displayfile[objectName]

        #Constroi matriz dos pontos
        matrix_points = []
        for o in object:
             points = self.coords(o)
             matrix_points.append([points[0],points[1], 1])
             matrix_points.append([points[2],points[3], 1])
        
        #Calcula novos pontos
        if transformType == 'translation':
            matrix_points = Transform.translation(matrix_points, dx, dy)
        
        elif transformType == 'scale':
            matrix_points = Transform.scale(matrix_points, sx, sy)

        elif transformType == 'rotation_object_center':
            cx = sum(point[0] for point in matrix_points)/len(matrix_points)
            cy = sum(point[1] for point in matrix_points)/len(matrix_points) 

            matrix_points = Transform.rotation(matrix_points, angle, cx, cy)

        elif transformType == 'rotation_world_center':
            matrix_points = Transform.rotation(matrix_points, angle, 0, 0)
        
        elif transformType == 'rotation_arbitrary_point':
            matrix_points = Transform.rotation(matrix_points, angle, x, y)

        #Altera pontos do objeto.
        for i in range(0,len(matrix_points)-1, 2):
            self.coords(object[int(i/2)], matrix_points[i][0], matrix_points[i][1], matrix_points[i+1][0], matrix_points[i+1][1])


