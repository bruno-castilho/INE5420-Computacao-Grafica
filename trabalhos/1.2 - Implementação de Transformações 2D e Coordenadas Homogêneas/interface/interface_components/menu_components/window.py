from tkinter import * 
from interface.interface_components.menu_components.window_components.zoom import Zoom
from interface.interface_components.menu_components.window_components.move import Move

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
            Objeto zoom.
        
        _move:
            Objeto move.


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
                       height=220, 
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
        
    def getMenu(self):
        return self.menu
