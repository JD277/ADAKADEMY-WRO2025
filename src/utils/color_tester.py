import cv2 as cv
#from picamera2 import Picamera2
import sys
from src.constants import *
import numpy as np

# Max value for LAB components
max_value = 255
max_value_L = 255
max_value_AB = 255  

maskDict = {
    "magenta": [[0,0,0], [0,0,0]],
    "red": mask_red,
    "green": mask_green,
    "blue": mask_blue_test,
    "orange": mask_orange_test,
    "black": mask_black_test
}

#set mask based on program arguments
if len(sys.argv) > 1:
    mask = maskDict[sys.argv[1].lower()]
            
    
low_L = mask[0][0]
low_A = mask[0][1]
low_B = mask[0][2]
high_L = mask[1][0]
high_A = mask[1][1]
high_B = mask[1][2]
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_L_name = 'Low L'
low_A_name = 'Low A'
low_B_name = 'Low B'
high_L_name = 'High L'
high_A_name = 'High A'
high_B_name = 'High B'

## [low]
def on_low_L_thresh_trackbar(val):
    global low_L
    global high_L
    low_L = val
    low_L = min(high_L-1, low_L)
    cv.setTrackbarPos(low_L_name, window_detection_name, low_L)
## [low]

## [high]
def on_high_L_thresh_trackbar(val):
    global low_L
    global high_L
    high_L = val
    high_L = max(high_L, low_L+1)
    cv.setTrackbarPos(high_L_name, window_detection_name, high_L)
## [high]

def on_low_A_thresh_trackbar(val):
    global low_A
    global high_A
    low_A = val
    low_A = min(high_A-1, low_A)
    cv.setTrackbarPos(low_A_name, window_detection_name, low_A)

def on_high_A_thresh_trackbar(val):
    global low_A
    global high_A
    high_A = val
    high_A = max(high_A, low_A+1)
    cv.setTrackbarPos(high_A_name, window_detection_name, high_A)

def on_low_B_thresh_trackbar(val):
    global low_B
    global high_B
    low_B = val
    low_B = min(high_B-1, low_B)
    cv.setTrackbarPos(low_B_name, window_detection_name, low_B)

def on_high_B_thresh_trackbar(val):
    global low_B
    global high_B
    high_B = val
    high_B = max(high_B, low_B+1)
    cv.setTrackbarPos(high_B_name, window_detection_name, high_B)

cap = cv.VideoCapture(2)
## [window]
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)
## [window]

## [trackbar]
cv.createTrackbar(low_L_name, window_detection_name , low_L, max_value_L, on_low_L_thresh_trackbar)
cv.createTrackbar(high_L_name, window_detection_name , high_L, max_value_L, on_high_L_thresh_trackbar)
cv.createTrackbar(low_A_name, window_detection_name , low_A, max_value_AB, on_low_A_thresh_trackbar)
cv.createTrackbar(high_A_name, window_detection_name , high_A, max_value_AB, on_high_A_thresh_trackbar)
cv.createTrackbar(low_B_name, window_detection_name , low_B, max_value_AB, on_low_B_thresh_trackbar)
cv.createTrackbar(high_B_name, window_detection_name , high_B, max_value_AB, on_high_B_thresh_trackbar)
## [trackbar]

while True:
    # Capture the frame
    ret, frame = cap.read()

    # Convert from BGR to LAB
    frame_LAB = cv.cvtColor(frame, cv.COLOR_BGR2Lab)
    
    #frame_LAB = cv.bilateralFilter(frame_LAB, d=3, sigmaColor=50, sigmaSpace=50)
    frame_LAB = cv.GaussianBlur(frame_LAB, (7, 7), 0)

    # Apply threshold using the LAB range (A and B are shifted)
    frame_threshold = cv.inRange(frame_LAB, (low_L, low_A, low_B), (high_L, high_A, high_B))
    
    

    kernel = np.ones((5, 5), np.uint8)
        
    e_frame = cv.erode(frame_threshold, kernel, iterations=1)
    d_frame = cv.dilate(e_frame, kernel, iterations=1)
    
    contours = cv.findContours(d_frame, cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE)[-2]
    
    cv.drawContours(frame, contours, -1, (238, 144, 144), 2)
    
    ## [show]
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, d_frame)
    ## [show]
    
    
    

    # Exit on 'q' or ESC
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        cap.release()
        cv.destroyAllWindows()
        
        # Print the LAB range for reference
        print([[low_L, low_A, low_B], [high_L, high_A, high_B]])
        break