import pygame
import math
#initialising workspace
pygame.init()
w,h = 800,800
win = pygame.display.set_mode((w,h))
pygame.display.set_caption('Planet simulation')
white = (255,255,255)
yellow = (255,255,0)
blue = (100,149,237)
red = (188,39,50)
dark_grey = (80,78,81)

#creating planets
class planet:
    au = 149.6e6 * 1000
    g = 6.67428e-11
    scale = 200/au # 1au == 100px
    timestep = 3600*24

    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.sun = False
        self.dist_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self,win):
        x = self.x * self.scale + w/2
        y = self.y * self.scale + h/2
        pygame.draw.circle(win,self.color,(x,y),self.radius)

    def attraction(self, other):
        other_x,other_y = other.x, other.y
        dist_x = other.x - self.x
        dist_y = other.y - self.y
        dist = math.sqrt(dist_x**2 + dist_y**2)
        if other.sun:
            self.dist_to_sun = dist

#creating procedure
def main():
    run = True
    clock = pygame.time.Clock()

    #initialising bodies
    sun = planet(0,0,30,yellow,198892*10**30)
    sun.sun = True
    mercury = planet(.387*planet.au,0,8,dark_grey,3.3*10**23)
    venus = planet(.723*planet.au,0,14,white,4.8685*10**24)
    earth = planet(-1*planet.au,0,16,blue,5.9742*10**24)
    mars = planet(-1.524*planet.au,0,12,red,6.39*10**23)
    planets = [sun,mercury,venus,earth,mars]

    #running display window
    while run:
        clock.tick(60)
        # win.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for body in planets:
            body.draw(win)
        pygame.display.update()
    pygame.quit()
main()