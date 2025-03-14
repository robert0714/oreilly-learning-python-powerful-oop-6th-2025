class Privacy:
    def __setattr__(self, attr, value):             # On self.attr = value
        if attr in self.privates:
            raise NameError(f'{attr!r} for {self}') 
        else:
            self.__dict__[attr] = value             # Avoid loops by using dict key

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Pat'               # To do better, see Chapter 39!

if __name__ == '__main__':
    x = Test1()
    x.name = 'Sue'      # Works
    print(x.name)
   #x.age = 40          # Fails

    y = Test2()
    y.age = 30          # Works
    print(y.age)
   #y.name = 'Bob'      # Fails

