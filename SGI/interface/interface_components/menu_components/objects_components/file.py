from tkinter import *
from tkinter import ttk
from interface.interface_components.menu_components.objects_components.windowfile import windowFile
class File(Frame):
    """
    ...

    ...
    
    Args
    ---------

    Atributos
    ---------

    Métodos
    -------

    """
    def __init__(self, mainframe):
        self.mainframe = mainframe

        #Set frame FileObject.
        Frame.__init__(self, 
                       mainframe, 
                       background="#9b9b9b",
                       width=180, 
                       height=90)
        
        #Cria label com texto 'File'.
        self.text = Label(self, text='File', background="#9b9b9b")
        self.text.pack(pady=(0,5))
        
        #Cria botão 'import'
        self.imp = Button(self, text='IMPORT', command=self.im)
        self.imp.pack(pady=(0,5))
        
        #Cria botão 'export'
        self.exp = Button(self, text='EXPORT', command=self.exp)
        self.exp.pack(pady=(0,5))

    def im(self):
        menu = self.mainframe.getMenu()
        interface = menu.getInterface()
        workspace = interface.getWorkspace()
        viewport = workspace.getViewport()

        top = windowFile(self.mainframe)
        top.imp(viewport)
        
        top.mainloop()
        
    
    def exp(self):
        top = windowFile()
        top.exp()
        
        top.mainloop()

