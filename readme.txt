In order to use dynSerialConnection.py:

In the main file you can control the identification, theta (angle in radians), thetaDot (velocity) and torque.  
These can be set to move individually each time, if a loop is desired then the following must be done:

1) Open a new python file
2) In the new file type:

#! /usr/bin/env python

from dynSerialConnection import dynSerialConnection

3) The above will give you the class that you can loop the data through.  

output = dynSerialConnection(theta,thetaDot,torque,id)

4) The value returned "output" (above) has the values of radian , velocity , torque that can be used in feedback control

output = dynSerialConnection(theta,thetaDot,torque,id)

newPosition = output.radian
newVelocity = output.velocity
newTorque = output.torque

5) You can also get data out by loading the ach simulator and looking for the process "dynProcess"
