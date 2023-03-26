from tkinter import *
from components.workspace import Workspace
from components.menu import Menu


class Interface(Tk):
    """
    ...
        Uma classe para criar a interface.
    ...
    
    Atributos
    ---------
        _workspace: Workspace
            Objeto Workspace

        _menu: Menu
            Objeto Menu

    Métodos
    -------
        getWorkspace() -> Workspace:
            Retorna o objeto workspace.
    """

    def __init__(self):
        
        #Set janela Interface.
        Tk.__init__(self)
        self.title("Sistema Gráfico Interativo")
        self.geometry("950x700")
        self.resizable(False, False)
        self.config(bg="skyblue")

        #Gera objeto Workspace.
        self.workspace = Workspace(self)
        self.workspace.grid(column=1, row=0, pady=25, padx=(0,5))

        #Gera objeto Menu
        self.menu = Menu(self)
        self.menu.grid(column=0, row=0, padx=5)
            
    def getWorkspace(self):
        return self.workspace
    

