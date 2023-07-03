from tkinter import * 
from utils.transform import Transform
from globals import *
from utils.file import File

class windowFile(Toplevel):
    """
    ...
        Uma classe para criar um Toplevel Objects.
    ...

    Args
    ---------

    Atributos
    ---------

    Métodos
    -------

    """
    def __init__(self, objects):
        #Set janela windowTransform.
        Toplevel.__init__(self)
        #Busca frame currentObjects na memoria.
        self.currentObjects = objects.getCurrentObjects()
        
        self.geometry("300x100")
        self.config(bg="skyblue")
        
        self.labelFilename = Label(self, text='Filename:', bg="skyblue")
        self.labelFilename.pack(pady=(10,0))

        self.filename = Entry(self, width=25)
        self.filename.pack(pady=(0,5))
        
    def imp(self, viewport):
        def confirm():
            filename = self.filename.get()
            File.read(f'./obj/{filename}')
            self.currentObjects.updateObjects()
            viewport.draw()
        
        btn = Button(self, text='OK', command=confirm)
        btn.pack(pady=(10,10))
    
    def exp(self):
        def confirm():
            filename = self.filename.get()
            File.write(f'./obj/{filename}')
            
        btn = Button(self, text='OK', command=confirm)
        
        btn.pack(pady=(10,10))

