from tkinter import * 
from utils.transform import Transform
from globals import *

class windowTransform(Toplevel):
    """
    ...
        Uma classe para criar um Toplevel Objects.
    ...

    Args
    ---------
        _objectName: str
            Nome do objeto que será transformado.

        _viewport: Viewport
            Objeto Viewport.

    Atributos
    ---------
        _text: Label
            Objeto Label para apresentar o nome do objeto que será transformado'.

        _translation: Frame
            Objeto frame com o menu de translação.

        _scale: Frame
            Objeto frame com o menu de escala.

        _rotation_object_center: Frame
            Objeto frame com o menu de rotação pelo centro do objeto.

        _rotation_world_center: Frame
            Objeto frame com o menu de rotação pelo centro do mundo.

        _rotation_arbitrary_point: Frame
            Objeto frame com o menu de rotação por um ponto arbitrario.


    Métodos
    -------
        createFrameTranslation(str: objectName,Viewport: viewport) -> Frame
            Gera menu de translação.

        createFrameScale(str: objectName,Viewport: viewport) -> Frame
            Gera menu de escala.

        createFrameRotationObjectCenter(str: objectName,Viewport: viewport) -> Frame
            Gera menu de rotação pelo centro do objeto.
            menu 
        createFrameRotationtWorldCenter(str: objectName,Viewport: viewport) -> Frame
            Gera menu de rotação pelo centro do mundo.

        createFrameRotationArbitraryPoint(str: objectName,Viewport: viewport) -> Frame
            Gera menu de rotação por um ponto arbitrario.
    """
    def __init__(self, objectName, viewport):
        #Set janela windowTransform.
        Toplevel.__init__(self)
        self.geometry("486x255")
        self.config(bg="skyblue")
        self.resizable(False, False)
        self.grid_propagate(0)
        self.grid_columnconfigure(0, minsize=80)
        self.grid_columnconfigure(1, minsize=80)
        self.grid_columnconfigure(2, minsize=80)
        self.grid_columnconfigure(4, minsize=80)
        self.grid_columnconfigure(5, minsize=80)

        #Cria label com o nome do objeto.
        self.text = Label(self, text=objectName)
        self.text.grid(column=0, row=0, columnspan=6, sticky='nwes')

        #Cria menu de translação
        self.translation = self.createFrameTranslation(objectName, viewport)
        self.translation.grid(column=0, row=1,columnspan=3, sticky='nwes', padx=1, pady=1)

        #Cria menu de escala.
        self.scale = self.createFrameScale(objectName, viewport)
        self.scale.grid(column=3, row=1,columnspan=3, sticky='nwes', padx=1, pady=1)

        #Cria menu de rotação pelo centro do objeto.
        self.rotation_object_center = self.createFrameRotationObjectCenter(objectName, viewport)
        self.rotation_object_center.grid(column=0, row=2,columnspan=2,sticky='nwes', padx=1, pady=1)

        #Cria menu de rotação pelo centro do mundo.
        self.rotation_world_center = self.createFrameRotationtWorldCenter(objectName, viewport)
        self.rotation_world_center.grid(column=2, row=2,columnspan=2,sticky='nwes', padx=1, pady=1)

        #Cria menu de rotação por um ponto arbitrario.
        self.rotation_arbitrary_point = self.createFrameRotationArbitraryPoint(objectName, viewport)
        self.rotation_arbitrary_point.grid(column=4, row=2,columnspan=2,sticky='nwes', padx=1, pady=1)

    def createFrameTranslation(self, objectName, viewport):
        def move(dx, dy, dz):
            #Busca objeto no displayfile.
            object = displayfile['CW'][objectName]

            #Pega matriz dos pontos.
            matrix_points = object.getPoints()
            matrix_points = [point+[1] for point in matrix_points] #Adiciona 1 como um 4 elemento de cada ponto


            #Gera matriz de translação.
            matrix_transition = Transform.translation3D(dx, dy, dz)


            #matrix_points x matrix_transition
            result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_transition)] 
                                for A_row in matrix_points] 
            
            result = [point[:-1] for point in result] #Remove o 1 de cada ponto e adiciona em self.points
            #Set novos pontos
            new_points = []
            for point in result:
                new_points.append([point[0],point[1],point[2]])

            
            
            object.setPoints(new_points)
            
            #Redesenha a viewport
            viewport.draw()
            
        #Cria frame para posicionar na janela.
        translation = Frame(self, width=240, height=110,highlightbackground="black",highlightthickness=1)
        translation.pack_propagate(0)

        #Cria frame para posicionar os widgets.
        frame = Frame(translation)
        frame.pack()

        #Cria label com o texto 'Translation'.
        Label(frame, text='Translation').grid(column=0, row=0, columnspan=4,sticky='nwes', pady=5)

        #Cria campo para receber Dx.
        Label(frame, text='Dx').grid(column=0, row=1,sticky='nwes')
        Dx = Entry(frame, width=5)
        Dx.grid(column=1, row=1,sticky='nwes')

        #Cria campo para receber Dy.
        Label(frame, text='Dy').grid(column=2, row=1,sticky='nwes')
        Dy = Entry(frame, width=5)
        Dy.grid(column=3, row=1,sticky='nwes')
        
        #Cria campo para receber Dy.
        Label(frame, text='Dz').grid(column=4, row=1,sticky='nwes')
        Dz = Entry(frame, width=5)
        Dz.grid(column=5, row=1,sticky='nwes')

        #Cria botão para fazer a transformação.
        Button(frame, 
               text='set', 
               command=lambda: move(dx=float(Dx.get()), dy=float(Dy.get()), dz=float(Dz.get()))
               ).grid(column=0, row=2, columnspan=4, pady=5)
        
        return translation

    def createFrameScale(self,objectName, viewport):
        def scale(sx, sy, sz):
            #Busca objeto no displayfile.
            object = displayfile['CW'][objectName]

            #Pega matriz dos pontos.
            matrix_points = object.getPoints()
            matrix_points = [point+[1] for point in matrix_points] #Adiciona 1 como um 4 elemento de cada ponto

            #Econtra ponto central do objeto.
            cx = sum(point[0]/len(matrix_points) for point in matrix_points)
            cy = sum(point[1]/len(matrix_points) for point in matrix_points)
            cz = sum(point[2]/len(matrix_points) for point in matrix_points)
            
            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation3D(-1*cx,-1*cy, -1*cz)

            #Gera matriz de escalonamento.
            matrix_scaling = Transform.scale3D(sx, sy, sz)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation3D(cx,cy,cz)
            

            #matrix_transition_origin x matrix_scaling
            matriz_origin_scaling = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_scaling)] 
                                            for A_row in matrix_transition_origin] 

            #matrix_transition_origin x matrix_scaling X matrix_transition_initial
            matriz_origin_scaling_initial = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matriz_origin_scaling] 

            #matrix_points x matriz_origin_scaling_initial
            result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matriz_origin_scaling_initial)] 
                            for A_row in matrix_points] 
            
            result = [point[:-1] for point in result] #Remove o 1 de cada ponto e adiciona em self.points
            
            #Set novos pontos
            new_points = []
            for point in result:
                new_points.append([point[0],point[1],point[2]])

            object.setPoints(new_points)
            
            #Redesenha a viewport
            viewport.draw()

        #Cria frame para posicionar na janela.
        frameScale = Frame(self, width=240, height=110,highlightbackground="black",highlightthickness=1)
        frameScale.pack_propagate(0)

        #Cria frame para posicionar os widgets.
        frame = Frame(frameScale)
        frame.pack()

        #Cria label com o texto 'Scale'.
        Label(frame, text='Scale').grid(column=0, row=0, columnspan=4,sticky='nwes', pady=5)

        #Cria campo para receber Sx.
        Label(frame, text='Sx').grid(column=0, row=1,sticky='nwes')
        Sx = Entry(frame, width=5)
        Sx.grid(column=1, row=1,sticky='nwes')

        #Cria campo para receber Sy.
        Label(frame, text='Sy').grid(column=2, row=1,sticky='nwes')
        Sy = Entry(frame, width=5)
        Sy.grid(column=3, row=1,sticky='nwes')
        
        #Cria campo para receber Sy.
        Label(frame, text='Sy').grid(column=4, row=1,sticky='nwes')
        Sz = Entry(frame, width=5)
        Sz.grid(column=5, row=1,sticky='nwes')

        #Cria botão para fazer a transformação.
        Button(frame, 
               text='set', 
               command=lambda: scale(sx=float(Sx.get()), sy=float(Sy.get()), sz=float(Sz.get()))
               ).grid(column=0, row=2, columnspan=4, pady=5)
        
        return frameScale
    
    def createFrameRotationObjectCenter(self, objectName, viewport):
        def rotation(angle):
            #Busca objeto no displayfile.
            object = displayfile['CW'][objectName]

            #Pega matriz dos pontos.
            matrix_points = object.getPoints()

            #Econtra ponto central do objeto.
            cx = sum(point[0]/len(matrix_points) for point in matrix_points)
            cy = sum(point[1]/len(matrix_points) for point in matrix_points)

            #Gera matriz de translação para a origem.
            matrix_transition_origin = Transform.translation(-1*cx,-1*cy)

            #Gera matriz de rotação.
            matrix_rotation = Transform.rotation(angle)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation(cx,cy)
            

            #matrix_transition_origin x matrix_scaling
            matriz_origin_rotation = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation)] 
                                            for A_row in matrix_transition_origin] 

            #matrix_transition_origin x matrix_scaling X matrix_transition_initial
            matriz_origin_rotation_initial = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matriz_origin_rotation] 

            #matrix_points x matriz_origin_scaling_initial
            result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matriz_origin_rotation_initial)] 
                            for A_row in matrix_points] 
            

            #Set novos pontos
            new_points = []
            for point in result:
                new_points.append([point[0],point[1],1])

            object.setPoints(new_points)
            
            #Redesenha a viewport
            viewport.draw()

        #Cria frame para posicionar na janela.
        rotation_object_center = Frame(self, width=160, height=120,highlightbackground="black",highlightthickness=1)
        rotation_object_center.pack_propagate(0)

        #Cria frame para posicionar os widgets. 
        frame = Frame(rotation_object_center)
        frame.pack()

        #Cria label com o texto 'Rotate Objcet Center'.
        Label(frame, text='Rotate Objcet Center').grid(column=0, row=0, columnspan=2,sticky='nwes', pady=5)

        #Cria campo para receber Angle.
        Label(frame, text='Angle').grid(column=0, row=1,sticky='nwes')
        angle = Entry(frame, width=5)
        angle.grid(column=1, row=1,sticky='nwes')

        #Cria botão para fazer a transformação.
        Button(frame, 
               text='set', 
               command=lambda: rotation(angle=float(angle.get()))
               ).grid(column=0, row=2, columnspan=2, pady=5)
        
        return rotation_object_center

    def createFrameRotationtWorldCenter(self, objectName, viewport):
        def rotation(angle):
            #Busca objeto no displayfile.
            object = displayfile['CW'][objectName]

            #Pega matriz dos pontos.
            matrix_points = object.getPoints()


            #Gera matriz de rotação.
            matrix_rotation = Transform.rotation(angle)

            #matrix_points x matriz_origin_scaling_initial
            result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_rotation)] 
                            for A_row in matrix_points] 
            
            #Set novos pontos
            new_points = []
            for point in result:
                new_points.append([point[0],point[1],1])

            object.setPoints(new_points)
            
            #Redesenha a viewport
            viewport.draw()
        
        #Cria frame para posicionar na janela.
        rotation_world_center = Frame(self, width=160, height=120,highlightbackground="black",highlightthickness=1)
        rotation_world_center.pack_propagate(0)

        #Cria frame para posicionar os widgets.
        frame = Frame(rotation_world_center)
        frame.pack()

        #Cria label com o texto 'Rotate World Center'.
        Label(frame, text='Rotate World Center').grid(column=0, row=0, columnspan=2,sticky='nwes', pady=5)

        #Cria campo para receber Angle.
        Label(frame, text='Angle').grid(column=0, row=1,sticky='nwes')
        angle = Entry(frame, width=5)
        angle.grid(column=1, row=1,sticky='nwes')

        #Cria botão para fazer a transformação.
        Button(frame, 
               text='set', 
               command=lambda: rotation(angle=float(angle.get()))
               ).grid(column=0, row=2, columnspan=2, pady=5)
        
        return rotation_world_center
    
    def createFrameRotationArbitraryPoint(self, objectName, viewport):
        def rotation(angle, x, y):
            #Busca objeto no displayfile.
            object = displayfile['CW'][objectName]

            #Pega matriz dos pontos.
            matrix_points = object.getPoints()

            #Gera matriz de translação x, y.
            matrix_transition_XY = Transform.translation(-1*x,-1*y)

            #Gera matriz de rotação.
            matrix_rotation = Transform.rotation(angle)

            #Gera matriz de translação para o ponto inicial.
            matrix_transition_initial = Transform.translation(x,y)
            

            #matrix_transition_XY x matrix_scaling
            matrix_XY_rotation = [[sum(a * b for a, b in zip(A_row, B_col))  
                                        for B_col in zip(*matrix_rotation)] 
                                            for A_row in matrix_transition_XY] 

            #matrix_transition_XY x matrix_scaling X matrix_transition_initial
            matrix_XY_rotation_initial = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*matrix_transition_initial)] 
                                                    for A_row in matrix_XY_rotation] 

            #matrix_points x matriz_XY_scaling_initial
            result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*matrix_XY_rotation_initial)] 
                            for A_row in matrix_points] 
            
            #Set novos pontos
            new_points = []
            for point in result:
                new_points.append([point[0],point[1],1])

            object.setPoints(new_points)
            
            #Redesenha a viewport
            viewport.draw()

        #Cria frame para posicionar na janela.
        rotation_arbitrary_point = Frame(self, width=160, height=120, highlightbackground="black",highlightthickness=1)
        rotation_arbitrary_point.pack_propagate(0)

        #Cria frame para posicionar os widgets.
        frame = Frame(rotation_arbitrary_point)
        frame.pack()

        #Cria label com o texto 'Arbitrary Point'.
        Label(frame, text='Arbitrary Point').grid(column=0, row=0, columnspan=4,sticky='nwes', pady=5)

        #Cria campo para receber Angle.
        Label(frame, text='Angle').grid(column=0, row=1,sticky='nwes', columnspan=2)
        angle = Entry(frame, width=5)
        angle.grid(column=2, row=1,sticky='nwes', columnspan=2)

        #Cria campo para receber X.
        Label(frame, text='X').grid(column=0, row=2,sticky='nwes')
        X = Entry(frame, width=2)
        X.grid(column=1, row=2,sticky='nwes')

        #Cria campo para receber Y.
        Label(frame, text='Y').grid(column=2, row=2,sticky='nwes')
        Y = Entry(frame, width=2)
        Y.grid(column=3, row=2,sticky='nwes')

        #Cria botão para fazer a transformação.
        Button(frame, 
               text='set', 
               command=lambda: rotation(angle=float(angle.get()), x=float(X.get()), y=float(Y.get()))
               ).grid(column=0, row=3, columnspan=4, pady=5)
        
        return rotation_arbitrary_point