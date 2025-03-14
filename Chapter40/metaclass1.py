class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Super:
    pass

print('Making class')
class Hack(Super, metaclass=MetaOne):     # Inherits from Super, instance of MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        return self.data + arg

print('Making instance')
X = Hack()
print('Attrs:', X.data, X.meth(2))

