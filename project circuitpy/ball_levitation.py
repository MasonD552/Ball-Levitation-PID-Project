# Mason Divers, Cooper Moreland
# PID Controlled Ping Ping Levitator
# Levitate a ping pong ball in a tube at a consistent height using an ultrasonic sensor, fan, and pid

import board
import adafruit_hcsr04
from PID_CPY import PID  
import pwmio   
import time # imports

pid = PID(24000,5,8500) # p, i, and d values for tuning
pid.setpoint = 12.5 # where to keep the ping pong ball floating
pid.output_limits = (20000.00,50000.00) # p, i, and d highest possible values

fanMotor = pwmio.PWMOut(board.D8,duty_cycle = 65535) # fanfanMotor
fanMotor.duty_cycle = 0

dist = adafruit_hcsr04.HCSR04(trigger_pin = board.D3, echo_pin = board.D2)

while True:
    try:
        height = 26 - dist.distance # distance of ultrasonic sensor from bottom
        speed = int(pid(height))
        fanMotor.duty_cycle = speed
        print("speed ", speed, " height ", height,)
    except RuntimeError:
        print("retry")
    time.sleep(.1)
    