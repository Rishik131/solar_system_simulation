import pygame
import math
pygame.init()
w,h = 800,800
win = pygame.display.set_mode((w,h))
pygame.display.set_caption('Planet simulation')
white = (255,255,255)

class planet:
    au = 149.6e6 * 1000
    g = 6.67428e-11
    scale = 250/au # 1au == 100px
    timestep = 3600*24

    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.sun = False
        self.dist = 0
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self,win):
        x = self.x * self.scale + w/2
        y = self.y * self.scale + h/2
        pygame.draw.circle(win,self.color,(x,y),self.radius)

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