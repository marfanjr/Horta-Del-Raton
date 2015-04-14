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

        self.initTimer(self, self.showLuminosity, 1000)

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


        # self.ui.pushButtonWater.clicked.connect(self.someFunc)

    def showInLabel(self, text):
        self.ui.textBrowser.append(text)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myMainWindow = ControlMainWindow()
    myMainWindow.show()
    sys.exit(app.exec_())
