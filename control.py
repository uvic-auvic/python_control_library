import sys
import re
import GateDetector
import serial as s
import time

class controls: 
    def __init__(self, com_port):
        self.pressure = 0 
        self. pressure_diff = 100
        self.ser = s.Serial(com_port, 9600, timeout = 2)

    def activate_motor(self, motor_number, power):
        if power > 0:
            ser.write(b'M{0}F{1}'.format(str(motor_number), str(power)))
        elif power < 0:
            ser.write(b'M{0}R{1}'.format(str(motor_number), str(-1*power)))
        elif power == 0:
            ser.write(b'M{0}0'.format(str(motor_number)))

    def move_forwards(self, power):
        # turn both x motors on
        self.activate_motor(6, power)
        self.activate_motor(4, power)

    def descend(self, power):
        self.activate_motor(1, power)
        self.activate_motor(7, power)
        self.activate_motor(8, power)
        self.activate_motor(3, power)

    def rotate(self, power):
        self.activate(2, power)
        self.activate(5, -1*power) 

    def stop_all(self):
        ser.write(b'STP')
        
