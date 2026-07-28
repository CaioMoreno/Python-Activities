# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

window.fill((0, 0, 0))

for i in range(20):
        y = random.randint(-200, -30)
        x = random.randint(0, 640 - robot.get_width())

        window.blit(robot, (x, y))

#I have to resolve the random robots in the animation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    window.blit(robot, (x, y))
    if y + robot.get_height() < 480:
        y += 1
    elif y + robot.get_height() >= 480 and x <= 320:
        x -= 1
    elif y + robot.get_height() >= 480 and x > 320:
        x += 1

    clock.tick(60)