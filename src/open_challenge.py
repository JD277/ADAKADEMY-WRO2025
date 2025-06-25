from src.modules.halbi import *
from src.constants import *

# Halbi setup
hal = HALBI("/dev/ttyUSB0", 0)
hal.setup_HALBI(PINS)

# Centering the directions
hal.turn_center()

# Saving the ROIs
ROIS = [OPEN_ROI_CENTER, ROI_LINES]

# Waiting to press the button
while hal.Start():
    pass

running = True
loops = 0
line_detected = False

# Start moving
while running:
    try:
        hal.go_forward(0)
        # get areas and contours-----------------
        hal.vision.receive_image()
        
        cnt_lines_blue = hal.vision.find_contours(mask_blue_test, ROI_LINES)
        cnt_lines_orange = hal.vision.find_contours(mask_orange_test, ROI_LINES)
        cnt_front_wall = hal.vision.find_contours(mask_black_test, OPEN_ROI_CENTER)
        
        black_area = hal.vision.max_contour(cnt_front_wall, OPEN_ROI_CENTER)[0]
        blue_area = hal.vision.max_contour(cnt_lines_blue, ROI_LINES)[0]
        orange_area = hal.vision.max_contour(cnt_lines_orange, ROI_LINES)[0]
        # get areas and contours-----------------
        
        # get turn direction based on line color----------
        
        if (hal.turning_direction == 0): #only look for line colors if no colors have been detected yet.
            if (blue_area >= 10):
                hal.turning_direction = 1 #left
            elif (orange_area >= 10):
                hal.turning_direction = 2 #right
        # get turn direction based on line color----------
        
        # Determines if the car have to turn
        if (black_area >= TURN_THRESH):
            hal.turn_direction()
            if line_detected:
                line_detected = False

        # Center the car  
        if (hal.turning_direction != 0):
            if (black_area <= TURN_EXIT_THRESH):
                hal.turn_center()
                if not line_detected:
                    loops += 1
                    line_detected = True
                
        # Break the cycle if it has completed all the laps
        if (loops == 12):
            break

        print(loops)
        
        
        
        #DRAWING------------------------------------------------------
        #draw rois---------s
        for roi in ROIS:
            hal.vision.draw_roi(roi)
        #draw rois---------
            
        #draw contours-----------
        hal.vision.draw_contours(cnt_front_wall, OPEN_ROI_CENTER, (255,255,0))
        hal.vision.draw_contours(cnt_lines_blue, ROI_LINES, (255,255,0))
        hal.vision.draw_contours(cnt_lines_orange, ROI_LINES, (255,0,0))
        #draw contours-----------
        
        #draw final img
        cv.putText(hal.vision.frame, "black area: " + str(black_area), (0,20), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv.putText(hal.vision.frame, "blue area: " + str(blue_area), (0,40), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv.putText(hal.vision.frame, "orange area: " + str(orange_area), (0,60), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
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


