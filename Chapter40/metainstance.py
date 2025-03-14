class Meta(type):
    def __new__(meta, classname, supers, classdict):        # Redefine type method
        print('In Meta.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def meth3(self):
        return 'three!'

class Super(metaclass=Meta):           # Metaclass inherited by subs too
    def meth2(self):                   # Meta run twice for two classes
        return 'two!'

class Sub(Super):                      # Superclass: inheritance versus instance
    def meth1(self):                   # Classes inherit from superclasses
        return 'one!'                  # But not from metaclasses for instance access

