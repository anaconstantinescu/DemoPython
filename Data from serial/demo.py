import sys
from PyQt4 import QtGui, QtCore
import serial.tools.list_ports
import pyqtgraph as pg
import serial




class Demo(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.initUI()

#   Define timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)

#   Event listener
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.stopBtn.clicked.connect(self.stopBtnClicked)
        
        pg.QtGui.QApplication.instance().exec_()
        
    def initUI(self):
  
#   Define elements      
        self.startBtn = QtGui.QPushButton('Start')
        self.stopBtn = QtGui.QPushButton('Stop')

#   Define Layout
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.startBtn, 0, 0)
        self.grid.addWidget(self.stopBtn, 0, 1)
        
#        self.stopBtn.setMaximumWidth(int(width))
#        self.startBtn.setMaximumWidth(int(width))\
        self.setLayout(self.grid)
        self.show()

    def startBtnClicked(self):

#   Find port
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "Arduino Micro" in port[1] or "USB" in port[1]:
                self.port = port[0]
                self.ser = serial.Serial(self.port, 9600, timeout=1)

        
        self.timer.start(0)

    def stopBtnClicked(self):
        self.ser.close()
        self.timer.stop()


    def update(self):
        if(self.repLbl.text() == self.turaLbl.text()):
            return self.stopBtnClicked()
        try:
            var = self.ser.readline()
            var = var.split()
        except:
            pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Demo()
