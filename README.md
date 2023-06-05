# PingPongBallLevitationPID
**Mason Divers and Cooper Moreland**

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
![Bodacious Tumelo-Bojo](https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/91158978/3eb6dd60-e7e1-40dc-8f2d-3f4bf1d5fea4)
![image](https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/91158978/62602e15-0bd6-4507-af8b-58f0fe3ef9b8)

## Code

```python

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
```

## CAD Renderings

![bob](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102213.png?raw=true)

Rendering of the Top and Side

![ted](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102254.png?raw=true)

Rendering of View from Below

![fred](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102329.png?raw=true)

Rendering of the Inside

## Images

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/71406906/a2da06b4-ad93-430d-8ef8-54d1295656db" alt="IMG_0847" width="400"/>

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/71406906/d8ac62ba-55c6-4ca4-a83c-ebed8fd0dd28" alt="IMG_0848" width="400"/>

<img src="https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/91158978/14a965af-2338-4a59-a945-40406d98cf5e" alt="IMG_2357" width="400"/>

## Video 

https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/71406906/f33dda7f-ae85-43b1-a4ff-a210ebcc4e39

## Obstacles/Errors

Original Box Design: We originally built a generic box, but once we decided to use a certain design for our 3d printed fan we had to redesign the box around the fans design so it could blow air directly out of the box without losing power to blowing some ar into walls.

Redesigning the Fan: Our initial fan design did not generate enough airflow to levitate the ping pong ball effectively. We asked Mr. Dierolf for help on the design with the fan and redesigned it so it was a more stable and power capable fan.

Shortening the Tube: We used vinyl for the tube so we could later cut it down if we needed to resize which turned out to be useful later when we needed to make it shorter ad also overlap less when we wrapped it.

Tuning PID Parameters: It took a while to find the separate values for P, I, and D in the code so we could levitate the ping pong ball without too much oscillation and keep it at the same height the whole time.

Sensor Interference: We encountered challenges with sensor interference during testing. The ultrasonic sensor occasionally picked up echoes or reflections from nearby objects, leading to inaccurate distance measurements. To mitigate this issue, we had to adjust the sensor positioning and implement filtering techniques to minimize interference and improve the reliability of the distance readings.

Runtime Errors: We ran into a lot of runtime errors while trying to finalize the code. What helped was starting the code simple by only making sure the dc motor worked, then later implementing PID and the ultrasonic sensor with the help of Mr. Dierolf.

Time Constraints: Time management was an ongoing challenge throughout the project. Balancing multiple tasks, such as CAD design, fabrication, programming, and testing, within the project timeline required effective planning and prioritization. Adapting to unforeseen obstacles and errors within the limited timeframe demanded flexibility and efficient resource allocation.

## Tips

This is a [Helpful video](https://www.youtube.com/watch?v=k0yTh2D-ypQ&list=PLWiHR1caPdEORSQOIG1W4TmaKShuoKJA5&index=3&t=65s) and a good reference for what our project is. -0.06 is a good allowance number for friction fit because we had to sand down edges with it at -0.08. CAD for this type of project is important to get done early because it's needed to test the code.

## Reflection 

This project helped us learn how to use PID in designs which was a previously unexplored piece of engineering and proved a challenge for us on the coding side of things. ALthough the code is short it took a while to fully optimize the code and have it working with no issues or runtime errors. Our wiring was originally a "rat's nest" so we had to redo it with shorter wires for a cleaner and more readable look to the project. We used electrical tape on the wires going to the top so it looked like one uniform wire instead of 4 separate wires tying knots with eachother going to the ultrasonic sensor. The finalized look for the wires was much cleaner and could be used to look back at the project and actually see which wire goes where. 
