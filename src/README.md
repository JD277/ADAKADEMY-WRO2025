# Software documentation

This section provides an overview of the software architecture  used in our autonomous vehicle for the WRO 2025 Futuros Ingenieros  competition. It includes:

* The programming languages and tools used

* A high-level description of the system's modules

* How the robot processes sensor data, makes decisions, and controls hardware

* Integration with vision systems (e.g., line detection, traffic sign recognition)

* Communication between controllers (e.g., Raspberry Pi ↔ Arduino Nano)

# Folders structure 
```
ADAKADEMY-WRO2025/src/
├── modules/
|    ├── board.py
|    ├── vision.py
|    └── halbi.py
├── utils/
|    ├── movement_test.py
|    ├── color_tester.py
|    └── vision_test.py
├── templates/
|   ├── open_challenge_with_seconds.py
|   └── open_challenge_with_seconds2.py
├── constants.py
├── open_challenge.py
└── obstacle_challenge.py
```
Where:

- `modules/board.py`: This is ArduinoController class manages Arduino hardware (LEDs, buzzers, servos, and motors via a L298N driver) using pyfirmata2.

- `modules/vision.py`: To Capture and process images to detect colored objects within a region of interest (ROI) using a Raspberry Pi camera.

- `modules/halbi.py`: Is the main class compossed by the other to that is used to program both challenges, this class is configured to be easy to program your car without worrying about complex stuff. 

- `utils/movement_test.py`: Is an implementation with pygame that allows you to control the car like an FPV car to test everything related with the movement.


- `utils/color_tester.py`: Is an opencv code to calibrate the mask that will be detected. This file was recover from [ASPARAGUS team](https://github.com/kylln20/WRO_FE_2023-24/blob/main/src/ColourTesterLAB.py) which has the fifth place on the international of 2024

- `utils/vision_test.py`: Is used to see how the masks are working and finish the calibration process 


- `templates/`: Are two file where is a rules based codes to complete the first challenge that we used to create the final code

- `constants.py`: Are all the values that don't change like arduino pins, indicators leds

- `open_challenge.py`: is the final code for the first challenge.

- `obstacle_challenge.py`: is the final code for the second challenge.



## Table of contents

* New code vs Past code

* Code description 

* Calibration

* Open challenge
    * Strategy
    * Flowchart
    * Explanation
    * Recomendations

* Obstacle challenge
    * Strategy
    * Flowchart
    * Explanation
    * Recomendations
