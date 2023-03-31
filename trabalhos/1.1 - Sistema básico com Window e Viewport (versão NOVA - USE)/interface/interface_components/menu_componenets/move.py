from tkinter import * 
from globals import *

class Move(Frame):
    """
    ...
        Uma classe para criar um frame Move.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    
    Atributos
    ---------
        _text:
            Objeto Label para apresentar o texto 'MOVE'.
        
        _up:
            Objeto Button para mover a window para cima.

        _left:
            Objeto Button para mover a window para esquerda.

        _right:
            Objeto Button para mover a window para direita.

        _down:
            Objeto Button para mover a window para baixo.

    Métodos
    -------
        moveUp(Viewport: viewport) -> None
            Move a window para cima e redesenha os objetos na viewport.

        moveLeft(Viewport: viewport) -> None
            Move a window para esquerda e redesenha os objetos na viewport.

        moveRight(Viewport: viewport) -> None
            Move a window para direita e redesenha os objetos na viewport.

        moveDown(Viewport: viewport) -> None
            Move a window para baixo e redesenha os objetos na viewport.
    """
    def __init__(self, mainframe):
        #Set frame move.
        Frame.__init__(self, mainframe, background="#9b9b9b", highlightbackground="black", highlightthickness=1, width=190, height=140)
        self.grid_propagate(0)
        self.grid_columnconfigure(0, minsize=60)
        self.grid_columnconfigure(1, minsize=60)
        self.grid_columnconfigure(2, minsize=60)

        #Busca objeto viewport na memoria.
        interface = mainframe.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        #Cria label com texto 'MOVE'.
        self.text = Label(self, text='MOVE', background="#9b9b9b")
        self.text.grid(column=0,row=0, columnspan=3, pady=5, padx=5, sticky='nwes')

        #Cria botão UP.
        self.up = Button(self, text='UP', width=3, command=lambda: self.moveUp(viewport))
        self.up.grid(column=1,row=1, sticky='nwes')

        #Cria botão LEFT.
        self.left = Button(self, text='LEFT', width=3, command=lambda: self.moveLeft(viewport))
        self.left.grid(column=0,row=2, sticky='nwes')
        
        #Cria botão RIGHT.
        self.right = Button(self, text='RIGHT', width=3, command=lambda: self.moveRight(viewport))
        self.right.grid(column=2,row=2, sticky='nwes')

        #Cria botão DOWN.
        self.down = Button(self, text='DOWN', width=3, command=lambda: self.moveDown(viewport))
        self.down.grid(column=1,row=3, sticky='nwes')

    def moveUp(self, viewport):
        #Move a window para cima.
        window.moveUp()
        #Redesenha os objetos na viewport.
        viewport.draw()
    
    def moveLeft(self, viewport):
        #Move a window para cima.
        window.moveLeft()
        #Redesenha os objetos na viewport.
        viewport.draw()
    
    def moveRight(self, viewport):
        #Move a window para cima.
        window.moveRight()
        #Redesenha os objetos na viewport.
        viewport.draw()
    
    def moveDown(self, viewport):
        #Move a window para cima.
        window.moveDown()
        #Redesenha os objetos na viewport.
        viewport.draw()