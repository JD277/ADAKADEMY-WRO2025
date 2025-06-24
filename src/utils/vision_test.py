import halbi
from constants import *
from vision import *
import cv2 as cv

hal = halbi.HALBI("/dev/ttyUSB0", 640, 480)

hal.setup_HALBI()

left_roi = ROI(0,100, 300, 300)

running = True

while running:
    
    hal.Vision.receive_image()
    
    red_contours = hal.Vision.find_contours(mask_red, left_roi)
    
    red_contours_info = hal.Vision.max_contour(red_contours, left_roi)
    
    #if red_contours_info.area > 50:
    #    hal.turn_left()
    #else:
    #    hal.turn_center()
    
        
    cv.rectangle(hal.Vision.frame, (left_roi.x1, left_roi.y1, left_roi.x2, left_roi.y2), (0,255,0), 1)
    cv.imshow("frame", hal.Vision.image_hsv)
    
    
    
    
    
    