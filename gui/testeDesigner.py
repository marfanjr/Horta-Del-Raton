# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testeDesigner.ui'
#
# Created: Sun Apr 12 19:29:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(5, 10, 721, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButtonWater = QtGui.QPushButton(self.centralwidget)
        self.pushButtonWater.setGeometry(QtCore.QRect(6, 206, 721, 51))
        self.pushButtonWater.setObjectName("pushButtonWater")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sistema Supervisório Del Raton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonWater.setText(QtGui.QApplication.translate("MainWindow", "Regar agora", None, QtGui.QApplication.UnicodeUTF8))


