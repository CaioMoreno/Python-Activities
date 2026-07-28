import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
i = 0
j = 100
velocity = 1
velocity2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (i, j))
    pygame.display.flip()
    
    x += velocity
    i += velocity2

    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    if velocity2 > 0 and i+robot.get_width() >= 640:
            velocity2 = -velocity2
    if velocity2 < 0 and i <= 0:
        velocity2 = -velocity2

    clock.tick(60)