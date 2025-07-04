from dataclasses import dataclass

# Region Of Interest:
#
#  x1,y1----------------
#  |                    |
#  |                    |
#  |                    |
#  -------------------x2,y2   

@dataclass
class ROI:
    """Recive two points from the frame  to extract the Region Of Interest"""

    x1: int; y1: int
    x2: int; y2: int


# Motor PINS
IN_3 = 12
IN_4 = 11
ENB = 10 # ENABLE
# Servo PINS and VALUES
SERVO_PIN = 9

RIGHT = 0
LEFT = 180

CENTER = 84


# LEDS PINS
LED_YELLOW = 7
LED_RED = 6
LED_WHITE = 5
LED_GREEN = 4

# Buton pin
BUTTON = 3
# Arduino pins
PINS = {
        "LED": [LED_YELLOW, LED_RED, LED_WHITE, LED_GREEN],
        "BUZZER": None, 
        "SERVO": SERVO_PIN,
        "MOTOR_EN": ENB,
        "MOTOR_IN3": IN_3,
        "MOTOR_IN4": IN_4,
        "BUTTON": BUTTON
}

RED_TARGET = 110 
GREEN_TARGET = 530


# Open Challenge regions
#OPEN_ROI_LEFT = ROI(0, 0, 60, 479)
#OPEN_ROI_RIGHT = ROI(1280 - 100, 0, 1280, 720)
CENTER_X = int(640 / 2)
CENTER_Y = int(480 / 2) + 30
OPEN_ROI_CENTER = ROI(CENTER_X - 120,CENTER_Y - 14,CENTER_X + 120,450)
ROI_LINES = ROI(200, 370, 440, 470)

# CLosed challenge regions

CLOSED_LEFT_ROI = ROI(0, CENTER_Y - 30, int(640 / 3), 480)

CLOSED_RIGHT_ROI = ROI(640 - int(640 / 3), CENTER_Y - 30, 640, 480)

CLOSED_CENTER_ROI = ROI(int(640 / 3), CENTER_Y - 30, 640 - int(640 / 3), 480)

CLOSED_GENERAL_ROI = ROI(0, CENTER_Y - 30, 640, 480)

TURN_THRESH = 30000.0
TURN_EXIT_THRESH = 10400.0






# Color masks for detecting obstacles
# The colorspace used is HSV
# H: Hue (From 0 to 180)
# S: Saturation
# V: Value

'''
              #lower range        # upper range
mask_red    = [ [160, 120, 40], [180, 255, 255]]
mask_green  = [  [40, 120, 40], [80, 255, 255] ]
mask_black =  [ [0, 0, 0], [180, 255, 75] ]
mask_orange = [ [30, 120, 40],     [30, 255, 255]]
mask_blue   = [ [30,120,40],         [30,255,255]]

'''

# Color masks in LAB colorspace


mask_red = [[0, 153, 140], [ 131,198, 171]]
mask_green = [[0, 45, 0], [255, 117, 153]]

mask_blue = [[54, 124, 25], [148, 164, 121]]
#mask_blue_test = [[14, 135, 71], [174, 203, 240]]
mask_blue_test = [[0, 61, 17], [114, 170, 126]]


mask_orange = [[0, 163, 163], [255, 191, 204]]
mask_orange_test = [[35, 135, 86], [175, 160, 177]]

mask_black = [[0, 109, 113], [59, 137, 150]]
#mask_black_test = [[2, 100, 69], [79, 168, 141]]
#mask_black_test = [[0, 58, 98], [120, 142, 126]]
#mask_black_test = [[0, 57, 93], [123, 140, 134]]

#casa jesus luz morada
mask_black_test = [[0, 58, 17], [108, 169, 137]]

# mascara de maremare 
#naranja [[70, 135, 86], [175, 160, 177]]
#mask_blue_test = [[41, 58, 12], [141, 163, 121]]
#mask_black_test = [[19, 50, 22], [129, 142, 142]]










