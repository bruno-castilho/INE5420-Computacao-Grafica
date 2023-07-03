from utils.window import Window
from utils.object import Object

#Lista de objetos.
displayfile = {
    'CW': {},
    'CN': {}}

#Objeto window.
window = Window(0,0,0, 690,460, 0)

#Window normalizada
WN = [[-1,-1,0], [-1,1,0], [1,1,0], [1,-1,0]] 
Mode_clipping = {'value':'Liang Barsky'}