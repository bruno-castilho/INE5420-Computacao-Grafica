from tkinter import *
from workspace import Workspace
from menu import Menu


class Interface():

    def __init__(self):
        self.janelaPrincipal = Tk()
        self.janelaPrincipal.title("Interface")
        self.janelaPrincipal.geometry("950x700")
        self.janelaPrincipal.resizable(False, False)

        self.workspace = Workspace(self.janelaPrincipal)
        self.workspace.grid(column=1, row=0, pady=25, padx=5)
         
        self.menu = Menu(self.janelaPrincipal, self)
        self.menu.grid(column=0, row=0, padx=5)

        self.janelaPrincipal.mainloop()
    
    def getWorks(self):
        return self.workspace
    

interface = Interface()