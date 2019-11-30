# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythonblue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyfirmata
from PyQt5.QtCore import pyqtSlot


board = pyfirmata.Arduino('/com5')




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(266, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LedYak = QtWidgets.QPushButton(self.centralwidget)
        self.LedYak.setGeometry(QtCore.QRect(20, 200, 221, 23))
        self.LedYak.setObjectName("LedYak")
        self.LedYak.clicked.connect(self.Yak)

        self.LedSon = QtWidgets.QPushButton(self.centralwidget)
        self.LedSon.setGeometry(QtCore.QRect(20, 240, 221, 23))
        self.LedSon.setObjectName("LedSon")
        self.LedSon.clicked.connect(self.Son)
        self.Cap1 = QtWidgets.QLabel(self.centralwidget)
        self.Cap1.setGeometry(QtCore.QRect(10, 70, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Cap1.setFont(font)
        self.Cap1.setObjectName("Cap1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 266, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LedYak.setText(_translate("MainWindow", "Led Yak!"))
        self.LedSon.setText(_translate("MainWindow", "Led Söndür !"))
        self.Cap1.setText(_translate("MainWindow", "PyQt5 Arduino PyFirmata"))

 
    def Yak(self,LedYak):
     board.digital[5].write(1)
    def Son(self,LedSon):
     board.digital[5].write(0)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
