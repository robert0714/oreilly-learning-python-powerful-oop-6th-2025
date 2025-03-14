class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 62.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __setattr__ too
        self.age  = age                          # _acct not mangled: name tested
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    def __getattr__(self, name):
        match name:
            case 'acct':                               # On undefined attr fetches
                return self._acct[:-3] + '***'         # name, age, addr are defined
            case 'remain':
                return self.retireage - self.age       # Doesn't trigger __getattr__
            case _:
                raise AttributeError(name)

    def __setattr__(self, name, value):
        match name:
            case 'name':                                 # On all attr assignments
                value = value.lower().replace(' ', '_')  # addr stored directly
            case 'age':                                  # acct mangled to _acct
                if value < 0 or value > 150:
                    raise ValueError('invalid age')
            case 'acct':
                name  = '_acct'
                value = value.replace('-', '')
                if len(value) != self.acctlen:
                    raise TypeError('invalid acct number')
            case 'remain':
                raise TypeError('cannot set remain')
        self.__dict__[name] = value                      # Avoid looping (or object)

