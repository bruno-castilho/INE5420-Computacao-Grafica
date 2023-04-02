from tkinter import * 
from interface.interface_components.menu_components.window_components.zoom import Zoom
from interface.interface_components.menu_components.window_components.move import Move
from interface.interface_components.menu_components.window_components.rotation import Rotation

class Window(Frame):
    """
    ...
        Uma classe para criar um frame Window.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    
    Atributos
    ---------
        _text:
            Objeto Label para apresentar o texto 'Window'.
            
        _zoom:
            Objeto Zoom.
        
        _move:
            Objeto Move.

        _rotation:
            Objeto Rotation.

    Métodos
    -------
        getMenu() -> Menu:
            Retorna o objeto Menu
    """
        
    def __init__(self, mainframe):
        self.menu = mainframe

        #Set frame Menu.
        Frame.__init__(self, 
                       mainframe, 
                       width=200, 
                       height=325, 
                       background="#9b9b9b",
                       highlightbackground="black",
                       highlightthickness=1)
        
        self.pack_propagate(0)
        
        #Cria label com texto 'Window'.
        self.text = Label(self, text='Window', background="#9b9b9b")
        self.text.pack(padx=5, pady=(0,5))

        #Gera frame zoom no menu.
        self.zoom = Zoom(self)
        self.zoom.pack(padx=5, pady=(0,5))

        #Gera frame move no menu.
        self.move = Move(self)
        self.move.pack(padx=5, pady=(0,5))

        #Gera frame rotation no menu.
        self.rotation = Rotation(self)
        self.rotation.pack(padx=5, pady=(0,5))
        
    def getMenu(self):
        return self.menu
