# importing pygame module
import pygame
import halbi
import sys


pygame.init()
 
turn_left = pygame.K_a
turn_right = pygame.K_d

go_forward = pygame.K_w
go_backward = pygame.K_s


display = pygame.display.set_mode((300, 300))


hal = halbi.HALBI("/dev/ttyACM0", 640, 480)

pins = {}

hal.setup_HALBI(pins)

while True:
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[go_forward]:
        hal.go_forward()

    if keys[go_backward]:
        hal.go_backward()

    if keys[turn_left]:
        hal.turn_left()

    if keys[turn_right]:
        hal.turn_right()