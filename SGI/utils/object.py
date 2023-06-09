

class Object():
        """
        ...
                Uma classe que representa um objeto no mundo.
        ...
        
        Args
        ---------
                _name: Str
                        Nome do objeto.

                _type: Int
                        Tipo do objeto (1: ponto, 2: linha, 3: wireframe).

                _points: list
                        Lista com os pontos do objeto.

                _color: Str
                        Cor do objeto.

                _Closed: Boolean
                        Identifica se o objeto é fechado ou aberto(default: False).

        Atributos
        ---------
                _name: Str
                        Nome do objeto

                _type: Int
                        Tipo do objeto (1: ponto, 2: linha, 3: wireframe)

                _points: list
                        Lista com os pontos do objeto.

                _color: Str
                        Cor do objeto.

                _Closed: Boolean
                        Identifica se o objeto é fechado ou aberto(default: False).

        Métodos
        -------
                getType() -> Int:
                        Retorna o tipo do objeto.

                getPoints() -> List:
                        Retorna os pontos do objeto.

                getColor() -> Str:
                        Retorna a cor do objeto.

                isClosed() -> Boolean:
                        Verifica se o objeto é fechado.
        """

        def __init__(self, name, type, points):
                self.name = name
                self.type = type
                self.points = points

        def getType(self):
                return self.type

        def getPoints(self):
                return self.points
        
        def setPoints(self, points):
                self.points = points
        def addPoint(self, point):
                self.points.append(point)

        def setType(self, type):
                self.type = type
        
        def getName(self):
                return self.name
        

