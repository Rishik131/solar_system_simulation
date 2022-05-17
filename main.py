import pygame
import math
pygame.init()
w,h = 800,800
win = pygame.display.set_mode((w,h))
pygame.display.set_caption('Planet simulation')
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()