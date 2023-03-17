from tkinter import * 

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

    """
    def __init__(self, mainframe):

        #Set frame zoom
        Frame.__init__(self, mainframe, background="#9b9b9b", highlightbackground="black", highlightthickness=1, width=190, height=70)
        self.grid_propagate(0)
        self.grid_columnconfigure(0, minsize=90)
        self.grid_columnconfigure(1, minsize=90)

        #Cria label com texto 'ZOOM'
        text = Label(self, text='ZOOM', background="#9b9b9b")
        text.grid(column=0,row=0, columnspan=2, pady=5, padx=5, sticky='nwes')


        #Busca objeto window na memoria
        interface = mainframe.getInterface()
        workspace = interface.getWorks()
        viewport = workspace.getViewport()
        window = viewport.getWindow()

        #Cria botão zoomIn
        self.btn_zoomIn = Button(self, text='+', width=1, height=1, command=window.zoomIn)
        self.btn_zoomIn.grid(column=0,row=1, pady=(0, 5), padx=(5,0), sticky='e')

        #Cria botão zoomOut
        self.btn_zoomOut = Button(self, text='-', width=1, height=1, command=window.zoomOut)
        self.btn_zoomOut.grid(column=1,row=1, pady=(0, 5), padx=(0,5), sticky='w')