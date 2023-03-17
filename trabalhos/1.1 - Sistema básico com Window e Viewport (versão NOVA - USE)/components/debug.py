from tkinter import *


class Debug(Frame):
    """
    ...
        Uma classe para criar um frame Debug.
    ...
    
    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    """
    def __init__(self, mainframe):
        Frame.__init__(self, mainframe, width=720, height=125, borderwidth=2, relief=SUNKEN)