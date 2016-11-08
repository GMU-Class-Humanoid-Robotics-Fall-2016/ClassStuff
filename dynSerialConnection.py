#! /usr/bin/env python

"""




"""

import numpy as np
import serial
import time
import sys
import struct
import array
from dynFunctions import *


class dynSerialConnection(object):

    def __init__(self , theta , thetaDot , torque , id):

        tick = self._convertToTick(theta)

        setVelocity = hex(thetaDot)

        


    def _openSerial(self,p,b):

        self.ser = serial.Serial(
            port = p ,
            baudrate = b ,
            parity = serial.PARITY_NONE ,
            stopbits = serial.STOPBITS_ONE ,
            bytesize = serial.EIGHTBITS
        )

        self.ser.open()
        connected = self.ser.isOpen()

        if connected == True:
            print 'Device Connected'
        elif connected == False:
            print 'Device Did Not Connect'
            sys.exit(2)



    def _transmitData(self , id , address , parameters , cmd):

        header = [0xff , 0xff]
        # id = [0x01]
        # len = [0x05] # Parameters + 2 ::: goal , low bit , high bit = 3 + 2 = 5
        address = [0x1e] # Goal Position

        len = 2. + np.size(parameters) + np.size(cmd)


        checkSum = [~(id[0] + len[0] + cmd[0] + address[0] + goalLow[0] + goalHigh[0]) & 0xff]


    def _readData(self , id ):

        cmd = [0x02]

