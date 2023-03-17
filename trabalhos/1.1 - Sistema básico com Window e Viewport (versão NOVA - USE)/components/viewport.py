from tkinter import *
from components.window import Window



class Viewport(Canvas):
    """
    ...
        Uma classe para criar um canvas Viewport.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o canvas será alocado.

        _scrollbar_VERTICAL: Scrollbar
            Objeto scrollbar para movimento vertical da window.

        _scrollbar_HORIZONTAL: Scrollbar
            Objeto scrollbar para movimento horizontal da window.

    Atributos
    ---------
        _window: Window
            Objeto Windo.

    Métodos
    -------
        getWindow() -> Window:
            Retorna o objeto Window
    """
    
    def __init__(self, mainframe, scrollbar_VERTICAL, scrollbar_HORIZONTAL):
        Canvas.__init__(self,mainframe, 
                        width=700, 
                        height=480,
                        borderwidth=2, 
                        relief=SUNKEN,  
                        yscrollcommand=scrollbar_VERTICAL.set, 
                        xscrollcommand=scrollbar_HORIZONTAL.set)

        #Gera objeto window.
        self.window = Window(self)
        self.create_window(350,240, window=self.window)

    def getWindow(self):
        return self.window
