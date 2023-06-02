# PingPongBallLevitationPID

## [Planning Document](https://docs.google.com/document/d/1iu1QzHzOoS6wglSrSRKpMj5YYZf-tlPRr4fQlHbtSWw/edit?usp=sharing)

## [Onshape Document](https://cvilleschools.onshape.com/documents/01ba54e9a02a0264ffe30b36/w/751f0ee8c634455b7b734eb5/e/1af5956fe3e64c1f0f977208?renderMode=0&uiState=643e998d3ae6405c35686462)

## Overview

The goal was to design, build, and program a device that uses PID feedback control. We did a PID controlled ping pong ball floater using a self made 3d printed fan to levitate the ball to a set point ad stay there using an ultrasonic sensor as te input and the 3d printed fan as the output. 

## CAD Renderings

![bob](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102213.png?raw=true)

Rendering of the Top and Side

![ted](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102254.png?raw=true)

Rendering of View from Below

![fred](https://github.com/MasonD552/Ball-Levitation-PID-Project/blob/CircuitPy/Screenshot%202023-05-30%20102329.png?raw=true)

Rendering of the Inside

## Images

## [Video](https://youtube.com/shorts/0u8GYpTUjR4?feature=share)

## Materials Used

- Acrylic
- Panel Mount LED
- HC-SR04 Ultrasonic Sensor
- Panel Mount Switch
- Metro M4 Express AirLift
- 6xAA Battery Pack w/ Batteries
- TIP120 Transistor

## Wiring Diagram
![Bodacious Tumelo-Bojo](https://github.com/MasonD552/Ball-Levitation-PID-Project/assets/91158978/3eb6dd60-e7e1-40dc-8f2d-3f4bf1d5fea4)

## Code

```python

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
#TIP 120 ask deirolf
```

## Obstacles/Errors

## Tips

This is a [Helpful video](https://www.youtube.com/watch?v=k0yTh2D-ypQ&list=PLWiHR1caPdEORSQOIG1W4TmaKShuoKJA5&index=3&t=65s) and a good reference for what our project is. -0.06 is a good allowance number for friction fit because we had to sand down edges with it at -0.08. CAD for this type of project is important to get done early b/c it's needed to test the code.

## Reflection 
During the course of the PingPongBallLevitationPID project, we embarked on a challenging journey to design, build, and program a device capable of levitating a ping pong ball using PID feedback control. As I reflect on this project, I can't help but acknowledge the valuable lessons learned and the sense of accomplishment we derived from overcoming various obstacles along the way.

One of the major highlights of this project was the utilization of PID feedback control. This concept allowed us to maintain stability and precision in levitating the ping pong ball to a desired set point. Understanding the intricacies of PID control, such as tuning the P, I, and D values, was a significant learning experience. We had to experiment and fine-tune these parameters to achieve the desired outcome. This process taught us the importance of iterative testing and the value of persistence in refining a control system.

The integration of CAD design into the project was another pivotal aspect. Creating detailed 3D models and renderings early on provided us with a visual representation of the device. This allowed us to identify potential design flaws, make necessary modifications, and validate the feasibility of our system before moving forward. The CAD design phase taught us the significance of careful planning and the benefits of addressing potential issues proactively.

The construction phase presented us with its fair share of challenges. From sourcing the required materials to assembling the components, we encountered obstacles that demanded creative problem-solving skills. For example, we had to ensure a friction fit of the ping pong ball within the levitation chamber, which required precision and adjustments to the CAD design. Overcoming these challenges instilled in us a sense of resilience and resourcefulness.

Programming the device was both exciting and demanding. We developed code that integrated the ultrasonic sensor, fan motor, and PID controller. Fine-tuning the PID values to maintain stability and responsiveness was a critical aspect of the programming phase. Through this process, we gained a deeper understanding of control systems and their practical implementation.

Collaboration played a vital role in the success of this project. Working as a team, we leveraged each other's strengths and expertise to overcome obstacles. Effective communication, delegation of tasks, and regular progress updates were instrumental in keeping the project on track. Moreover, we learned the importance of leveraging external resources, such as videos and references, to enhance our understanding and problem-solving capabilities.

In hindsight, I believe this project provided an excellent opportunity for us to apply theoretical concepts to a practical real-world scenario. It taught us the value of interdisciplinary collaboration, attention to detail, and persistence in achieving our goals. Furthermore, it deepened our understanding of control systems, CAD design, and programming.

Moving forward, I am confident that the skills and knowledge gained from this project will serve as a solid foundation for future endeavors. The PingPongBallLevitationPID project has not only enhanced our technical skills but also fostered a spirit of curiosity, innovation, and a desire to continue exploring new challenges. -Cooper and Mason
