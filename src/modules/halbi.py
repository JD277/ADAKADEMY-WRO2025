from vision import *
from board  import *

class HALBI():

    def __init__(self, serial_port: any, cam_width: int, cam_height: int):

        self.Vision = VisionController(cam_width, cam_height)
        self.Board  = ArduinoController(serial_port)

        self.turns: int = 0
        """Number of turns the car has made in the circuit"""

        self.first_color_detected : int = 0
        """First color that the camera detected\n 
        1 = Red, 
        2 = Green, 
        0 = None"""


        self.regions = {}
        """Dictionary to store the regions of interest that the camera will work in.\n
        Example:\n
        regions["Up Left Corner"] = ROI(0, 0, 50, 50)"""

        self.turning_direction: int = 0
        """Direction that the car will be running in, this will by determined by the vision controller\n
        1 = Left,
        2 = Right,
        0 if the camera hasn't detected the direction."""

        self.DEBUG_MODE = True
        """Optional mode for debugging, 
         only active on testing since debugging functions and log prints may slow down the program"""

    def Stop(self):
        #etc
        pass

    def Start(self):
        #etc
        pass

    def _test(self):
        """for testing components or mechanic movements"""

        #don't execute this function if debug mode is disabled
        if not self.debug:
            return
        #etc
        pass
