""" Receives constants to know how to communicate and uses comport """


class Sensors:
    def __init__(self, constants, comport):
        self.constants = constants
        self.comport = comport

    def getLuminosity(self):
        # make conversions if needed
        self.comport.write(self.constants.cmdLuminosity)
        # return float(self.comport.read())
        return self.comport.read()

    def getHumidity(self):
        # make conversions if needed
        self.comport.write(self.constants.cmdHumidity)
        # return float(self.comport.read())
        return self.comport.read()
