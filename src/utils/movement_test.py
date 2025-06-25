
import pygame
import src.modules.halbi
from src.modules.vision import *
import sys
import cv2 as cv
from src.constants import *

pygame.init()
pygame.display.init()
 
turn_left = pygame.K_a
turn_right = pygame.K_d

go_forward = pygame.K_w
go_backward = pygame.K_s

ROI_LEFT = ROI(20, 110, 260, 240)
ROI_RIGHT = ROI(260, 110, 600, 240)
pygame.display.set_mode((640, 480))




#display = pygame.display.set_mode((300, 300))


hal = halbi.HALBI("/dev/ttyUSB0",0)

hal.setup_HALBI(PINS)


while True:
    hal.vision.receive_image()
    
    
    #hal.Vision.receive_image()
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[go_forward]:
        hal.go_forward()

    elif keys[go_backward]:
        hal.go_backward()
        
    else:
        hal.Stop()
        
    if keys[turn_left]:
        hal.turn_left()

    elif keys[turn_right]:
        hal.turn_right()
    
    else:
        
        hal.turn_center()
        
    #frame = hal.Vision.frame
    #cv.rectangle(frame, (ROI_LEFT.x1, ROI_LEFT.y1, ROI_LEFT.x2, ROI_LEFT.y2), (0,0,255), 1)
    
    #cv.imshow("r", frame)
    #if cv.waitKey(1) == ord('q'):
        #break
    