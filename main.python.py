import os
import pygame
import random
import math
pygame.init()
def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False
WIDTH,HEIGHT = 800,800
window = pygame.display.set_mode((WIDTH,HEIGHT))
def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False
    

class snake:
    def __init__(self,x,y,rad,krugovi,direction_x,direction_y):
        self.x = x
        self.y = y
        self.rad = rad
        self.krugovi = krugovi
        self.direction_x = direction_x
        self.direction_y = direction_y
    def draw(self,window):
        pygame.draw.circle(window,pygame.Color(255,100,10),(self.x,self.y),self.rad)
        pygame.draw.circle(window,pygame.Color(255,255,0),(self.x,self.y),self.rad)

    def move(self, keys):
        self.x += self.direction_x
        self.y += self.direction_y
        if keys(pygame.K_DOWN) or keys(pygame.K_s):
            self.direction_x = 0
            self.direction_y = 1
        if keys(pygame.K_UP) or keys(pygame.K_w):
            self.direction_x = 0
            self.direction_y = -1
        if keys(pygame.K_RIGHT) or keys(pygame.K_d):
            self.direction_x = 1
            self.direction_y = 0
        if keys(pygame.K_LEFT) or keys(pygame.K_a):
            self.direction_x = -1
            self.direction_y = 0



while True:

    window.fill("White")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys(pygame.K_ESCAPE):
        exit()