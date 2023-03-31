from tkinter import * 
from interface.interface_components.menu_componenets.newobject import NewObject
from interface.interface_components.menu_componenets.zoom import Zoom
from interface.interface_components.menu_componenets.move import Move

class Menu(Frame):
    """
    ...
        Uma classe para criar um frame Menu.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    
    Atributos
    ---------
        _zoom:
            Objeto zoom.
        
        _move:
            Objeto move.

        _objects:
            Objeto objects.

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

        #Gera frame move no menu.
        self.move = Move(self)
        self.move.pack(padx=5 ,pady=5)
        
        #Gera frame objects no menu.
        self.objects = NewObject(self)
        self.objects.pack(padx=5, pady=5)

    def getInterface(self):
        return self.interface
