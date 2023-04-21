from tkinter import * 
from globals import *
from utils.transform import Transform

class Rotation(Frame):
    """
    ...
        Uma classe para criar um frame Rotation.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    Atributos
    ---------
        _text: Label
            Objeto Label para apresentar o texto 'ROTATION'.

        _labelAngle: Label
            Label com o texto 'Angle:'.

        _angle: Entry
            Entry para receber angulo para rotação da window.

        _btn_rotation: Button
            Botão para rotacionar a window.

    Métodos
    -------
        rotation(Viewport: viewport) -> None
            Roda a window e redesenha objetos na viewport.

    """
    
    def __init__(self, mainframe):

        #Set frame zoom
        Frame.__init__(self, mainframe, background="#9b9b9b", width=180, height=100)

        #Cria label com texto 'ZOOM'
        self.text = Label(self, text='ROTATION', background="#9b9b9b")
        self.text.grid(column=0,row=0, columnspan=2, sticky='nwes')

        #Busca objeto viewport na memoria
        menu = mainframe.getMenu()
        interface = menu.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        #Cria label com texto 'Angle:'.
        self.labelAngle = Label(self, text='Angle:', background="#9b9b9b")
        self.labelAngle.grid(row=1, column=0, pady=5)

        #Cria entry para receber 'angle'.
        self.angle = Entry(self, width=5)
        self.angle.grid(row=1, column=1)

        #Cria botão RIGHT
        self.btn_rotation = Button(self, text='SET', width=3, height=1, command=lambda: self.rotation(viewport))
        self.btn_rotation.grid(column=0,row=2,columnspan=2)

    def rotation(self, viewport):
        #Aumenta tamanho da window.
        window.rotation(float(self.angle.get()))
        #Redesenha os objetos na viewport.
        viewport.draw()

