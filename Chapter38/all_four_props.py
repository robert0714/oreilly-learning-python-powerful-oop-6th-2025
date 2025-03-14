"Two dynamically computed attributes with properties"

class Powers:
    def __init__(self, square, cube):
        self._square = square                      # _square is the base value
        self._cube   = cube                        # square is the property name

    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)        # or @property decorator

    def getCube(self):
        return self._cube ** 3 
    cube = property(getCube)                       # Likewise

