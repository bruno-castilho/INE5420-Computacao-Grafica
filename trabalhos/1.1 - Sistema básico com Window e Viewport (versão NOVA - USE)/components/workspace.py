from tkinter import *
from components.viewport import Viewport
from components. debug import Debug


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
        _scrollbar_VERTICAL: Scrollbar
            Objeto Scrollbar para percorrer a viewport verticalmente.
        
        _scrollbar_HORIZONTAL: Scrollbar
            Objeto Scrollbar para percorrer a viewport horizontalmente.

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
        #Set frame workspace.
        Frame.__init__(self, 
                       mainframe, 
                       width=735, 
                       height=650, 
                       background="#9b9b9b",
                       borderwidth=2, 
                       relief=RAISED)
        self.grid_propagate(0)

        #Cria o scrollbar vertical para a viewport.
        self.scrollbar_VERTICAL = Scrollbar(self, orient=VERTICAL)
        self.scrollbar_VERTICAL.grid(column=1, row=0, pady=5 ,sticky="news")

        #Cria o scrollbar horizontal para a viewport.
        self.scrollbar_HORIZONTAL = Scrollbar(self, orient=HORIZONTAL)
        self.scrollbar_HORIZONTAL.grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky="news")

        #Gera a viewport.
        self.viewport = Viewport(self, self.scrollbar_VERTICAL, self.scrollbar_HORIZONTAL)
        self.viewport.grid(column=0, row=0, pady=(5,0), padx=5)

        #Set movimento da viewport.
        self.scrollbar_VERTICAL.config(command=self.viewport.yview)
        self.scrollbar_HORIZONTAL.config(command=self.viewport.xview)
        self.viewport.configure(scrollregion=self.viewport.bbox("all"))

        #Gera frame Debug
        self.debug = Debug(self)
        self.debug.grid(column=0, row=2, columnspan=2)

    def getViewport(self):
        return self.viewport
    
    def getDebug(self):
        return self.debug
