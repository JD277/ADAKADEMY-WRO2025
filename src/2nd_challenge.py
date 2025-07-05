from halbi import *
import atexit
import traceback
from constants import *
import time

#start 
hal = HALBI("/dev/ttyUSB0", 1)
hal.setup_HALBI(PINS)



hal.turn_center()

ROIS = [CLOSED_LEFT_ROI, CLOSED_CENTER_ROI, CLOSED_RIGHT_ROI, CLOSED_GENERAL_ROI]

running = False

while hal.Start():
    pass

hal.board.led_on(5)
time.sleep(1)
hal.board.led_off(5)


running = True
loops = 0
line_detected = False
current_obstacle = 0

def draw_obstacle(frame, x,y):
    cv.line(frame, (x,0), (x,480), (0,255,255), 2)

hal.go_backward(255)
time.sleep(1.6)

while running:
    try:
        
        
        
        #get areas and contours-----------------
        hal.vision.receive_image()
        green_cnt = hal.vision.find_contours(mask_green, CLOSED_GENERAL_ROI)
        red_cnt = hal.vision.find_contours(mask_red, CLOSED_GENERAL_ROI)
        
        max_obs_green = hal.vision.max_contour(green_cnt, CLOSED_GENERAL_ROI)
        max_obs_red = hal.vision.max_contour(red_cnt, CLOSED_GENERAL_ROI)
        
        if (max_obs_red[0] > 1):
            if (max_obs_red[1] > SCREEN_LEFTSIDE and max_obs_red[2] > OBSTACLE_TURN_THRESH ):
                print("derecha")
                hal.turn_right()
                
    
        if (max_obs_green[0] > 1):
            if (max_obs_green[1] < SCREEN_RIGHTSIDE and max_obs_green[2] > OBSTACLE_TURN_THRESH):
                hal.turn_left()
                print("izquierda")
                
        
        if (max_obs_red[0] > 5):
            if (max_obs_red[1] < SCREEN_LEFTSIDE) or (max_obs_green[1] > SCREEN_RIGHTSIDE):
                hal.turning_direction = 0
                hal.turn_direction()
                
            
        
        hal.go_forward(255)
        
        

        #get areas and contours-----------------
        
        #get turn direction based on line color----------
        
        #get turn direction based on line color----------
        
        
                

        if (loops == 12):
            break
        
        
        
        #DRAWING------------------------------------------------------
        #draw rois---------s
        for roi in ROIS:
            hal.vision.draw_roi(roi)
        draw_obstacle(hal.vision.frame, max_obs_red[1], max_obs_red[2])
        draw_obstacle(hal.vision.frame, max_obs_green[1], max_obs_green[2])
        
        #draw rois---------
            
        #hal.vision.draw_contours(green_cnt, CLOSED_GENERAL_ROI, (0,0,255))
            
        cv.imshow("frame", hal.vision.frame)
        
        #------------
        if cv.waitKey(1) == ord('q') or not running:
            hal.vision.camera_cap.release()
            cv.destroyAllWindows()
            
        
    except Exception as e:
        print("Exception:", e)
        #print(traceback.format_exc())
        hal.Stop()
        break
    
    

hal.Stop()
exit()



