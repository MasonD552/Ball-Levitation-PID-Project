# Mason Divers, Cooper Moreland
# PID Controlled Ping Ping Levitator
# Levitate a ping pong ball in a tube at a consistent height using an ultrasonic sensor, fan, and pid
#optimization of the pid parameters is required for the best results
#optimize pid parameters by changing the setpoint to the desired height and then changing the kp, ki, and kd values until the ball is levitating at the desired height
#the setpoint can be changed to any height between 0 and 26
#the output limits can be changed to any value between 0 and 65535
#the kp, ki, and kd values can be changed to any value between 0 and 65535
#the fan speed can be changed to any value between 0 and 65535

import board 
import adafruit_hcsr04 
from PID_CPY import PID  
import pwmio   
import time 

pid = PID(15000, 1.0, 4750) # PID parameters
pid.setpoint = 15.00     # setpoint
pid.output_limits = (20000.00,50000.00) # output limits

fanMotor = pwmio.PWMOut(board.D8,duty_cycle = 65535) # fanfanMotor
fanMotor.duty_cycle = 0 

dist = adafruit_hcsr04.HCSR04(trigger_pin = board.D3, echo_pin = board.D2) # distance sensor

while True:
    try:
        height = 26 - dist.distance # 26 is how tall the tube is
        speed = int(pid(height))    # pid output
        fanMotor.duty_cycle = speed # fan speed
        print("speed ", speed, " height ", height,)  # print speed and height
    except RuntimeError: 
        print("retry")  # retry if there is an error
    time.sleep(0.1)     # 0.1 second delay