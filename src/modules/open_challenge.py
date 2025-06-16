from halbi import *
import atexit
import constants
import time

hal = HALBI("/dev/ttyUSB0", 0)

def stop():
    hal.Stop()
    print("stop")

hal.setup_HALBI(PINS)
atexit.register(stop)
hal.turn_center()

#running = False

#while hal.Start():
#    pass

running = True

while running:

    for i in range(4):
        hal.go_forward(255)
        time.sleep(3)
        hal.turn_left()
        time.sleep(1.8)
        hal.turn_center()
    
        
        if i == 3:
            hal.Stop()
            running = False
    
    

hal.Stop()
exit()
