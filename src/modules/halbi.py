from vision import *
from board  import *

class HALBI():

    def __init__(self):
        self.Vision : VisionController
        self.Board  : ArduinoController


        self.DEBUG_MODE = True
        """Optional mode for debugging, 
        only active on testing since debugging functions and logs may slow down the program"""

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

# Test
if __name__ == "__main__":

    halbi = HALBI()

    halbi.Vision = VisionController(width=640, height=480)
    halbi.Board = ArduinoController(port = 'dev/tty0')



