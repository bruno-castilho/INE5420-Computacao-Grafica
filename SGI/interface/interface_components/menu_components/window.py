from tkinter import * 
from interface.interface_components.menu_components.window_components.zoom import Zoom
from interface.interface_components.menu_components.window_components.move import Move
from interface.interface_components.menu_components.window_components.rotation import Rotation
from tkinter import ttk
from globals import Mode_clipping

class Window(Frame):
    """
    ...
        Uma classe para criar um menu de interação com a window.
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
                       height=370, 
                       background="#9b9b9b",
                       highlightbackground="black",
                       highlightthickness=1)
        
        self.pack_propagate(0)
        
        #Cria label com texto 'Window'.
        self.text = Label(self, text='Window', background="#9b9b9b")
        self.text.pack(padx=5, pady=(0,5))

        #Cria lista para escolha de modo de clipping de linha
        Label(self, text='Clipping Mode:', background="#9b9b9b").pack(padx=5)
        self.mode_clipping = ttk.Combobox(self, state= "readonly", values=['Liang Barsky', 'Cohen Sutherland'])
        self.mode_clipping.pack(pady=(0,5))
        self.mode_clipping.current(0)
        self.mode_clipping.bind('<<ComboboxSelected>>', self.mode_clipping_canged)

        #Gera frame zoom no menu.
        self.zoom = Zoom(self)
        self.zoom.pack(padx=5, pady=(0,5))

        #Gera frame move no menu.
        self.move = Move(self)
        self.move.pack(padx=5, pady=(0,5))

        #Gera frame rotation no menu.
        self.rotation = Rotation(self)
        self.rotation.pack(padx=5, pady=(0,5))
    
    def mode_clipping_canged(self,event):
        Mode_clipping['value'] = self.mode_clipping.get()


    def getMenu(self):
        return self.menu
