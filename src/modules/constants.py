
# Arduino pins
IN_3 = 3
IN_4 = 4
ENB = 5 #ENABLE
SERVO_PIN = 6




CAMERA_X_RESOLUTION = 640
CAMERA_Y_RESOLUTION = 480

# Color masks for detecting obstacles
# The colorspace used is HSV
# H: Hue (From 0 to 180)
# S: Saturation
# V: Value

#Obstacles
              #lower range        #upper range
mask_red    = [ [160, 120, 40], [180, 255, 255]]
mask_green  = [  [40, 120, 40], [80, 255, 255] ]


#Floor lines
mask_orange = [ [30, 120, 40],     [30, 255, 255]]
mask_blue   = [ [30,120,40],         [30,255,255]]
