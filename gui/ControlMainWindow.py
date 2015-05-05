from __future__ import absolute_import
from testeDesigner import Ui_MainWindow
from PySide import QtGui, QtCore
from horta.utils import constants
from horta.hw import actuators, comport, sensors
import sys


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initHw()
        self.initTimer(self, self.showHumidity, 2000)
        self.initTimer(self, self.showLuminosity, 3000)
        self.ui.pushButtonWater.clicked.connect(self.workForMe)

    def initHw(self):
        # init the hardware configurations
        constant = constants.Constants()
        port = comport.Comport(constant)

        self.sensor = sensors.Sensors(constant, port)
        self.actuator = actuators.Actuators(constant, port)

    def initTimer(self, window, function, timeInterval):
        # defines the frequency of execution for a given function
        timer = QtCore.QTimer(window)
        timer.timeout.connect(function)
        timer.start(timeInterval)

    def showLuminosity(self):
        self.luminosity = self.sensor.getLuminosity()
        self.showInLabel(self.luminosity)

    def showHumidity(self):
        self.humidity = self.sensor.getHumidity()
        self.showInLabel(self.humidity)

    def showListening(self):
        self.listening = self.sensor.getListening()
        self.showInLabel(self.listening)

    def showInLabel(self, text):
        self.ui.textBrowser.append(text)

    def workForMe(self):
        self.ui.textBrowser.append(self.actuator.solenoid(1))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myMainWindow = ControlMainWindow()
    myMainWindow.show()
    sys.exit(app.exec_())
