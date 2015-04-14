""" Receives constants to know how to communicate and uses comport """
import time as systime


class Actuators:
    def __init__(self, constants, comport):
        self.constants = constants
        self.comport = comport

    def write(self, command, value):
        self.comport.write(command)
        systime.sleep(0.1)
        self.comport.write(value)

    def solenoid(self, value):
        # make conversions if needed
        self.write(self.constants.cmdSolenoid, value)
        return self.comport.read()
