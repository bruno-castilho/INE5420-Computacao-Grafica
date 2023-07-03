from tkinter import * 
from tkinter import ttk
from utils.object import Object
from globals import *

class windowCreationObject(Toplevel):
    """
    ...
        Uma classe para criar um Toplevel Objects.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto Menu.

    Atributos
    ---------
        _currentObjects: Frame:
            Objeto currentObjects.

        _labelCor: Label
            Objeto Label para apresentar o texto 'Cor:'.

        _color: Combobox
            Objeto Combobox para escolha de cor ('black','red', 'yellow', 'blue', 'green', 'gray', 'orange').

        _scrollbar: Scrollbar
            Objeto Srollbar utilizado para rolagem das entries.

        _canvas_entries: Canvas
            Objeto Canvas que contem o Frame entries, necessario para rolagem.

        _entrys: Frame
            Objeto Frame para ser posicionados as entradas dos pontos. 


    Métodos
    -------
        new_entry_point(list: points_list) -> None:
            Função que gera entries para recebimento de pontos e insere no frame entries.

        createPoint(Viewport: viewport) -> None:
            Monta a janela para criar um ponto.

        createLine(Viewport: viewport) -> None:
            Monta a janela para criar uma linha.

        createWireframe(Viewport: viewport) -> None:
            Monta a janela para criar um wireframe.
    """

    def __init__(self, menu):
        #Busca frame currentObjects na memoria.
        objects = menu.getObjects()
        self.currentObjects = objects.getCurrentObjects()

        Toplevel.__init__(self)
        self.geometry("450x220")
        self.config(bg="skyblue")
        
        #Cria label com texto 'Name:'.
        self.labelName = Label(self, text='Name:', bg="skyblue")
        self.labelName.pack(pady=(10,0))

        self.name = Entry(self, width=50)
        self.name.pack(pady=(0,5))
        
        #Cria label com texto 'Points:'.
        self.labelPoints = Label(self, text='Points:', bg="skyblue")
        self.labelPoints.pack(pady=(5,0))
        
        self.points = Text(self, width=50, height=5)
        self.points.pack()

    def createPoint(self, viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            points = eval(f'[{string}]')
            if len(points) == 1:
                name = self.name.get()            
                displayfile['CW'][name] = Object(name, 0, points)
                viewport.draw()
                self.currentObjects.updateObjects()
                
        
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))
    
    def createLine(self, viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            points = eval(f'[{string}]')
            
            if len(points) == 2:
                name = self.name.get()
                displayfile['CW'][name] = Object(name, 1, points)
                viewport.draw()
                self.currentObjects.updateObjects()
        
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))
    
    def createWireframe(self, viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            points = eval(f'[{string}]')
            
            if len(points) > 2:
                name = self.name.get()
                displayfile['CW'][name] = Object(name, 2, points)
                viewport.draw()
                self.currentObjects.updateObjects()
        
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))
    
    def createBezierCurve(self, viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            points = eval(f'[{string}]')
            
            if (len(points) >= 4) and ((len(points)-4) % 3 == 0):
                name = self.name.get()
                displayfile['CW'][name] = Object(name, 3, points)
                viewport.draw()
                self.currentObjects.updateObjects()
        
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))

    def createBSpline(self, viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            points = eval(f'[{string}]')
            
            if len(points) >= 4:
                name = self.name.get()
                displayfile['CW'][name] = Object(name, 4, points)
                viewport.draw()
                self.currentObjects.updateObjects()
        
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))

    def createBezierSurfaces(self, viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            lines = string.split(';')

            points = []
            for line in lines:
                line = eval(f'[{line}]')
                if len(line) != 16: return
                points.append(line)

            name = self.name.get()
            displayfile['CW'][name] = Object(name, 5, points)
            viewport.draw()
            self.currentObjects.updateObjects()
                
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))
    
    def createSurfaceFwdDiff(self,viewport):
        def create():
            string = self.points.get(1.0, END)
            string = string.strip()
            lines = string.split(';')

            if len(lines) >= 4 and len(lines) <=20:
                points = []
                for line in lines:
                    line = eval(f'[{line}]')
                    if len(line) != len(lines): return
                    points.append(line)

                name = self.name.get()
                displayfile['CW'][name] = Object(name, 6, points)
                viewport.draw()
                self.currentObjects.updateObjects()
        
        btn = Button(self, text='OK', command=create)
        btn.pack(pady=(10,10))