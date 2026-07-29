# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

pygame.init()
window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()


def calc_angle(angle: float, width: int):
    rad_angle = math.radians(angle - 90)
    x = 320 + math.cos(rad_angle) * width
    y = 240 + math.sin(rad_angle) * width
    return (x, y)

while True:
    pygame.display.set_caption(datetime.now().strftime("%H:%M:%S"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), (320, 240), 10)
    pygame.draw.circle(window, (255, 0, 0), (320, 240), 200, 10)
    
    s_angle = datetime.now().second * 6
    m_angle = (datetime.now().minute + datetime.now().second / 60) * 6
    h_angle = (datetime.now().hour % 12 + datetime.now().minute / 60) * 30

    s_xy = calc_angle(s_angle, 180)
    m_xy = calc_angle(m_angle, 170)
    h_xy = calc_angle(h_angle, 100)

    pygame.draw.line(window, (0, 0, 255), (320, 240), s_xy, 2)
    pygame.draw.line(window, (0, 0, 255), (320, 240), m_xy, 4)
    pygame.draw.line(window, (0, 0, 255), (320, 240), h_xy, 7)


    pygame.display.flip()


    clock.tick(60)