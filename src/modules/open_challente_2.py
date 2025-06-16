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

    try:
        for i in range(12):
            hal.go_forward(255)
            time.sleep(2.8)
            
            hal.turn_right()
            time.sleep(1.35)
            
            hal.turn_center()
            time.sleep(0.8)
        
            
            if i == 11:
                hal.Stop()
                running = False
                
    except Exception as e:
        print("Exception", e)
        stop()
    
    

hal.Stop()
exit()

