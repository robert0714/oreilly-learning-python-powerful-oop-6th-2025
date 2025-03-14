"Same, but with descriptors (per-instance state)"

class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers:
    square = DescSquare()
    cube   = DescCube()
    def __init__(self, square, cube):
        self._square = square                  # "self.square = square" works too,
        self._cube   = cube                    # because it triggers desc __set__!

