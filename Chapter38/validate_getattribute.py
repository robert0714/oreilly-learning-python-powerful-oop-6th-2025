class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 62.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __setattr__ too
        self.age  = age                          # acct not mangled: name tested
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    def __getattribute__(self, name):
        superget = object.__getattribute__                 # Don't loop: level up
        match name:
            case 'acct':                                   # On all attr fetches
                return superget(self, 'acct')[:-3] + '***'
            case 'remain':
                return superget(self, 'retireage') - superget(self, 'age')
            case _:
                return superget(self, name)                # name, age, addr: stored

    def __setattr__(self, name, value):
        match name:
            case 'name':                                   # On all attr assignments
                value = value.lower().replace(' ', '_')    # addr stored directly
            case 'age':
                if value < 0 or value > 150:
                    raise ValueError('invalid age')
            case 'acct':
                value = value.replace('-', '')
                if len(value) != self.acctlen:
                    raise TypeError('invalid acct number')
            case 'remain':
                raise TypeError('cannot set remain')
        self.__dict__[name] = value                         # Avoid loop, orig names

