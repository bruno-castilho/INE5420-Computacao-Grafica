from utils.window import Window
from utils.object import Object

#Lista de objetos.
displayfile = {
    'CW': {'minha_superficie':Object('minha_superficie', 5, [[0,0,0],
                 [0,30,40],
                 [0,60,30],
                 [0,100,0],
                 [30,20.5,20],
                 [20,60,50],
                 [30,80,50],
                 [40,00,20],
                 [60,30,20],
                 [80,60,50],
                 [70,100,40.5],
                 [60,0,20.5],
                 [100,0,0],
                 [110,30,40],
                 [110,60,30],
                 [100,90,0]
                 ], 'red')},
    'CN': {}}

#Objeto window.
window = Window(0,0,0, 690,460, 0)

#Window normalizada
WN = [[-1,-1,0], [-1,1,0], [1,1,0], [1,-1,0]] 
Mode_clipping = {'value':'Liang Barsky'}