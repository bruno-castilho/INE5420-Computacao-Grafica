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
        self.geometry("230x440")
        self.resizable(False, False)
        
        #Cria label com texto 'Cor:'.
        self.labelName = Label(self, text='Name:')
        self.labelName.grid(column=0, row=0, columnspan=2, pady=(10,0))

        self.name = Entry(self, width=20)
        self.name.grid(column=0, row=1, columnspan=2, pady=(5,5))

        #Cria o scrollbar vertical.
        self.scrollbar = Scrollbar(self,orient=VERTICAL)
        self.scrollbar.grid(column=1, row=2, sticky="ns")

        #Canvas para receber o frame entries, necessario para rolagem.
        self.canvas_entries = Canvas(self,yscrollcommand=self.scrollbar.set, width=190, height=190)
        self.canvas_entries.grid(column=0, row=2)

        #Cria Frame para posicionar as entrys.
        self.entries = Frame(self.canvas_entries, width=190)
        
        #Configura rolagem.
        self.scrollbar.config(command=self.canvas_entries.yview)
        self.canvas_entries.create_window(0,0, window=self.entries, anchor='n')
        self.canvas_entries.configure(scrollregion=self.canvas_entries.bbox("all"))

        #Cria label com texto 'Color:'.
        self.labelCor = Label(self, text='Color:')
        self.labelCor.grid(column=0, row=3, columnspan=2, pady=5)

        #Cria boxlist para escolha da cor do objeto a ser desenhado.
        self.color = ttk.Combobox(self, state= "readonly")
        self.color['values'] = ('black','red', 'yellow', 'blue', 'green', 'gray', 'orange')
        self.color.current(0)
        self.color.grid(column=0, row=4, columnspan=2, pady=(0,10), padx=20)

    def new_entry_point(self, points_list):
            n_points = len(points_list)
            point_n = n_points + 1

            #Cria label com texto 'Point-N:'.
            labelPoint_1 = Label(self.entries, text=f'Point-{point_n}:')
            labelPoint_1.grid(row=n_points*2, column=0, pady=5, columnspan=6)
            
            #Cria label com texto 'X:'.
            labelX = Label(self.entries, text='X:')
            labelX.grid(row=n_points*2 + 1, column=0, pady=5)
            #Cria entry para receber 'x'.
            x = Entry(self.entries, width=5)
            x.grid(row=n_points*2 + 1, column=1)

            #Cria label com texto 'Y:'.
            labelY = Label(self.entries, text='Y:')
            labelY.grid(row=n_points*2 + 1, column=2, pady=5)
            #Cria entry para receber 'y'.
            y = Entry(self.entries, width=5)
            y.grid(row=n_points*2 + 1, column=3)
            
            #Cria label com texto 'Y:'.
            labelY = Label(self.entries, text='Z:')
            labelY.grid(row=n_points*2 + 1, column=4, pady=5)
            #Cria entry para receber 'y'.
            z = Entry(self.entries, width=5)
            z.grid(row=n_points*2 + 1, column=5)

            #Adiciona entries como um ponto na lista de pontos
            points_list.append([x,y,z])
            
            #Redimensiona região de rolagem.
            scrollregion = self.canvas_entries.config('scrollregion')[4]
            scrollregion = scrollregion.split()
            self.canvas_entries.configure(scrollregion=(int(scrollregion[0]),int(scrollregion[1]),int(scrollregion[2]), int(scrollregion[3])+65))

    def createPoint(self, viewport):
        entries_points = []
        #Cria e adiciona objeto no display file e redesenha a viewport.
        def create():
             name = self.name.get()
             color = self.color.get()
             
             points = [[float(entries_points[0][0].get()), float(entries_points[0][1].get()), float(entries_points[0][2].get())]]
             displayfile['CW'][name] = Object(name, 0, points, color)
             viewport.draw()

             self.currentObjects.updateObjects()

        self.new_entry_point(entries_points)

        #Cria o botão 'OK' para desenhar o ponto.
        btn = Button(self, text='OK', width=3, command=create)
        btn.grid(column=0, row=5, columnspan=2, pady=(10,10))

    def createLine(self, viewport):
        entries_points = []

        #Cria e adiciona objeto no display file e redesenha a viewport.
        def create():
             name = self.name.get()
             color = self.color.get()
             points = []
             for entry in entries_points:
                  points.append([float(entry[0].get()), float(entry[1].get()), float(entry[2].get())])

             displayfile['CW'][name] = Object(name, 1, points, color)
             viewport.draw()

             self.currentObjects.updateObjects()

        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)

        #Cria o botão 'OK' para desenhar a linha.
        btn = Button(self, text='OK', width=3, command=create)
        btn.grid(column=0, row=5, columnspan=2, pady=(10,10))
    
    def createWireframe(self, viewport):
        entries_points = []

        #Cria e adiciona objeto no display file e redesenha a viewport.
        def create():
            name = self.name.get()
            color = self.color.get()
            points = []
            for entry in entries_points:
                  points.append([float(entry[0].get()), float(entry[1].get()),float(entry[2].get())])

            points.append([float(entries_points[0][0].get()), float(entries_points[0][1].get()),float(entry[2].get())])
            displayfile['CW'][name] = Object(name, 2, points, color)
            viewport.draw()

            self.currentObjects.updateObjects()

        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)

        #Cria o botão 'MORE' para adicionar mais uma entrada de ponto.
        btn = Button(self, text='MORE', width=3, command=lambda: self.new_entry_point(entries_points))
        btn.grid(column=0, row=6, columnspan=2, pady=(5,5))

        #Cria o botão 'OK' para desenhar o wireframe.
        OK = Button(self, text='OK', width=3, command=create)
        OK.grid(column=0, row=7, columnspan=2,pady=(5,10))
    
    def createBezierCurve(self, viewport):
        entries_points = []

        #Cria e adiciona objeto no display file e redesenha a viewport.
        def create():
            name = self.name.get()
            color = self.color.get()
            points = []
            for entry in entries_points:
                  points.append([float(entry[0].get()), float(entry[1].get()),float(entry[2].get())])

            displayfile['CW'][name] = Object(name, 3, points, color)
            viewport.draw()

            self.currentObjects.updateObjects()

        #Adiciona novos pontos para continuidade da curva.
        def more():
            self.new_entry_point(entries_points)
            self.new_entry_point(entries_points)
            self.new_entry_point(entries_points)

             
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)


        #Cria o botão 'MORE' para adicionar mais uma entrada de ponto.
        btn = Button(self, text='MORE', width=3, command=more)
        btn.grid(column=0, row=6, columnspan=2, pady=(5,5))

        #Cria o botão 'OK' para desenhar o wireframe.
        OK = Button(self, text='OK', width=3, command=create)
        OK.grid(column=0, row=7, columnspan=2,pady=(5,10))

    def createBSpline(self, viewport):
        entries_points = []

        #Cria e adiciona objeto no display file e redesenha a viewport.
        def create():
            name = self.name.get()
            color = self.color.get()
            points = []
            for entry in entries_points:
                  points.append([float(entry[0].get()), float(entry[1].get()),float(entry[2].get())])

            displayfile['CW'][name] = Object(name, 4, points, color)
            viewport.draw()

            self.currentObjects.updateObjects()
             
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)


        #Cria o botão 'MORE' para adicionar mais uma entrada de ponto.
        btn = Button(self, text='MORE', width=3, command=lambda: self.new_entry_point(entries_points))
        btn.grid(column=0, row=6, columnspan=2, pady=(5,5))

        #Cria o botão 'OK' para desenhar o wireframe.
        OK = Button(self, text='OK', width=3, command=create)
        OK.grid(column=0, row=7, columnspan=2,pady=(5,10))
               
    def createBezierSurfaces(self, viewport):
        entries_points = []

        #Cria e adiciona objeto no display file e redesenha a viewport.
        def create():
            name = self.name.get()
            color = self.color.get()
            points = []
            for entry in entries_points:
                  points.append([float(entry[0].get()), float(entry[1].get()),float(entry[2].get())])

            displayfile['CW'][name] = Object(name, 5, points, color)
            viewport.draw()

            self.currentObjects.updateObjects()
             
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)
        self.new_entry_point(entries_points)


        #Cria o botão 'OK' para desenhar o wireframe.
        OK = Button(self, text='OK', width=3, command=create)
        OK.grid(column=0, row=6, columnspan=2,pady=(5,10))
        