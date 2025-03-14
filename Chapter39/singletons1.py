instances = {}

def singleton(aClass):                          # On @ decoration
    def onCall(*args, **kwargs):                # On instance creation
        if aClass not in instances:             # One dict entry per class
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

