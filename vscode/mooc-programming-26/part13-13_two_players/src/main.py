# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 640 - robot.get_width()
y = 480 - robot.get_height()
i = 0
j = 0

P1_to_right = False
P1_to_left = False
P1_to_up = False
P1_to_down = False

P2_to_right = False
P2_to_left = False
P2_to_up = False
P2_to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        #player1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                P1_to_left = True
            if event.key == pygame.K_RIGHT:
                P1_to_right = True
            if event.key == pygame.K_UP:
                P1_to_up = True
            if event.key == pygame.K_DOWN:
                P1_to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                P1_to_left = False
            if event.key == pygame.K_RIGHT:
                P1_to_right = False
            if event.key == pygame.K_UP:
                P1_to_up = False
            if event.key == pygame.K_DOWN:
                P1_to_down = False
        #Player2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                P2_to_left = True
            if event.key == pygame.K_d:
                P2_to_right = True
            if event.key == pygame.K_w:
                P2_to_up = True
            if event.key == pygame.K_s:
                P2_to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                P2_to_left = False
            if event.key == pygame.K_d:
                P2_to_right = False
            if event.key == pygame.K_w:
                P2_to_up = False
            if event.key == pygame.K_s:
                P2_to_down = False
                            

        if event.type == pygame.QUIT:
            exit()

    if x + robot.get_width() >= 640:
        P1_to_right = False
    if x <= 0:
        P1_to_left = False
    if y + robot.get_height() >= 480:
        P1_to_down = False
    if y <= 0:
        P1_to_up = False

    if i + robot.get_width() >= 640:
        P2_to_right = False
    if i <= 0:
        P2_to_left = False
    if j + robot.get_height() >= 480:
        P2_to_down = False
    if j <= 0:
        P2_to_up = False

    #player1
    if P1_to_right:
        x += 2
    if P1_to_left:
        x -= 2
    if P1_to_down:
        y += 2
    if P1_to_up:
        y -= 2
    #player2
    if P2_to_right:
        i += 2
    if P2_to_left:
        i -= 2
    if P2_to_down:
        j += 2
    if P2_to_up:
        j -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (i, j))
    pygame.display.flip()

    clock.tick(60)