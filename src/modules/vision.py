import cv2 as cv
import numpy as np
from constants import *



class VisionController():
    """
        Initialize the vision controller with the desired resolution

        Args:
            width: is the widness of the cam resolution
            height: is the the high of the cam resolution
    """
    # init picamera module with desired resolution
    def __init__(self, usb_port):

        self.image_width  = 640
        self.image_height = 480
        self.image_lab = 0
        self.frame = any
        self.camera_cap = cv.VideoCapture(usb_port)
        self.camera_cap.set(cv.CAP_PROP_FRAME_WIDTH, self.image_width)
        self.camera_cap.set(cv.CAP_PROP_FRAME_HEIGHT, self.image_height)
        #self.camera_cap.set(cv.CAP_PROP_CONTRAST, 145)

        


    def receive_image(self):
        """Receive image array from Picamera and convert it to hsv format"""
        ret, frame_read = self.camera_cap.read()
        if not ret:
            print("No se pudo obtener imagen de la camara.")
        self.frame = frame_read
    

        self.image_lab = cv.cvtColor(self.frame, cv.COLOR_BGR2LAB)
        self.image_lab = cv.GaussianBlur(self.image_lab, (7,7), 0)

    def draw_roi(self, roi):
        cv.rectangle(self.frame, (roi.x1, roi.y1), (roi.x2, roi.y2), (0,255,0), 2)

    def draw_contours(self, cnt, roi, color):
        cv.drawContours(self.frame[roi.y1:roi.y2, roi.x1:roi.x2], cnt, -1, color, 2)

    def find_contours(self, range, roi: ROI):
        """
            Find contours of an image within a defined color range and region of interest.

            Args:
                range:is the range of the colors that we're looking for
                roi: region of interest of the
            
            Return:
                The contours of the ROI
        """
        # Get region of interest (ROI)
        img_segmented = self.image_lab[roi.y1:roi.y2, roi.x1:roi.x2]

        # get lower and upper color limits from the provided range
        lower_mask = np.array(range[0])
        upper_mask = np.array(range[1])

        # Get color mask
        mask = cv.inRange(img_segmented, lower_mask, upper_mask)

        # Reduce image noise
        kernel = np.ones((5, 5), np.uint8)
        eroded_mask = cv.erode(mask, kernel, iterations=1)
        dilated_mask = cv.dilate(eroded_mask, kernel, iterations=1)

        # Get contours...
        contours = cv.findContours(dilated_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

        return contours
    
    # Finds the largest contour in a list and returns it aswell as its position and area.
    def max_contour(self, contours, roi: ROI):
        """
            Finds the largest contour in a list and returns it aswell as its position and area.

            Args:
                contours: contours of the image
                roi: region of th interest
            
            Return:
                The largest detected object
        """
        # make sure there are contours to check for
        #if len(contours) == 0:
            #return 0
        
        max_area = 0
        max_y = 0
        max_x = 0
        max_cnt = any

        for c in contours:
            area = cv.contourArea(c)

            if area > 100:  # Filter contours that are too small
                approx = cv.approxPolyDP(c, 0.01 * cv.arcLength(c, True), True)
                x, y, w, h = cv.boundingRect(approx)
                #cv.rectangle(self.frame, (x, y), (x + w, y + h), (255,0,0), 1)
                

                # Convert relative position from the ROI to global position on camera.
                x += roi.x1 + w // 2
                y += roi.y1 + h // 2

                # ROI          # Screen
                # ------       -----------------------
                # |    |  -->  |     ------          |
                # ------       |     |    |          |
                #              |     ------          |
                #              |                     |
                #              -----------------------

                if area > max_area:
                    max_area = area
                    max_y = y
                    max_x = x
                    max_cnt = c

        return 	[max_area, max_x, max_y, max_cnt]
    
    
if __name__ == "__main__":
    from halbi import *


    ROIs = [OPEN_ROI_LINES]
    
    turnThresh = 150
    exitThresh = 1500
    
    
    visionc = VisionController(0)
    leftArea = 0
    rightArea = 0
    
    leftTurn = False
    rightTurn = False

    while (1):
    
            visionc.receive_image()
    
            
            # contornos paredes negras
            cnt_lines_blue = visionc.find_contours(mask_blue, OPEN_ROI_LINES)
            cnt_lines_orange = visionc.find_contours(mask_orange, OPEN_ROI_LINES)
            
            
            
            
        
            visionc.draw_contours(cnt_lines_blue, OPEN_ROI_LINES, (255,0,255))

            
                
            
            for roi in ROIs:
                visionc.draw_roi(roi)

            
            cv.imshow("frame", visionc.frame)
            
            if cv.waitKey(1) == ord('q'):
                break
        

    cv.destroyAllWindows()
