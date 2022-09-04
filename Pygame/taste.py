import sys, pygame
from pygame import gfxdraw

pygame.init()

size = width, height = 400, 400
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("D:\GitRepos\learning-manim\Pygame\intro_ball.gif")
ballrect = ball.get_rect()

sum = 200

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    #screen.blit(ball, ballrect)
    pygame.draw.circle(screen, (255,0,0), (200,sum), 15)
    
    sum += 0.1
    pygame.display.flip()