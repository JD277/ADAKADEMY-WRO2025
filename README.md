## Intro

This is the official Github repository for The Adakademy Team, before known as Adagroup, conformed by Jesser Palma, Jesús Alcalá and Hector Cartagena. This repository contains all the code, documentation, and resources for our project, HALBI. This is our third year participating in WRO

# 📖 Content of README 📖
* **[Hardware](#-hardware-)**
  * [Components](#%EF%B8%8F-components-%EF%B8%8F)
  * [Mobility Management](#-mobility-management-)
    * [Chassis](#chassis)
    * [Design](#design)
    * [Motors](#motors)
  * [Power and Sense Management](#-power-and-sense-management-)
    * [Power and Wiring](#power-and-wiring)
    * [Sensors](#sensors)
    * [Schematic](#schematic)
* **[Software](#-software-)**
  * [Initialization and Connection Process](#-initialization-and-connection-process-)
  * [Object Management](#object-management)
    *  [Object Detection](#object-detection--open-challenge--obstacle-challenge-)
    *  [Wall Detection/Management](#wall-detectionmanagement--open-challenge--obstacle-challenge-)
    *  [Signal Pillar Detection/Management](#signal-pillar-detectionmanagement--obstacle-challenge-)
    *  [Turning (Open Challenge)](#turning--open-challenge-)
    *  [Turning (Obstacle Challenge)](#turning--obstacle-challenge-)
    *  [Parking Lot Detection/Management](#parking-lot-detectionmanagement--obstacle-challenge-)
    *  [Three-Point Turn](#three-point-turn--obstacle-challenge-)
    *  [Backing Up](#backing-up--obstacle-challenge-)
    *  [Potential Improvement: Stuck Detection](#potential-improvement-stuck-detection--open-challenge--obstacle-challenge-)
* **[Assembly Instructions](#-complete-assembly-instructions-)**
# Hardware
### First Design

At first, we planned to design the car from scratch, modeling and printing our own 3D pieces, including the chassis and direction, Although it seemed like a good idea at first, as we progressed we started to face problem after problem, we realized that our current design would give us more problems, at the end we tried our best with the time constraints we had, and this was the vehicle we presented at WRO 2024, Cybercooper.

![cybercooper](v-photos/old_right.jpg)

### Current Design

#### Prototype

Given the resources we currently had, our main idea was to re-design Cybercooper, modifying the existing base, strategy and using better electronic components; we started printing the new parts with white material and thinking of better ways to assemble the car direction.

#### Fischertechnik kit

At the end, we decided to use a premade base for the chassis, the main reason for this was to save time ( and headaches) with the mechanical design, giving us more time to focus on the electronics and programming.

## Car Photos



# Hardware

## Components


## Mobility

Our vehicle is made the Ackermann steering mechanism, which is a geometric configuration used in vehicle steering systems to ensure that when turning, the inner and outer wheels travel along different radii, preventing tire scrubbing and maximizing cornering stability. This is achieved by steering the front wheels at different angles, with the inner wheel turning at a greater angle than the outer whee

## Power and Sense Management

# Software

We developed the software using python3 as our main programming language and using Thonny/Terminal as code editor.

We wanted to keep the code as simple as possible and use a single language, in order to make this possible we used a library called Pyfirmata which enables us to merge the microcontroller code and the raspberry code in a single unit. 

#### Image Processing

We use the raspberry camera to capture the image, which is converted from BGR format to LAB `(lightness, green-red, blue-yellow)`. We use this colorspace because it's easier to detect the colors, regardless of the environment lighting.

We then use OpenCV to apply a threshold to the image, which returns a mask image with the pixels that reside within the specified color range, we can also reduce processing time by only searching within a specific region of interest on the screen.


###Obstacle Detection

For Obstacle detection, we specify various color ranges that coincide with the color of the obstacles, red and green. After the camera captures the image, we apply gaussian blur and median filters to get a sharper image, the program then applies thresholds to get masks with the colors we are interested in, with this mask we can detected the screen position of the obstacles and the contours of the circuit wall, which can be used to decide the turning direction of the car based on a proportional derivative (PD) algorithm, which involves calculating the differences between the area of the walls

### Open Challenge

#### 

#### Steering Control

### Closed Challenge

#### Obstacle detection
