from utils.window import Window
from utils.object import Object

#Lista de objetos.
displayfile = {
    'CW': {'minha_superficie':Object('minha_superficie', 6, [[0,0,0],
                 [30,30,40],
                 [30,60,30],
                 [30,100,0],
                 [30,200.5,20],
                 [30,250.5,20],
                 [30,300.5,20],
                 [30,350.5,20],
                 [70,20.5,20],
                 [90,20.5,20],
                 [10,20.5,20],
                 [20,20.5,20],
                 [90,20.5,20],
                 [0,20.5,20],
                 [10,20.5,20],
                 [90,20.5,20]
                 ], 'red')},
    'CN': {}}

#Objeto window.
window = Window(0,0,0, 690,460, 0)

#Window normalizada
WN = [[-1,-1,0], [-1,1,0], [1,1,0], [1,-1,0]] 
Mode_clipping = {'value':'Liang Barsky'}