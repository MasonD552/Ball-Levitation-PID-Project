# PingPongBallLevitationPID
**[Mason Divers](https://github.com/MasonD552) and [Cooper Moreland](https://github.com/Cooper-Moreland)**

## [Planning Document](https://docs.google.com/document/d/1iu1QzHzOoS6wglSrSRKpMj5YYZf-tlPRr4fQlHbtSWw/edit?usp=sharing)

## [Onshape Document](https://cvilleschools.onshape.com/documents/01ba54e9a02a0264ffe30b36/w/751f0ee8c634455b7b734eb5/e/1af5956fe3e64c1f0f977208?renderMode=0&uiState=643e998d3ae6405c35686462)

## Materials Used

- Acrylic
- Panel Mount LED
- HC-SR04 Ultrasonic Sensor
- Panel Mount Switch
- Metro M4 Express AirLift
- 6xAA Battery Pack w/ Batteries
- TIP120 Transistor

## Overview

The goal was to design, build, and program a device that uses PID feedback control. We did a PID-controlled ping pong ball floater using a self-made 3d-printed fan to levitate the ball to a set point ad stay there using an ultrasonic sensor as the input and the 3d printed fan as the output. 

## Wiring Diagram

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/91158978/4c23f570-8741-4c18-bbee-7d778997aa82" alt="Screenshot 2023-06-05 105221" width="900"/>

Final wiring diagram made in TinkerCAD.

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/tip120-motor.png?raw=true" alt="tip120-motor" width="700"/>

This is the wiring diagram we used to help us wire the TIP 120 transistor.

## Code

```python
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
```


## CAD Renderings

![bob](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102213.png?raw=true)

Rendering of the Top and Side

![ted](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102254.png?raw=true)

Rendering of View from Below

![fred](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102329.png?raw=true)

Rendering of the Inside

## Images

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/IMG_0873.jpg?raw=true" alt="IMG_0873" width="400"/>

photo of the back/side

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/IMG_0872.jpg?raw=true" alt="IMG_0872" width="400"/>

photo of the front

## Video 

![video](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/pid%20ping%20pong%20ball%20floater.gif?raw=true)

working ping-pong ball floater video

## Obstacles/Errors

Original Box Design: We originally built a generic box, but once we decided to use a certain design for our 3d-printed fan we had to redesign the box around the fan's design so it could blow air directly out of the box without losing power to blowing some air into walls.

Redesigning the Fan: Our initial fan design did not generate enough airflow to levitate the ping pong ball effectively. We asked Mr. Dierolf for help on the design of the fan and redesigned it so it was a more stable and power-capable fan.

Shortening the Tube: We used vinyl for the tube so we could later cut it down if we needed to resize which turned out to be useful later when we needed to make it shorter ad also overlap less when we wrapped it.

Tuning PID Parameters: It took a while to find the separate values for P, I, and D in the code so we could levitate the ping pong ball without too much oscillation and keep it at the same height the whole time.

Sensor Interference: We encountered challenges with sensor interference during testing. The ultrasonic sensor occasionally picked up echoes or reflections from nearby objects, leading to inaccurate distance measurements. To mitigate this issue, we had to adjust the sensor positioning and implement filtering techniques to minimize interference and improve the reliability of the distance readings.

Runtime Errors: We ran into a lot of runtime errors while trying to finalize the code. What helped was starting the code simply by only making sure the dc motor worked, then later implementing PID and the ultrasonic sensor with the help of Mr. Dierolf.

Time Constraints: Time management was an ongoing challenge throughout the project. Balancing multiple tasks, such as CAD design, fabrication, programming, and testing, within the project timeline required effective planning and prioritization. Adapting to unforeseen obstacles and errors within the limited timeframe demanded flexibility and efficient resource allocation.

## Tips

- Utilize this informative [video](https://www.youtube.com/watch?v=k0yTh2D-ypQ&list=PLWiHR1caPdEORSQOIG1W4TmaKShuoKJA5&index=3&t=65s) as a valuable reference for our project.
+ -0.06 is a good allowance number for friction fit because we had to sand down edges of our side to make it friction fit.
* Prioritize completing the CAD work early on for this project, as it is crucial for code testing purposes.

## Reflection 

This project provided us with valuable insights into implementing PID in our designs, which was a previously unexplored aspect of engineering. It presented us with coding challenges that required considerable effort to optimize and eliminate any runtime errors. Our initial wiring setup was quite chaotic, resembling a "rat's nest," so we decided to redo it using shorter wires to achieve a cleaner and more organized appearance. To enhance the aesthetics and readability of the project, we used electrical tape to create the illusion of a single, unified wire instead of multiple wires tangled together, particularly for the connections leading to the ultrasonic sensor. The finalized wiring configuration greatly improved the project's visual clarity and enabled easy identification of each wire's purpose. Additionally, we needed to adjust the outer shell of the fan. Instead of reprinting it using a 3D printer, we opted for laser cutting a 3.18mm thick shell, which was slightly wider on the inside. This modification allowed for a more precise fit and addressed the sizing issue effectively. In conclusion, this project not only enhanced our understanding of PID but also highlighted the significance of cable management and maintaining cleanliness in design implementations.
