# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = random.randint(0, 640 - robot.get_width())
robot_y = random.randint(0, 480 - robot.get_height())
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]
            target_y = event.pos[1]
        click_x = abs(target_x - robot_x)
        click_y = abs(target_y - robot_y)

        if click_x < 50 and click_y < 86:
            robot_x = random.randint(0, 640 - robot.get_width())
            robot_y = random.randint(0, 480 - robot.get_height())

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)