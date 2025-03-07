from vision import *
from board  import *

class HALBI():
    """
        
    """
    def __init__(self, serial_port: any, cam_width: int, cam_height: int):

        self.Vision = VisionController(cam_width, cam_height)
        self.Board  = ArduinoController(serial_port)

        self.turns: int = 0
        """Number of turns the car has made in the circuit"""

        self.first_color_detected : int = 0
        """First color that the camera detected\n 
        0 = None
        1 = Red, 
        2 = Green, 
        3 = Blue,
        4 = Orange
        """


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
    def setup_HALBI(self, pins : dict):
        """
            Setup all the pins of HALBI on the ArduinoController class \n
            if you don't pass all the keys from the dictionary it will 
            raise an exception

            Args:
                pins = {
                        "LED": [led_r, led_g, led_b],\n
                        "BUZZER": a digital pin,\n
                        "SERVO": a digital pin,\n
                        "MOTOR_EN": a pwm pin,\n
                        "MOTOR_IN1": a digital pin,\n
                        "MOTOR_IN2": a digital pin
                    }
        """
        self.pins = pins
        try:
            if self.pins["LED"] != None:
                self.Board.setup_led(self.pins["LED"])
            if self.pins["BUZZER"] != None:
                self.Board.setup_buzzer(self.pins["BUZZER"])
            if self.pins["SERVO"] != None:
                self.Board.setup_servo(self.pins["SERVO"])
            if self.pins["MOTOR_EN"] != None and self.pins["MOTOR_IN1"] != None and self.pins["MOTOR_IN2"] != None:
                self.Board.setup_motor(self.pins["MOTOR_IN1"], self.pins["MOTOR_IN2"], "MOTOR_EN")
        except:
            raise("Error setting up HALBI, check your pins!")

    def Stop(self):
        #etc
        pass

    def Start(self):
        #etc
        pass

    def go_forward(self):
        pass
    
    def go_backward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def _test(self):
        """for testing components or mechanic movements"""

        # don't execute this function if debug mode is disabled
        if not self.debug:
            return
        #etc
        pass
