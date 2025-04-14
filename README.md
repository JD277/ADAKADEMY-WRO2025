## Content

* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members).
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom).
* `video` contains the video.md file with the link to a video where the driving demonstration exists.
* `schemes` contains one or several schematic diagrams in the form of JPEG, PNG, or PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains the code of control software for all components that were programmed to participate in the competition.
* `models` is for the files for models used by 3D printers, laser cutting machines, and CNC machines to produce the vehicle elements. If there is nothing to add to this location, the directory can be removed.
* `other` is for other files which can be used to understand how to prepare the vehicle for the competition. It may include documentation on how to connect to an SBC/SBM and upload files there, datasets, hardware specifications, communication protocols descriptions, etc. If there is nothing to add to this location, the directory can be removed.


## Intro

This is the official Github repository for The Adakademy Team, before known as Adagroup, conformed by Jesser Palma, Jesús Alcalá and Hector Cartagena. This repository contains all the code, documentation, and resources for our project, HALBI. This is our third year participating in WRO


## First Design

At first, we planned to design the car from scratch, modeling and printing our own 3D pieces, including the chassis and direction, Although it seemed like a good idea at first, as we progressed we started to face problem after problem, we realized that our current design would give us more problems, at the end we tried our best with the time constraints we had, and this was the vehicle we presented at WRO 2024, Cybercooper.

![cybercooper](https://github.com/user-attachments/assets/188943c0-d6d6-4796-bf28-c8c82174c24e)


## Current Design

### Prototype

Given the resources we currently had, our main idea was to re-design Cybercooper, modifying the existing base, strategy and using better electronic components; we started printing the new parts with white material and thinking of better ways to assemble the car direction.
![cooper white prototype](https://github.com/user-attachments/assets/8885f4cd-e4e0-4fe3-9b6e-9026baf66653)


### Fischertechnik kit

At the end, we decided to use a premade base for the chassis, the main reason for this was to save time ( and headaches) with the mechanical design, giving us more time to focus on the electronics and programming.
![fischertechnik master kit car](https://github.com/user-attachments/assets/1b3b9a5c-0a64-4d31-8718-00e75f88f6c2)


## Car Photos


## Mobility

### Chassis

## Electronics

### Raspberry

### Camera

### Microcontroller

## Schematics



## Software

We developed the software using python3 as our main programming language and using Thonny/Terminal as code editor.

#### Unifying Code

We wanted to keep the code as simple as possible and use a single language, in order to make this possible we used a library called Pyfirmata which enables us to merge the microcontroller code and the raspberry code in a single unit.


### Open Challenge

#### Image Processing

#### Steering Control

### Closed Challenge

#### Obstacle detection
