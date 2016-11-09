
import ach
import sys
import time
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel('dynProcess')
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
class THE_I(Structure):
    _pack_ = 1
    _fields_ = [("id"    , c_int16),
                ("velocity"   , c_double),
                ("position" , c_double),
                ("torque" , c_double)]

processData = THE_I()

while(True):
    [statuss, framesizes] = s.get(processData, wait=False, last=True)
    print processData.id , processData.velocity , processData.position , processData.torque