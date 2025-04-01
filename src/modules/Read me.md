# Documentation for modules

##  Folder structure
The JS files are organized with this order:
```
ADAKADEMY-WRO2025/src/modules├── models/
├── text_motors/
│   └── text_motors.ino
├── MovementTest.py
├── board.py
├── constants.py
├── halbi.py
└──vision.py
```
Where:

- `/text_motors`: Code to controls a DC motor via an H-bridge
- `/MovementTest.py`: Controls a robot (HALBI) using keyboard inputs (WASD) for movement (forward, backward, left, right) via Pygame.
- `/board.py`: This ArduinoController class manages Arduino hardware (LEDs, buzzers, servos, and motors via a DRV8833 driver) using pyfirmata2.
- `/constants.py`: Defines Arduino pins for motor/servo control and camera resolution 
- `/halbi.py`: 
- `/vision.py`: To Capture and process images to detect colored objects within a region of interest (ROI) using a Raspberry Pi camera.

## Table of contents

1. [Text_motors](#text_motors)
    - [text_motors.ino](#text_motors.ino)
2. [MovementTest.py](#MovementTest.py)
3. [board.py](#board.py)
4. [constants.py](#constants.py)
5. [halbi.py](#halbi.py)
6. [vision.py](#vision.py)
