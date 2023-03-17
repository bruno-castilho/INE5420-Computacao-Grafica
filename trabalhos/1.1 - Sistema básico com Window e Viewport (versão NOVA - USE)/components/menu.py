from tkinter import * 
from components.objects import Objects
from components.zoom import Zoom
    
class Menu(Frame):
    """
    ...
        Uma classe para criar um frame Menu.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    Métodos
    -------
        getInterface() -> Interface:
            Retorna o objeto Interface
    """
        
    def __init__(self, mainframe):
        self.interface = mainframe

        #Set frame Menu.
        Frame.__init__(self, 
                       mainframe, 
                       width=200, 
                       height=650, 
                       background="#9b9b9b",
                       borderwidth=2, 
                       relief=RAISED)
        
        self.pack_propagate(0)

        #Gera frame zoom no menu.
        self.zoom = Zoom(self)
        self.zoom.pack(padx=5 ,pady=5)
        
        #Gera frame objects no menu.
        self.objects = Objects(self)
        self.objects.pack(padx=5, pady=5)

    def getInterface(self):
        return self.interface
