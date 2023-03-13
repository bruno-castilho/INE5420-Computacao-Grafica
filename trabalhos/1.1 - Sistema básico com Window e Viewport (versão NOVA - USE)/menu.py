from tkinter import * 
from tkinter import ttk
class Zoom(Frame):
    def __init__(self, mainframe):

        Frame.__init__(self, mainframe, highlightbackground="grey", highlightthickness=1)
        self.grid(column=0,row=0, pady=5)

        text = Label(self, text='ZOOM')
        text.grid(column=0,row=0, columnspan=2, pady=(0, 5))

        interface = mainframe.getInterface()
        workspace = interface.getWorks()
        viewport = workspace.getViewport()
        window = viewport.getWindow()

        btn = Button(self, text='+', width=1, height=1, command=window.zoomIn)
        btn.grid(column=0,row=1, padx=(55,1), pady=(0, 5))

        btn = Button(self, text='-', width=1, height=1, command=window.zoomOut)
        btn.grid(column=1,row=1, padx=(1,55),pady=(0, 5))
        
class Move(Frame):
    def __init__(self, mainframe):
        Frame.__init__(self, mainframe, highlightbackground="grey", highlightthickness=1)
        self.grid(column=0,row=1, pady=5)

        interface = mainframe.getInterface()
        workspace = interface.getWorks()
        viewport = workspace.getViewport()
        window = viewport.getWindow()

        text = Label(self, text='MOVE')
        text.grid(column=0,row=0, columnspan=3,padx=71, pady=(0,5))


        btn = Button(self, text='UP', width=3, command=window.up)
        btn.grid(column=1,row=1 )

        btn = Button(self, text='LEFT', width=3, command=window.left)
        btn.grid(column=0,row=2)


        btn = Button(self, text='RIGHT', width=3, command=window.right)
        btn.grid(column=2,row=2)

        btn = Button(self, text='DOWN', width=3, command=window.down)
        btn.grid(column=1,row=3, pady=(0,5))

