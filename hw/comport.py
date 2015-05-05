import serial
import time as systime


class Comport:
    """ Comport Utils """
    def __init__(self, constants):
        print "Establishing serial connection..."
        self.comport = serial.Serial(constants.serialPortPath,
                                     constants.serialBaud)
        systime.sleep(2)  # time to establish serial connection.
        self.write(2)

    def __del__(self):
        print "Closing serial connection..."
        self.write(5)
        self.comport.close()     # closing serial connection

    def write(self, command):
        print "command " + str(command)
        self.comport.write(str(command))

    def read(self):
        # return "its working!"
        return self.comport.readline()  # read from arduino
