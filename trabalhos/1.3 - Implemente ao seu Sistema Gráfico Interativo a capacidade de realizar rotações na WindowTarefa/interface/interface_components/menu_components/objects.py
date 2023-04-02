from tkinter import * 
from interface.interface_components.menu_components.objects_components.newobject import NewObject
from interface.interface_components.menu_components.objects_components.currentobjects import CurrentObjects

class Objects(Frame):
    """
    ...
        Uma classe para criar um frame Objects.
    ...

    Args
    ---------
        _mainframe: Tk
            Objeto tk onde o frame será alocado.

    
    Atributos
    ---------
        _text:
            Objeto Label para apresentar o texto 'Objects'.

        _newObject:
            Objeto NewObject.

        _currentObjects:
            Objeto CurrentObjects:
            

    Métodos
    -------
        getMenu() -> Menu:
            Retorna o objeto Menu

        getCurrentObjects() -> CurrentObjects:
            Retorn o objeto CurrentObjects.

    """
        
    def __init__(self, mainframe):
        self.menu = mainframe

        #Set frame Menu.
        Frame.__init__(self, 
                       mainframe, 
                       width=200, 
                       height=220, 
                       background="#9b9b9b",
                       highlightbackground="black",
                       highlightthickness=1)
        
        self.pack_propagate(0)
        
        #Cria label com texto 'Window'.
        self.text = Label(self, text='Objects', background="#9b9b9b")
        self.text.pack(padx=5, pady=(0,5))

        #Gera frame NewObject no menu.
        self.newObject = NewObject(self)
        self.newObject.pack(padx=5, pady=(0,5))

        #Gera frame CurrentObjects no menu.
        self.currentObjects = CurrentObjects(self)
        self.currentObjects.pack(padx=5, pady=(0,5))


    def getMenu(self):
        return self.menu
    
    def getCurrentObjects(self):
        return self.currentObjects
