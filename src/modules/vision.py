import cv2 as cv
import numpy
from picamera2 import Picamera2

from dataclasses import dataclass


# Types:

# Region Of Interest:
#
#  x1,y1----------------
#  |                    |
#  |                    |
#  |                    |
#  -------------------x2,y2   

@dataclass
class ROI:
    """Region Of Interest"""
    x1: int
    y1: int
    x2: int
    y2: int
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1; self.y1 = y1
        self.x2 = x2; self.y2 = y2


@dataclass
class ContourInfo:
    """Class containing info about a detected object: position, area and contours"""
    area: int
    x: int
    y: int
    contour: 0
    def __init__(self, area: int, x: int, y: int, contour):
        self.area = area
        self.x = x; self.y = y
        self.contour = contour

# Class:

class VisionController():

    #init picamera module with desired resolution
    def __init__(self, width: int, height: int):
        self.image_width  = width
        self.image_height = height
        self.image_hsv = 0  

        self.picam = Picamera2()

        preview_config = self.picam.create_preview_configuration(main={"size": (640, 480)})
        self.picam.configure(preview_config)

        self.picam.start()

    #receive image array from Picamera
    #and convert it to hsv format
    def receive_image(self):
        frame = self.picam.capture_array()
        self.image_hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)


    #find contours of an image within a defined color range and region of interest.
    def find_contours(self, range, roi: ROI):

        # get region of interest (ROI)
        img_segmented = self.image_hsv[roi.y1:roi.y2, roi.x1:roi.x2]

        # get lower and upper color limits from the provided range
        lower_mask = np.array(range[0])
        upper_mask = np.array(range[1])

        # get color mask
        mask = cv.inRange(img_segmented, lower_mask, upper_mask)

        # reduce image noise
        kernel = np.ones((5, 5), np.uint8)
        eroded_mask = cv.erode(mask, kernel, iterations=1)
        dilated_mask = cv.dilate(eroded_mask, kernel, iterations=1)

        # get contours...
        contours = cv.findContours(dilated_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

        return contours
    
    #Finds the largest contour in a list and returns it aswell as its position and area.
    def max_contour(self, contours, roi: ROI):

        #make sure there are contours to check for
        if len(self.contours) == 0:
            return 0
        
        max_area = 0
        max_y = 0
        max_x = 0
        max_cnt = None

        for c in contours:
            area = cv.contourArea(c)

            if area > 100:  # filter contours that are too small
                approx = cv.approxPolyDP(c, 0.01 * cv.arcLength(c, True), True)
                x, y, w, h = cv.boundingRect(approx)

                # convert relative position from the ROI to global position on camera.
                x += roi.x1 + w // 2
                y += roi.y1 + h // 2

                # roi          #screen
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

        return ContourInfo(max_area, max_y, max_x, max_cnt)