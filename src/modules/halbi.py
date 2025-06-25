from src.modules.vision import *
from src.modules.board  import *
from src.constants import *

class HALBI():
    """
        
    """
    def __init__(self, serial_port: any, camera_port: any):

        self.vision = VisionController(camera_port)
        self.board  = ArduinoController(serial_port)

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

        

        self.turning_direction: int = 0
        """Direction that the car will be running in, this will by determined by the vision controller\n
        1 = Left,
        2 = Right,
        0 if the camera hasn't detected the direction."""

        self.DEBUG_MODE = True
        """Optional mode for debugging"""
    
    def setup_HALBI(self, pins:dict):
        """
            Setup all the pins of HALBI on the ArduinoController class \n
            if you don't pass all the keys from the dictionary it will 
            raise an exception

            Args:
                pins = {
                        "LED": [led_r, led_g, led_b],\n
                        "BUZZER": a pwm pin,\n
                        "SERVO": a digital pin,\n
                        "MOTOR_EN": a pwm pin,\n
                        "MOTOR_IN3": a digital pin,\n
                        "MOTOR_IN4": a digital pin,\n
                        "BUTTON": a digital pin,\n
                    }
        """
        try:
            self.board.setup_servo(pins["SERVO"])
            self.board.setup_motor(pins["MOTOR_IN3"], pins["MOTOR_IN4"], 'MOTOR', pins["MOTOR_EN"])
            self.board.setup_button(pins["BUTTON"])
            for i in pins["LED"]:
                self.board.setup_led(i)
                self.board.led_on(i)
                time.sleep(0.05)
                self.board.led_off(i)
            
        except:
            raise("Error setting up HALBI, check your pins!")

    def Stop(self):
        self.board.set_motor_speed("MOTOR",0)
        self.turn_center()
        for i in PINS["LED"]:
            self.board.led_off(i)

    def Start(self):
        return self.board.buttons[PINS["BUTTON"]].state

    def go_forward(self,speed: int = 255):
        self.board.set_motor_speed("MOTOR",speed)
        #self.board.led_on(LED_WHITE)
        self.board.led_off(LED_RED)
        self.board.led_off(LED_YELLOW)
        self.board.led_off(LED_GREEN)
    
    def go_backward(self,speed: int = 255):
        self.board.set_motor_speed("MOTOR",-speed)
        self.board.led_off(LED_YELLOW)
        self.board.led_off(LED_GREEN)
        self.board.led_off(LED_RED)
        self.board.led_off(LED_WHITE)

    def turn_left(self):
        self.board.set_servo_angle(SERVO_PIN,LEFT)
        self.board.led_off(LED_RED)
        self.board.led_on(LED_YELLOW)
        self.board.led_off(LED_WHITE)
        self.board.led_off(LED_GREEN)

    def turn_right(self):
        self.board.set_servo_angle(SERVO_PIN,RIGHT)
        self.board.led_off(LED_RED)
        self.board.led_on(LED_YELLOW)
        self.board.led_off(LED_GREEN)
        self.board.led_on(LED_WHITE)
        
    def turn_direction(self):
        if self.turning_direction == 0:
            self.turn_center()
        elif self.turning_direction == 1:
            self.turn_left()
        elif self.turning_direction == 2:
            self.turn_right()

    def turn_center(self):
        self.board.set_servo_angle(SERVO_PIN,CENTER)


    def _test(self):
        """for testing components or mechanic movements"""


        # don't execute this function if debug mode is disabled
        if not self.debug:
            return
        
        self.board.interactive_test_menu()
    def close(self):
        self.board.close()

