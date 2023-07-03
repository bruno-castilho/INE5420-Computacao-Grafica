from tkinter import * 
from interface.interface_components.menu_components.objects import Objects
from interface.interface_components.menu_components.window import Window

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
                       height=720, 
                       background="#9b9b9b",
                       borderwidth=2, 
                       relief=RAISED)
        
        self.pack_propagate(0)

        #Gera frame window no menu.
        self.window_cofs = Window(self)
        self.window_cofs.pack(padx=5,pady=5)
        
        #Gera frame objects no menu.
        self.objects_conf = Objects(self)
        self.objects_conf.pack(padx=5, pady=5)

    def getInterface(self):
        return self.interface
    
    def getObjects(self):
        return self.objects_conf
