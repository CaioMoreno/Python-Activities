# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 320 - robot.get_width()
y = 240 - robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
                            

        if event.type == pygame.QUIT:
            exit()

    if x + robot.get_width() >= 640:
        to_right = False
    if x <= 0:
        to_left = False
    if y + robot.get_height() >= 480:
        to_down = False
    if y <= 0:
        to_up = False

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_down:
        y += 2
    if to_up:
        y -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)