class Objects(Frame):
    def __init__(self, mainframe):
        self.menu = mainframe
        Frame.__init__(self, self.menu, highlightbackground="grey", highlightthickness=1)

        self.text = Label(self, text='Objects')
        self.text.pack(padx=66, pady=(0,5))
        

        self.object = ttk.Combobox(self, state= "readonly")
        self.object['values'] = ('point','line', 'poligno')
        self.object.current(0)
        self.object.pack(pady=(0,5))

        btn = Button(self, text='SET', command=self.set)
        btn.pack(pady=(0,5))

    def set(self):
        interface = self.menu.getInterface()
        workspace = interface.getWorks()
        viewport = workspace.getViewport()
        window = viewport.getWindow()

        top = Toplevel()

        labelCor = Label(top, text='Cor:')
        labelCor.pack(pady=(10,5))
        color = ttk.Combobox(top, state= "readonly")
        color['values'] = ('black','red', 'yellow', 'blue', 'green', 'gray', 'orange')
        color.current(0)
        color.pack(pady=(0,10), padx=20)

        entrys = Frame(top)
        entrys.pack(pady=(10,10))

        points = []

        if self.object.get() == 'point':
            labelPoint = Label(entrys, text='Point:')
            labelPoint.grid(row=0, column=0, pady=5, columnspan=4)
            
            labelX = Label(entrys, text='X:')
            labelX.grid(row=1, column=0, pady=5, padx=2)
            x = Entry(entrys, width=5)
            x.grid(row=1, column=1, padx=2)

            labelY = Label(entrys, text='Y:')
            labelY.grid(row=1, column=2, pady=5, padx=2)
            y = Entry(entrys, width=5)
            y.grid(row=1, column=3, padx=2)

            points.append((x,y))

        if self.object.get() == 'line':
            labelPoint_1 = Label(entrys, text='Point-1:')
            labelPoint_1.grid(row=0, column=0, pady=5, columnspan=4)
            
            labelX_1 = Label(entrys, text='X:')
            labelX_1.grid(row=1, column=0, pady=5, padx=2)
            x_1 = Entry(entrys, width=5)
            x_1.grid(row=1, column=1, padx=2)

            labelY_1 = Label(entrys, text='Y:')
            labelY_1.grid(row=1, column=2, pady=5, padx=2)
            y_1 = Entry(entrys, width=5)
            y_1.grid(row=1, column=3, padx=2)


            labelPoint_2 = Label(entrys, text='Point-2:')
            labelPoint_2.grid(row=2, column=0, pady=5, columnspan=4)
            
            labelX_2 = Label(entrys, text='X:')
            labelX_2.grid(row=3, column=0, pady=5, padx=2)
            x_2 = Entry(entrys, width=5)
            x_2.grid(row=3, column=1, padx=2)

            labelY_2 = Label(entrys, text='Y:')
            labelY_2.grid(row=3, column=2, pady=5, padx=2)
            y_2 = Entry(entrys, width=5)
            y_2.grid(row=3, column=3, padx=2)


            points.append((x_1,y_1))
            points.append((x_2,y_2))

        if self.object.get() == 'poligno':
            labelPoint_1 = Label(entrys, text='Point-1:')
            labelPoint_1.grid(row=0, column=0, pady=5, columnspan=4)
            
            labelX_1 = Label(entrys, text='X:')
            labelX_1.grid(row=1, column=0, pady=5, padx=2)
            x_1 = Entry(entrys, width=5)
            x_1.grid(row=1, column=1, padx=2)

            labelY_1 = Label(entrys, text='Y:')
            labelY_1.grid(row=1, column=2, pady=5, padx=2)
            y_1 = Entry(entrys, width=5)
            y_1.grid(row=1, column=3, padx=2)

            labelPoint_2 = Label(entrys, text='Point-2:')
            labelPoint_2.grid(row=2, column=0, pady=5, columnspan=4)
            
            labelX_2 = Label(entrys, text='X:')
            labelX_2.grid(row=3, column=0, pady=5, padx=2)
            x_2 = Entry(entrys, width=5)
            x_2.grid(row=3, column=1, padx=2)

            labelY_2 = Label(entrys, text='Y:')
            labelY_2.grid(row=3, column=2, pady=5, padx=2)
            y_2 = Entry(entrys, width=5)
            y_2.grid(row=3, column=3, padx=2)

            labelPoint_3 = Label(entrys, text='Point-3:')
            labelPoint_3.grid(row=4, column=0, pady=5, columnspan=4)
            
            labelX_3 = Label(entrys, text='X:')
            labelX_3.grid(row=5, column=0, pady=5, padx=2)
            x_3 = Entry(entrys, width=5)
            x_3.grid(row=5, column=1, padx=2)

            labelY_3 = Label(entrys, text='Y:')
            labelY_3.grid(row=5, column=2, pady=5, padx=2)
            y_3 = Entry(entrys, width=5)
            y_3.grid(row=5, column=3, padx=2)

            labelPoint_4 = Label(entrys, text='Point-4:')
            labelPoint_4.grid(row=6, column=0, pady=5, columnspan=4)
            
            labelX_4 = Label(entrys, text='X:')
            labelX_4.grid(row=7, column=0, pady=5, padx=2)
            x_4 = Entry(entrys, width=5)
            x_4.grid(row=7, column=1, padx=2)

            labelY_4 = Label(entrys, text='Y:')
            labelY_4.grid(row=7, column=2, pady=5, padx=2)
            y_4 = Entry(entrys, width=5)
            y_4.grid(row=7, column=3, padx=2)

            points.append((x_1,y_1))
            points.append((x_2,y_2))
            points.append((x_3,y_3))
            points.append((x_4,y_4))

        btn = Button(top, text='OK', width=3, command=lambda: window.create_object(self.object.get(), points, color))
        btn.pack(pady=(10,10))

        top.mainloop()

class Menu(Frame):
    def __init__(self, mainframe, interface):
        self.interface = interface
        Frame.__init__(self, mainframe, width=200, height=650, borderwidth=2, relief=RAISED)

        self.zom = Zoom(self)
        self.move = Move(self)
        self.objects = Objects(self)
        self.objects.grid(column=0,row=2, pady=(5, 345), padx=5)
    
    def getInterface(self):
        return self.interface
