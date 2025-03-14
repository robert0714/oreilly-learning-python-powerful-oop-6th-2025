class Hack:
    numInstances = 0
    def __init__(self):
        Hack.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances:', Hack.numInstances)

