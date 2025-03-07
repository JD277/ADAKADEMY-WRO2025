import cv2 as cv
import numpy as np
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
    """Recive two points from the frame  to extract the Region Of Interest"""

    x1: int; y1: int
    x2: int; y2: int


@dataclass
class ContourInfo:
    """Class containing info about a detected object: position, area and contours"""
    area    : int
    x       : int
    y       : int
    contour : any



# Pendiente: Hacer que el controlador de vision funcione en hilos.

class VisionController():
    """
        Initialize the vision controller with the desired resolution

        Args:
            width: is the widness of the cam resolution
            height: is the the high of the cam resolution
    """
    # init picamera module with desired resolution
    def __init__(self, width: int, height: int):


        self.image_width  = width
        self.image_height = height
        self.image_hsv = 0  
        self.frame = 0

        self.picam = Picamera2()

        # Configure picamera2
        preview_config = self.picam.create_preview_configuration(main={"size": (width, height)})
        self.picam.configure(preview_config)

        self.picam.start()


    def receive_image(self):
        """Receive image array from Picamera and convert it to hsv format"""
        self.frame = self.picam.capture_array()
        self.image_hsv = cv.cvtColor(self.frame, cv.COLOR_RGB2HSV)


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
        img_segmented = self.image_hsv[roi.y1:roi.y2, roi.x1:roi.x2]

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
        if len(self.contours) == 0:
            return 0
        
        max_area = 0
        max_y = 0
        max_x = 0
        max_cnt = None

        for c in contours:
            area = cv.contourArea(c)

            if area > 100:  # Filter contours that are too small
                approx = cv.approxPolyDP(c, 0.01 * cv.arcLength(c, True), True)
                x, y, w, h = cv.boundingRect(approx)

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

        return ContourInfo(max_area, max_x, max_y, max_cnt)
