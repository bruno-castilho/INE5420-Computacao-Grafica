from tkinter import *
from tkinter import ttk
from interface.interface_components.menu_components.objects_components.windowcreationobject import windowCreationObject

class NewObject(Frame):
    """
    ...
        Uma classe para criar um frame Objects.
    ...
    
    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    Atributos
    ---------
        _text: Label
            Objeto Label para apresentar o texto 'Objects'.

        _objects: Combobox
            Objeto Combobox para escolha de um objeto ('point','line', 'wireframe').

        _btn: Button
            Objeto Button para abrir a janela de criação do objeto escolhido.

    Métodos
    -------
        create() -> None:
            Abre uma jenala de criação de objeto, conforme o tipo.
    """
    def __init__(self, mainframe):
        self.mainframe = mainframe

        #Set frame objects.
        Frame.__init__(self, 
                       mainframe, 
                       background="#9b9b9b",
                       width=180, 
                       height=90)
        
        self.pack_propagate(0)

        #Cria label com texto 'Objects'.
        self.text = Label(self, text='New Object', background="#9b9b9b")
        self.text.pack(pady=(0,5))
        
        #Cria boxlist para escolha do objeto a ser criado.
        self.objects = ttk.Combobox(self, state= "readonly")
        self.objects['values'] = ('point','line', 'wireframe','Bézier Curve', 'B-splines', 'Bézier Surfaces')
        self.objects.current(0)
        self.objects.pack(pady=(0,5))

        #Cria botão 'set' para abrir a janela de criação do objeto escolhido.
        self.crate = Button(self, text='CREATE', command=self.create)
        self.crate.pack(pady=(0,5))

    def create(self):
        #Busca objeto viewport na memoria
        menu = self.mainframe.getMenu()
        interface = menu.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        #Cria janela para criação do objeto
        top = windowCreationObject(menu)

        #Define que tipo de objeto será criado
        if self.objects.get() == 'point':
            top.createPoint(viewport)
        if self.objects.get() == 'line':
            top.createLine(viewport)
        if self.objects.get() == 'wireframe':
            top.createWireframe(viewport)
        if self.objects.get() == 'Bézier Curve':
            top.createBezierCurve(viewport)
        if self.objects.get() == 'B-splines':
            top.createBSpline(viewport)
        if self.objects.get() == 'Bézier Surfaces':
            top.createBezierSurfaces(viewport)
        #Inicia janela
        top.mainloop()