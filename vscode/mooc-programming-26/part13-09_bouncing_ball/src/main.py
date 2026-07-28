# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 320
y = 240
x_velocity = 1
y_velocity = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity

    if x_velocity > 0 and x + ball.get_width() >= 640:
        x_velocity = -x_velocity
    if x_velocity < 0 and x <= 0:
        x_velocity = -x_velocity

    if y_velocity > 0 and y + ball.get_height() >= 480:
        y_velocity = -y_velocity
    if y_velocity < 0 and y <=0:
        y_velocity = -y_velocity
    

    clock.tick(60)