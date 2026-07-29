# WRITE YOUR SOLUTION HERE:
import pygame
from datetime import datetime

pygame.init()
window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
pygame.draw.circle(window, (255, 0, 0), (320, 240), 10)
pygame.draw.circle(window, (255, 0, 0), (320, 240), 200, 10)

while True:
    pygame.display.set_caption(datetime.now().strftime("%H:%M:%S"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.draw.line(window, (0, 0, 255), (320, 240), (440, 360), 2)
    pygame.draw.line(window, (0, 0, 255), (320, 240), (180, 140), 4)
    pygame.draw.line(window, (0, 0, 255), (320, 240), (210, 250), 7)
    pygame.display.flip()


    clock.tick(60)