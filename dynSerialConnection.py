#! /usr/bin/env python

"""




"""

import numpy as np
import serial
import time
import sys
import struct
import array
import dynFunctions as dyn


class dynSerialConnection(object):

    def __init__(self , theta , thetaDot , torque , id):

        p = '/dev/ttyUSB0'
        b = 1000000

        id = dyn._convertToSingleByte(id)
        tickLow , tickHigh = dyn._convertToLowHighByte(dyn._convertToTick(theta))
        address = [0x1e]

        velLow , velHigh = dyn._convertToLowHighByte(thetaDot)

        torqueLow , torqueHigh = dyn._convertToLowHighByte(torque)

        params = tickLow + tickHigh + velLow + velHigh + torqueLow + torqueHigh

        self._openSerial(p,b)


        self._transmitData(id , address , params , [0x03])
        time.sleep(1)
        curData , curDataInt = self._readData(id, [0x02])

        rad = dyn._convertToRadian(dyn._convertLowHighByteToInteger(curDataInt[5],curDataInt[6]))
        vel = dyn._convertLowHighByteToInteger(curDataInt[7],curDataInt[8])
        torque = dyn._convertLowHighByteToInteger(curDataInt[9],curDataInt[10])

        print rad , vel , torque


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

        address = [0x1e] # Goal Position

        len = dyn._convertToSingleByte(2. + np.size(parameters) + np.size(cmd))

        checkSum = dyn._getChecksum(id,len,cmd,address,parameters)

        # print checkSum

        # checkSumLow , checkSumHigh = dyn._convertToLowHighByte(dyn._getChecksum(id,len,cmd,address,parameters))

        output = header + id + len + cmd + address + parameters + checkSum



        outputFinal = bytearray(output)


        self.ser.write(outputFinal)
        self.ser.read(6)

    def _readData(self , id , cmd ):

        header = [0xff,0xff]
        len = [0x04]
        goal = [0x06]
        address = [0x24]
        checkSum = dyn._getChecksum(id,len,cmd,address,goal)

        output = header + id + len + cmd + address + goal + checkSum

        outputFinal = bytearray(output)

        self.ser.write(outputFinal)

        curData = bytearray(12)
        curDataInt = np.zeros([12,1],dtype=int)

        for i in range(12):
            curData[i] = self.ser.read(1)
            curDataInt[i] = int(curData[i])

        print curDataInt

        return curData , curDataInt

if __name__ == "__main__":

    id = 1
    theta = +np.pi/4
    thetaDot = 500
    torque = 500




    dynSerialConnection(theta,thetaDot,torque,id)