from tkinter import * 
from tkinter import ttk

class windowCreationObject(Toplevel):
    """
    ...
        Uma classe para criar um Toplevel Objects.
    ...

    Atributos
    ---------
        _labelCor: Label
            Objeto Label para apresentar o texto 'Cor:'.

        _color: Combobox
            Objeto Combobox para escolha de cor ('black','red', 'yellow', 'blue', 'green', 'gray', 'orange').

        _entrys: Frame
            Objeto Frame para ser posicionados as entradas dos pontos. 

    Métodos
    -------
        createPoint(Canvas: window) -> None:
            Monta a janela para criar um ponto.

        createLine(Canvas: window) -> None:
            Monta a janela para criar uma linha.

        createWireframe(Canvas: window) -> None:
            Monta a janela para criar um wireframe.
    """
    def __init__(self):
        Toplevel.__init__(self)

        #Cria label com texto 'Cor:'.
        self.labelCor = Label(self, text='Cor:')
        self.labelCor.pack(pady=(10,5))

        #Cria boxlist para escolha da cor do objeto a ser desenhado.
        self.color = ttk.Combobox(self, state= "readonly")
        self.color['values'] = ('black','red', 'yellow', 'blue', 'green', 'gray', 'orange')
        self.color.current(0)
        self.color.pack(pady=(0,10), padx=20)

        #Cria frame para posicionar as entrys.
        self.entrys = Frame(self)
        self.entrys.pack(pady=(10,10))

    def createPoint(self, window):
        #Cria label com texto 'Point:'.
        labelPoint = Label(self.entrys, text='Point:')
        labelPoint.grid(row=0, column=0, pady=5, columnspan=4)
        
        #Cria label com texto 'X:'.
        labelX = Label(self.entrys, text='X:') 
        labelX.grid(row=1, column=0, pady=5, padx=2)
        #Cria entry para receber 'x'
        x = Entry(self.entrys, width=5)
        x.grid(row=1, column=1, padx=2)

        #Cria label com texto 'Y:'.
        labelY = Label(self.entrys, text='Y:')
        labelY.grid(row=1, column=2, pady=5, padx=2)

        #Cria entry para receber 'y'.
        y = Entry(self.entrys, width=5)
        y.grid(row=1, column=3, padx=2)

        #Lista com o ponto a ser criado.
        point = [(x,y)]

        #Cria o botão 'OK' para desenhar o ponto.
        btn = Button(self, text='OK', width=3, command=lambda: window.create_object('point', point, self.color))
        btn.pack(pady=(10,10))

    def createLine(self, window):
        ########## Point-1 ##########
        #Cria label com texto 'Point-1:'.
        labelPoint_1 = Label(self.entrys, text='Point-1:')
        labelPoint_1.grid(row=0, column=0, pady=5, columnspan=4)
        
        #Cria label com texto 'X:'.
        labelX_1 = Label(self.entrys, text='X:')
        labelX_1.grid(row=1, column=0, pady=5, padx=2)
        #Cria entry para receber 'x_1'.
        x_1 = Entry(self.entrys, width=5)
        x_1.grid(row=1, column=1, padx=2)

        #Cria label com texto 'Y:'.        
        labelY_1 = Label(self.entrys, text='Y:')
        labelY_1.grid(row=1, column=2, pady=5, padx=2)
        #Cria entry para receber 'y_1'.
        y_1 = Entry(self.entrys, width=5)
        y_1.grid(row=1, column=3, padx=2)


        ########## Point-2 ##########
        #Cria label com texto 'Point-2:'.
        labelPoint_2 = Label(self.entrys, text='Point-2:')
        labelPoint_2.grid(row=2, column=0, pady=5, columnspan=4)
        
        #Cria label com texto 'X:'.
        labelX_2 = Label(self.entrys, text='X:')
        labelX_2.grid(row=3, column=0, pady=5, padx=2)
        #Cria entry para receber 'x_2'.
        x_2 = Entry(self.entrys, width=5)
        x_2.grid(row=3, column=1, padx=2)


        #Cria label com texto 'Y:'.
        labelY_2 = Label(self.entrys, text='Y:')
        labelY_2.grid(row=3, column=2, pady=5, padx=2)
        #Cria entry para receber 'y_2'.
        y_2 = Entry(self.entrys, width=5)
        y_2.grid(row=3, column=3, padx=2)

        #Cria lista com os pontos da linha.
        points = [(x_1,y_1), (x_2,y_2)]

        #Cria o botão 'OK' para desenhar a linha.
        btn = Button(self, text='OK', width=3, command=lambda: window.create_object('line', points, self.color))
        btn.pack(pady=(10,10))
    
    def createWireframe(self, window):

        ########## Point-1 ##########
        #Cria label com texto 'Point-1:'.
        labelPoint_1 = Label(self.entrys, text='Point-1:')
        labelPoint_1.grid(row=0, column=0, pady=5, columnspan=4)
        
        #Cria label com texto 'X:'.
        labelX_1 = Label(self.entrys, text='X:')
        labelX_1.grid(row=1, column=0, pady=5, padx=2)
        #Cria entry para receber 'x_1'.
        x_1 = Entry(self.entrys, width=5)
        x_1.grid(row=1, column=1, padx=2)

        labelY_1 = Label(self.entrys, text='Y:')
        labelY_1.grid(row=1, column=2, pady=5, padx=2)
        #Cria entry para receber 'y_1'.
        y_1 = Entry(self.entrys, width=5)
        y_1.grid(row=1, column=3, padx=2)

        
        ########## Point-2 ##########
        #Cria label com texto 'Point-2:'.
        labelPoint_2 = Label(self.entrys, text='Point-2:')
        labelPoint_2.grid(row=2, column=0, pady=5, columnspan=4)
        
        #Cria label com texto 'X:'.
        labelX_2 = Label(self.entrys, text='X:')
        labelX_2.grid(row=3, column=0, pady=5, padx=2)
        #Cria entry para receber 'x_2'.
        x_2 = Entry(self.entrys, width=5)
        x_2.grid(row=3, column=1, padx=2)

        #Cria label com texto 'Y:'.
        labelY_2 = Label(self.entrys, text='Y:')
        labelY_2.grid(row=3, column=2, pady=5, padx=2)
        #Cria entry para receber 'y_2'.
        y_2 = Entry(self.entrys, width=5)
        y_2.grid(row=3, column=3, padx=2)

        
        ########## Point-3 ##########
        #Cria label com texto 'Point-3:'.
        labelPoint_3 = Label(self.entrys, text='Point-3:')
        labelPoint_3.grid(row=4, column=0, pady=5, columnspan=4)

        #Cria label com texto 'X:'.
        labelX_3 = Label(self.entrys, text='X:')
        labelX_3.grid(row=5, column=0, pady=5, padx=2)
        #Cria entry para receber 'x_3'.
        x_3 = Entry(self.entrys, width=5)
        x_3.grid(row=5, column=1, padx=2)

        #Cria label com texto 'Y:'.
        labelY_3 = Label(self.entrys, text='Y:')
        labelY_3.grid(row=5, column=2, pady=5, padx=2)
        #Cria entry para receber 'y_3'.
        y_3 = Entry(self.entrys, width=5)
        y_3.grid(row=5, column=3, padx=2)

        
        ########## Point-4 ##########
        #Cria label com texto 'Point-4:'.
        labelPoint_4 = Label(self.entrys, text='Point-4:')
        labelPoint_4.grid(row=6, column=0, pady=5, columnspan=4)
        
        #Cria label com texto 'X:'.
        labelX_4 = Label(self.entrys, text='X:')
        labelX_4.grid(row=7, column=0, pady=5, padx=2)
        #Cria entry para receber 'x_4'.
        x_4 = Entry(self.entrys, width=5)
        x_4.grid(row=7, column=1, padx=2)

        #Cria label com texto 'Y:'.
        labelY_4 = Label(self.entrys, text='Y:')
        labelY_4.grid(row=7, column=2, pady=5, padx=2)
        #Cria entry para receber 'y_4'.
        y_4 = Entry(self.entrys, width=5)
        y_4.grid(row=7, column=3, padx=2)

        #Cria lista com os pontos do wireframe
        points = [(x_1,y_1),(x_2,y_2),(x_3,y_3),(x_4,y_4)]

        #Cria o botão 'OK' para desenhar o wireframe.
        btn = Button(self, text='OK', width=3, command=lambda: window.create_object('wireframe', points, self.color))
        btn.pack(pady=(10,10))
    