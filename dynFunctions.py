#! /usr/bin/env python


"""




"""


import numpy as np
import struct

def _convertToRadian(encoder):

    return ((float(encoder) - 512.0) * .29296875) * np.pi / 180.

def _convertToTick(radian):

    return ((180. * radian) / (np.pi * .29296875)) + 512.

def _prepareToTransmit(id,address,params):

    header = [0xff , 0xff]

def _convertToSingleByte(val):

    x = struct.pack('<h',val)
    return np.fromstring(x[0],dtype=np.uint8).tolist()

def _convertToLowHighByte(val):

    low , high = struct.pack('<h',val)

    low = np.fromstring(low,dtype=np.uint8).tolist()
    high = np.fromstring(high,dtype=np.uint8).tolist()

    return low , high

def _getChecksum(id,len,cmd,address,goal):

    cur = id[0] + len[0] + cmd[0] + address[0]

    for i in range(np.size(goal)):
        cur += goal[i]

    return [~(cur) & 0xff]










