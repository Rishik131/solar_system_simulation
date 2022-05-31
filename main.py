import pygame
import math
pygame.init()
w,h = 800,800
win = pygame.display.set_mode((w,h))
pygame.display.set_caption('Planet simulation')
white = (255,255,255)

class planet:
    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        win.fill(white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
main()