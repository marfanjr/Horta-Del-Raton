import os


class Constants:
    """ Constants Utils """
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        file = open(BASE_DIR+'/horta/arduino/constants/constants.h')

        for line in file:
            self.parseLine(line)

    def __del__(self):
        print "Constants utils del"

    def parseLine(self, line):
        words = line.split()

        if len(words) == 3:
            if words[0] == "#define":

                if words[1] == "PORT_PATH":
                    self.serialPortPath = words[2]
                if words[1] == "BAUD_RATE":
                    self.serialBaud = words[2]
                # SENSORS
                if words[1] == "CMD_LUMINOSITY":
                    self.cmdLuminosity = words[2]
                if words[1] == "CMD_HUMIDITY":
                    self.cmdHumidity = words[2]
                # ACTUATORS
                if words[1] == "CMD_SOLENOID":
                    self.cmdSolenoid = words[2]
