from tkinter import *
from tkinter import ttk
from interface.interface_components.menu_components.objects_components.windowtransform import windowTransform

class CurrentObjects(Frame):
    """
    ...
        Uma classe para criar um frame CurrentObjects.
    ...
    
    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    Atributos
    ---------
        _text: Label
            Objeto Label para apresentar o texto 'Current Objects'.

        _objectsBoxList: Combobox
            Objeto Combobox para escolha de um objeto já existente.

        _transform: Button
            Objeto Button para abrir a janela de transformação de objeto.

    Métodos
    -------
        openWindow() -> None:
            Abre uma janela de transformação de objeto.

        updateObjects(dic: displayfile) -> None:
            Atualiza boxList de objetos.

    """
    def __init__(self, mainframe):
        self.mainframe = mainframe

        #Set CurrentObjects.
        Frame.__init__(self, 
                       mainframe, 
                       background="#9b9b9b",
                       width=180, 
                       height=90)
        self.pack_propagate(0)

        #Cria label com texto 'Current Objects'.
        self.text = Label(self, text='Current Objects', background="#9b9b9b")
        self.text.pack(pady=(0,5))

        #Cria boxlist para listagem de objetos existentes.
        self.objectsBoxList = ttk.Combobox(self, state= "readonly")
        self.objectsBoxList.pack(pady=(0,5))

        #Cria botão 'transform' para abrir a janela de transformação de objeto.
        self.transform = Button(self, text='TRANSFORM', command=self.openWindow)
        self.transform.pack(pady=(0,5))
    
    def openWindow(self):
        #Busca viewport na memoria.
        menu = self.mainframe.getMenu()
        interface = menu.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        #Cria janela para transformar objeto.
        top = windowTransform(self.objectsBoxList.get(), viewport)

        #Inicia janela
        top.mainloop()
    
    def updateObjects(self, displayfile):
        #Atualiza boxList
        self.objectsBoxList['values'] = list(displayfile.keys())
        self.objectsBoxList.current(0)
        

