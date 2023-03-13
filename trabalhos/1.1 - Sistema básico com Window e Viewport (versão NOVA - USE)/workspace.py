from tkinter import *

class Window(Canvas):
    def __init__(self, mainframe):
        Canvas.__init__(self, mainframe, bg='white', width=700, height=500)
        self.displayfile = []
    
    def zoomIn(self):
        self.scale('all', 350, 250, 2, 2)
        
    def zoomOut(self):
        self.scale('all', 350, 250, 0.5, 0.5)

    def up(self):
        for object in self.displayfile:
            self.move(object, 0, -10)
        self.update()
    
    def left(self):
        for object in self.displayfile:
            self.move(object, -10, 0)
        self.update()
    
    def right(self):
        for object in self.displayfile:
            self.move(object, 10, 0)
        self.update()

    def down(self):
        for object in self.displayfile:
            self.move(object, 0, 10)
        self.update()

    def create_object(self, object, points, color):

        if object == 'point':
            x, y = (points[0][0].get(),points[0][1].get())
            self.displayfile.append(self.create_oval(x,y,x,y,fill=color.get(), width=1))
        elif object == 'line':
            x1, y1 = (points[0][0].get(),points[0][1].get())
            x2, y2 = (points[1][0].get(),points[1][1].get())
            self.displayfile.append(self.create_line(x1,y1,x2,y2,fill=color.get()))

        elif object == 'poligno':
            x1, y1 = (points[0][0].get(),points[0][1].get())
            x2, y2 = (points[1][0].get(),points[1][1].get())
            x3, y3 = (points[2][0].get(),points[2][1].get())
            x4, y4 = (points[3][0].get(),points[3][1].get())

            self.displayfile.append(self.create_line(x1,y1,x2,y2,fill=color.get()))
            self.displayfile.append(self.create_line(x1,y1,x3,y3,fill=color.get()))
            self.displayfile.append(self.create_line(x2,y2,x4,y4,fill=color.get()))
            self.displayfile.append(self.create_line(x3,y3,x4,y4,fill=color.get()))

class Viewport(Frame):
    def __init__(self, mainframe):
        Frame.__init__(self,mainframe, bg='white', width=700, height=500, borderwidth=2, relief=SUNKEN)

        self.window = Window(self)
        self.window.pack()

    def getWindow(self):
        return self.window

class Debug(Frame):
    def __init__(self, mainframe):
        Frame.__init__(self, mainframe, width=700, height=130, borderwidth=2, relief=SUNKEN)

class Workspace(Frame):
    def __init__(self, mainframe):
        Frame.__init__(self, mainframe, width=790, height=650)

        self.viewport = Viewport(self)
        self.viewport.grid(column=0, row=0, pady=0, padx=5)

        self.debug = Debug(self)
        self.debug.grid(column=0, row=1, pady=(20,0), padx=5)

    def getViewport(self):
        return self.viewport
    
    def getDebug(self):
        return self.debug
