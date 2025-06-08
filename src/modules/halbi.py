from vision import *
from board  import *
from constants import *

class HALBI():
    """
        
    """
    def __init__(self, serial_port: any, camera_port: any, cam_width: int, cam_height: int):
        self.leftWallArea = 0
        self.rightWallArea = 0

        self.Vision = VisionController(cam_width, cam_height, camera_port)
        self.Board  = ArduinoController(serial_port)

        self.turns: int = 0
        """Number of turns the car has made in the circuit"""
        
        self.current_angle = 0
        self.previous_angle = 0
        
        self.kp = 0.02 #valor de la proporcional
        self.kd = 0.006 #valor de la derivativa
        
        self.straightAngle = 90 #Angulo en que el carro va recto
        
        self.turnThresh = 150 #si el area de una pared es menor a este valor el carro entra en un giro
        self.exitThresh = 1500 #si el area de ambas paredes es mayor a este valor el carro deja de girar
        self.areaDiff = 0 #diferencia entre las areas de las paredes
        self.areaPrevDiff = 0 #valor previo de la diferencia de area para el desvio proporcional

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
        """Optional mode for debugging, 
         only active on testing since debugging functions and log prints may slow down the program"""
    def setup_HALBI(self):
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
        try:
            self.Board.setup_servo(SERVO_PIN)
            self.Board.setup_motor(IN_3, IN_4, "MOTOR",5)
        except:
            raise("Error setting up HALBI, check your pins!")

    def Stop(self):
        self.Board.set_motor_speed("MOTOR",0)

    def Start(self):
        #etc
        pass

    def go_forward(self):
       self.Board.set_motor_speed("MOTOR",100)
    
    def go_backward(self):
        self.Board.set_motor_speed("MOTOR",-100)

    def turn_left(self):
        self.Board.set_servo_angle(SERVO_PIN,RIGHT)

    def turn_right(self):
        self.Board.set_servo_angle(SERVO_PIN,LEFT)

    def turn_center(self):
        self.Board.set_servo_angle(SERVO_PIN,CENTER)

    def _test(self):
        """for testing components or mechanic movements"""

        # don't execute this function if debug mode is disabled
        if not self.debug:
            return
        #etc
        pass
