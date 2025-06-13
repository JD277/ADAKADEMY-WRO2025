import time
import pyfirmata2

class ArduinoController:
    def __init__(self, port=None):
        """
        Initializes the connection with Arduino.
        If no port is specified, it attempts to autodetect.
        """
        # If port is not provided, auto_setup returns the proper port
        self.board = pyfirmata2.Arduino(port)

        # Start the iterator to continuously read data from Arduino
        self.iterator = pyfirmata2.util.Iterator(self.board)
        self.iterator.start()

        # Dictionaries to store components
        self.servos = {}
        self.motors = {}
        self.leds = {}
        self.buzzers = {}
        self.buttons = {}

    def setup_led(self, pin: int):
        """Configures an LED on the specified pin."""
        self.leds[pin] = self.board.get_pin(f'd:{pin}:o')

    def led_on(self, pin: int):
        """Turns on the LED."""
        self.leds[pin].write(1)

    def led_off(self, pin: int):
        """Turns off the LED."""
        self.leds[pin].write(0)

    def setup_buzzer(self, pin: int):
        """Configures a buzzer on the specified pin."""
        self.buzzers[pin] = self.board.get_pin(f'd:{pin}:o')

    def buzzer_on(self, pin: int):
        """Activates the buzzer."""
        self.buzzers[pin].write(1)

    def buzzer_off(self, pin: int):
        """Deactivates the buzzer."""
        self.buzzers[pin].write(0)

    def setup_servo(self, pin: int):
        """Configures a servo on the specified pin."""
        self.servos[pin] = self.board.get_pin(f'd:{pin}:s')  # Servo mode
        time.sleep(0.1)  # Small pause for initialization

    def set_servo_angle(self, pin: int, angle: float):
        """Sets the servo angle (0-180 degrees)."""
        self.servos[pin].write(angle)

    def setup_motor(self, in1_pin: int, in2_pin: int, motor_id: str, enb_pin:int):
        """
        Configures a DC motor using the DRV8833 driver.
        For l298n, two control signals (in1 and in2) are used.
        The motor_id is an identifier for storing this motor's configuration.
        """
        self.motors[motor_id] = {
            'in1': self.board.get_pin(f'd:{in1_pin}:o'),  # PWM capable pin
            'in2': self.board.get_pin(f'd:{in2_pin}:o'),   # PWM capable pin
            'eb': self.board.get_pin(f'd:{enb_pin}:p')   # PWM capable pin
        }

    def set_motor_speed(self, motor_id: str, speed: int):
        """
        Controls the speed and direction of the motor (-255 to 255) using DRV8833.
        If speed > 0: forward, if speed < 0: reverse, and if speed == 0: stop.
        """
        # Limit the speed to the range -255 to 255
        normalized_speed = abs(speed) / 255.0  # Normalize to 0-1 for PWM

        motor = self.motors[motor_id]

        if speed > 0:
            # Forward: PWM on in1, in2
            motor['eb'].write(normalized_speed)
            motor['in1'].write(1)
            motor['in2'].write(0)
        elif speed < 0:
            # Reverse: in1 low, PWM on in2
            motor['eb'].write(normalized_speed)
            motor['in1'].write(0)
            motor['in2'].write(1)
        else:
            # Stop motor: both signals low
            motor['eb'].write(0)
            motor['in1'].write(0)
            motor['in2'].write(0)
            
    def setup_button(self, pin: int):
        """
            Configures a button on the specified pin with internal pull-up resistor.
            Returns the pin object for direct access if needed.
        """
        button_pin = self.board.get_pin(f'd:{pin}:u')
        button_pin.register_callback(lambda data: self.button_callback(data, pin))
        button_pin.enable_reporting()
        self.buttons[pin] = button_pin
        self.buttons[pin].state = True
    
    def button_callback(self, data, pin:int):
        """
        Se llama automáticamente cuando cambia el estado del botón
        data == 1 -> Botón suelto (HIGH)
        data == 0 -> Botón presionado (LOW)
        """
        self.buttons[pin].state = data
        
    def is_button_pressed(self, pin: int):
        """
        Return:
            true if the button is released, otherwise false
        """
        return self.buttons[pin].state
    
    def interactive_test_menu(self):
        """Interactive console menu to test LEDs, buttons, motors, and servos."""
        while True:
            print("\n=== Menú de Pruebas ===")
            print("1. Probar LED")
            print("2. Probar Botón")
            print("3. Probar Motor")
            print("4. Probar Servo")
            print("5. Salir")
            choice = input("Selecciona una opción (1-5): ")

            try:
                choice = int(choice)
            except ValueError:
                print("Opción inválida. Por favor ingresa un número entre 1 y 5.")
                continue

            if choice == 1:
                # Test LED
                pin = int(input("Introduce el pin del LED (ej. 4): "))
                self.setup_led(pin)
                print("Encendiendo LED...")
                self.led_on(pin)
                time.sleep(1)
                print("Apagando LED...")
                self.led_off(pin)

            elif choice == 2:
                # Test Button
                pin = int(input("Introduce el pin del botón (ej. 3): "))
                self.setup_button(pin)
                print(f"Esperando presión del botón en pin {pin}. Presiona Ctrl+C para salir...")
                try:
                    while True:
                        print(self.is_button_pressed(pin))
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print("Saliendo de la prueba del botón.")

            elif choice == 3:
                # Test Motor
                in1 = int(input("Pin IN1 del motor (ej. 12): "))
                in2 = int(input("Pin IN2 del motor (ej. 11): "))
                en = int(input("Pin ENB del motor (ej. 10): "))
                motor_id = input("Nombre del motor (ej. 'back'): ")

                self.setup_motor(in1, in2, motor_id, en)
                print(f"Motor '{motor_id}' configurado. Probando movimiento...")

                speed = int(input("Velocidad del motor (-255 a 255): "))
                duration = float(input("Duración del movimiento (segundos): "))

                self.set_motor_speed(motor_id, speed)
                print(f"Moviendo motor '{motor_id}' durante {duration}s...")
                time.sleep(duration)
                self.set_motor_speed(motor_id, 0)

            elif choice == 4:
                # Test Servo
                pin = int(input("Pin del servo (ej. 9): "))
                self.setup_servo(pin)
                print(f"Servo en pin {pin} configurado.")

                while True:
                    angle_input = input("Ingresa ángulo (0-180), o 'salir' para terminar: ")
                    if angle_input.lower() == 'salir':
                        break
                    try:
                        angle = int(angle_input)
                        if 0 <= angle <= 180:
                            self.set_servo_angle(pin, angle)
                            print(f"Girando servo a {angle}°")
                        else:
                            print("Ángulo fuera de rango. Debe ser entre 0 y 180.")
                    except ValueError:
                        print("Entrada inválida. Ingresa un número o escribe 'salir'.")

            elif choice == 5:
                print("Saliendo del menú de pruebas.")
                break

            else:
                print("Opción no válida. Selecciona entre 1 y 5.")
    def close(self):
        """Closes the connection with Arduino."""
        self.iterator.stop()
        self.board.exit()
        
from constants import *
nano = ArduinoController("/dev/ttyUSB0")
nano.interactive_test_menu()
# Testing LEDs
# nano.setup_led(4)
# nano.led_on(4)
# time.sleep(1)
# nano.led_off(4)

# Testing Buttons
"""nano.setup_button(3)
print("Configurado")
input()"""

# Testing Motors
"""nano.setup_motor(12,11,"back",10)
nano.set_motor_speed('back',100)
print("listo")
time.sleep(2)
nano.set_motor_speed('back',0)
time.sleep(2)
nano.close()"""

# Testing servo
"""nano.setup_servo(9)
nano.set_servo_angle(9,20)
time.sleep(1)
print(120)
nano.set_servo_angle(9,90)
time.sleep(2)
print(70)
nano.set_servo_angle(9,0)
time.sleep(2)
print(90)
nano.set_servo_angle(9,20)
"""
