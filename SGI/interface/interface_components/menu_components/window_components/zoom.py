from tkinter import * 
from globals import *

class Zoom(Frame):
    """
    ...
        Uma classe para criar um frame Zoom.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    Atributos
    ---------
        _text: Label
            Objeto Label para apresentar o texto 'ZOOM'.

        _btn_zoomIn: Button
            Objeto Button para fazer o Zoom_In.

        _btn_zoomOut: Button
            Objeto Button para fazer o Zoom_Out.

    Métodos
    -------
        zoomIn(Viewport: viewport) -> None
            Aumenta o tamanho da window e redesenha objetos na viewport.

        zoomOut(Viewport: viewport) -> None
            Diminui o tamanho da window e redesenha objetos na viewport.
    """
    
    def __init__(self, mainframe):

        #Set frame zoom
        Frame.__init__(self, mainframe, background="#9b9b9b", width=180, height=60)
        self.grid_propagate(0)
        self.grid_columnconfigure(0, minsize=90)
        self.grid_columnconfigure(1, minsize=90)

        #Cria label com texto 'ZOOM'
        self.text = Label(self, text='ZOOM', background="#9b9b9b")
        self.text.grid(column=0,row=0, columnspan=2, sticky='nwes')

        #Busca objeto viewport na memoria
        menu = mainframe.getMenu()
        interface = menu.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        #Cria botão zoomIn
        self.btn_zoomIn = Button(self, text='+', width=1, height=1, command=lambda: self.zoomIn(viewport))
        self.btn_zoomIn.grid(column=0,row=1, sticky='e')

        #Cria botão zoomOut
        self.btn_zoomOut = Button(self, text='-', width=1, height=1, command=lambda: self.zoomOut(viewport))
        self.btn_zoomOut.grid(column=1,row=1, sticky='w')

    def zoomIn(self, viewport):
        #Aumenta tamanho da window.
        window.zomIn()
        #Redesenha os objetos na viewport.
        viewport.draw()

    
    def zoomOut(self, viewport):
        #Diminui tamanho da window.
        window.zomOut()
        #Redesenha os objetos na viewport.
        viewport.draw()

