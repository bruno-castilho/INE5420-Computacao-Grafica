from tkinter import *
from interface.interface_components.workspace_components.viewport import Viewport
from interface.interface_components.workspace_components.debug import Debug


class Workspace(Frame):
    """
    ...
        Uma classe para criar um frame Workspace.
    ...
    
    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    Atributos
    ---------
        _viewport: Viewport
            Objeto Viewport

        _debug: Debug
            Objeto Debug

    Métodos
    -------
        getViewport() -> Canvas:
            Retorna o objeto viewport.
        getDebug() ->:
            Retorna o objeto debug.
    """
    
    def __init__(self, mainframe):
        self.interface = mainframe
        #Set frame workspace.
        Frame.__init__(self, 
                       mainframe, 
                       width=735, 
                       height=650, 
                       background="#9b9b9b",
                       borderwidth=2, 
                       relief=RAISED)
        
        self.pack_propagate(0)



        #Gera a viewport.
        self.viewport = Viewport(self)
        self.viewport.pack(pady=(10,5), padx=10)

        #Gera frame Debug
        self.debug = Debug(self)
        self.debug.pack(pady=(5,10), padx=10)

    def getViewport(self):
        return self.viewport
    
    def getDebug(self):
        return self.debug
    
    def getInterface(self):
        return self.interface
