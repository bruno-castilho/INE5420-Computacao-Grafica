from tkinter import *
from tkinter import ttk
from components.windowcreationobject import windowCreationObject

class Objects(Frame):
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

        _object: Combobox
            Objeto Combobox para escolha de um objeto ('point','line', 'wireframe').

        _btn: Button
            Objeto Button para abrir a janela de criação do objeto escolhido.

    Métodos
    -------
        create() -> None:
            Abre uma jenala de criação de objeto, conforme o tipo.
    """
    def __init__(self, mainframe):
        self.menu = mainframe

        #Set frame objects.
        Frame.__init__(self, 
                       self.menu, 
                       highlightbackground="black", 
                       highlightthickness=1, 
                       background="#9b9b9b",
                       width=190, 
                       height=90)
        
        self.pack_propagate(0)

        #Cria label com texto 'Objects'.
        self.text = Label(self, text='Objects', background="#9b9b9b")
        self.text.pack(pady=(0,5))
        
        #Cria boxlist para escolha do objeto a ser criado.
        self.object = ttk.Combobox(self, state= "readonly")
        self.object['values'] = ('point','line', 'wireframe')
        self.object.current(0)
        self.object.pack(pady=(0,5))

        #Cria botão 'set' para abrir a janela de criação do objeto escolhido.
        self.btn = Button(self, text='SET', command=self.create)
        self.btn.pack(pady=(0,5))

    def create(self):
        #Busca objeto viewport na memoria
        interface = self.menu.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        #Cria janela para criação do objeto
        top = windowCreationObject()

        #Define que tipo de objeto será criado
        if self.object.get() == 'point':
            top.createPoint(viewport)
        if self.object.get() == 'line':
            top.createLine(viewport)
        if self.object.get() == 'wireframe':
            top.createWireframe(viewport)

        #Inicia janela
        top.mainloop()