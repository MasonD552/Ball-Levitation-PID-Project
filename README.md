# PingPongBallLevitationPID
**Mason Divers and Cooper Moreland**

## [Planning Document](https://docs.google.com/document/d/1iu1QzHzOoS6wglSrSRKpMj5YYZf-tlPRr4fQlHbtSWw/edit?usp=sharing)

## [Onshape Document](https://cvilleschools.onshape.com/documents/01ba54e9a02a0264ffe30b36/w/751f0ee8c634455b7b734eb5/e/1af5956fe3e64c1f0f977208?renderMode=0&uiState=643e998d3ae6405c35686462)

## Overview

The goal was to design, build, and program a device that uses PID feedback control. We did a PID-controlled ping pong ball floater using a self-made 3d-printed fan to levitate the ball to a set point ad stay there using an ultrasonic sensor as the input and the 3d printed fan as the output. 

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

## Obstacles/Errors
Throughout the PingPongBallLevitationPID project, we encountered several obstacles and errors that required us to adapt and make adjustments. These challenges tested our problem-solving abilities and pushed us to find innovative solutions. Here are some of the obstacles and errors we faced:

Original Box Design: Initially, we created an original box design for the ping pong ball levitation chamber. However, during testing, we realized that the box was not providing sufficient stability and containment for the ball. This forced us to go back to the drawing board and redesign the entire box to ensure a secure and stable levitation environment.

Redesigning the Fan: Our initial fan design did not generate enough airflow to levitate the ping pong ball effectively. We discovered that the fan blades were not optimized for the required air circulation. As a result, we had to revisit the fan design, modify the blade shape and pitch, and experiment with different configurations to achieve the desired airflow and levitation capabilities.

Shortening the Tube: The length of the tube connecting the levitation chamber and the fan also posed a challenge. Initially, the tube was longer than necessary, resulting in a delay in airflow response and stability issues. To address this, we decided to shorten the tube to minimize air resistance and improve the responsiveness of the system.

Tuning PID Parameters: Implementing PID control required us to tune the P, I, and D parameters to achieve optimal performance. However, finding the right balance proved to be a complex task. Initially, the system exhibited overshoot, instability, or sluggish response. It took several iterations and experiments to fine-tune the PID values and achieve the desired ball levitation and stability.

Sensor Interference: We encountered challenges with sensor interference during testing. The ultrasonic sensor occasionally picked up echoes or reflections from nearby objects, leading to inaccurate distance measurements. To mitigate this issue, we had to adjust the sensor positioning and implement filtering techniques to minimize interference and improve the reliability of the distance readings.

Runtime Errors: During the programming phase, we faced runtime errors and exceptions that affected the overall functionality of the device. These errors required careful debugging and troubleshooting to identify and resolve the underlying issues. It was crucial to thoroughly test the code, handle potential exceptions, and ensure the smooth operation of the system.

Time Constraints: Time management was an ongoing challenge throughout the project. Balancing multiple tasks, such as CAD design, fabrication, programming, and testing, within the project timeline required effective planning and prioritization. Adapting to unforeseen obstacles and errors within the limited timeframe demanded flexibility and efficient resource allocation.

Despite these obstacles and errors, we approached them with determination and a willingness to learn from our mistakes. Each challenge provided valuable insights and lessons that ultimately contributed to the success of the Ping Pong Ball Levitation project. Through perseverance and collaborative problem-solving, we were able to overcome these hurdles and achieve a functional and stable ping pong ball levitation system.
## Tips

This is a [Helpful video](https://www.youtube.com/watch?v=k0yTh2D-ypQ&list=PLWiHR1caPdEORSQOIG1W4TmaKShuoKJA5&index=3&t=65s) and a good reference for what our project is. -0.06 is a good allowance number for friction fit because we had to sand down edges with it at -0.08. CAD for this type of project is important to get done early because it's needed to test the code.

## Reflection 
During the time of this PID project we were trying to solve a problem of , and programming a device to achieve stable ball levitation using PID feedback control. It was an exciting challenge that allowed us to explore the realms of 3D printing, electronics, and control systems.
The project started with meticulous planning, where we defined our objectives and outlined the necessary steps. We dove into CAD design, crafting detailed renderings that brought our vision to life. The Onshape document became our creative hub, housing all the CAD models, technical drawings, and assembly instructions.
As we ventured into the construction phase, we encountered both expected and unexpected obstacles. Through perseverance and problem-solving, we tackled each challenge head-on, learning valuable lessons along the way. The materials we used, such as acrylic, the ultrasonic sensor, and the 3D-printed fan, played crucial roles in bringing our device to fruition.
Programming the PID control system was a thrilling endeavor. We carefully fine-tuned the PID parameters to achieve the desired set point and maintain ball levitation. Our code, neatly organized and commented, served as the backbone of the project, connecting all the hardware components and facilitating precise control.
Looking back, this project taught us the importance of collaboration and interdisciplinary skills. From designing elegant CAD models to troubleshooting hardware and software issues, we developed a holistic understanding of the project's intricacies. We also learned the value of documentation, capturing our progress, obstacles, and triumphs through images and reflection.
The ping pong ball levitation project pushed our boundaries and fueled our curiosity. It was a testament to our creativity, technical prowess, and dedication. As we witnessed the ball floating effortlessly, we felt a sense of accomplishment and pride. This project will forever hold a special place in our hearts as a symbol of innovation and perseverance.
In conclusion, the ping pong ball levitation project allowed us to merge our passions for engineering, design, and problem-solving. It challenged us to think critically, collaborate effectively, and embrace the iterative nature of engineering. It was an incredible experience that not only enriched our skills but also fueled our desire to continue exploring the vast possibilities of technology.
