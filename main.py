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
        self.l = [self.x,self.y,self.x-(self.rad*2),self.y,self.x-(self.rad*4),self.y,self.x-(self.rad*6),self.y,self.x-(self.rad*8),self.y]
        for i in range(0,self.krugovi*2):
            self.l.append(self.x)
            self.l.append(self.x)
    def draw(self,window):
        for i in range(0,self.krugovi*2,2):
            if i == 0:
                pygame.draw.circle(window,pygame.Color(255,255,0),(self.x-(self.rad*i),self.y),self.rad)
                pygame.draw.circle(window,pygame.Color(255,100,10),(self.x-(self.rad*i),self.y),self.rad-10)
                pygame.draw.circle(window,pygame.Color(0,0,0),(self.x-(self.rad*i)+5,self.y-7),5)
                pygame.draw.circle(window,pygame.Color(0,0,0),(self.x-(self.rad*i)+5,self.y+7),5)
            else:
                pygame.draw.circle(window,pygame.Color(255,255,0),(self.x-(self.rad*i),self.y),self.rad)
                pygame.draw.circle(window,pygame.Color(255,100,10),(self.x-(self.rad*i),self.y),self.rad-10)

    def move(self, keys):
        self.x += self.direction_x
        self.y += self.direction_y
        if keys[pygame.K_DOWN] and self.direction_y != -0.15 or keys[pygame.K_s] and self.direction_y != -0.15:
            self.direction_x = 0
            self.direction_y = 0.15
        if keys[pygame.K_UP] and self.direction_y != 0.15 or keys[pygame.K_w] and self.direction_y != 0.15:
            self.direction_x = 0
            self.direction_y = -0.15
        if keys[pygame.K_RIGHT] and self.direction_x != -0.15 or keys[pygame.K_d] and self.direction_x != -0.15:
            self.direction_x = 0.15
            self.direction_y = 0
        if keys[pygame.K_LEFT] and self.direction_x != 0.15 or keys[pygame.K_a] and self.direction_x != 0.15:
            self.direction_x = -0.15
            self.direction_y = 0
        
class Apple:
    def __init__(self,x,y,rad):
        self.x = x
        self.y = y
        self.rad = rad
        self.sprite_img = pygame.image.load('apple.png')
        self.width = self.sprite_img.get_width()*0.07
        self.height = self.sprite_img.get_height()*0.07
        self.scaled_img = pygame.transform.scale(self.sprite_img, (self.width, self.height))
    def draw(self,window):
        self.width = self.scaled_img.get_width()
        self.height =self.scaled_img.get_height()
        window.blit(self.scaled_img, (self.x - self.width/2, self.y - self.height/2))
s1 = snake(300,100,30,5,0.15,0)
apple = []
score = 0
hiscore = 0
x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
a1 = Apple(x_a,y_a,35)
apple.append(a1)
while True:
    
    window.fill("White")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
    if collison(a1.x,a1.y,a1.rad,s1.x,s1.y,s1.rad):
        x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
        y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
        a1 = Apple(x_a,y_a,35)
        score+=1
    s1.move(keys)
    s1.draw(window)
    a1.draw(window)
    pygame.display.update()