import os
import pygame
import random
import math
import time
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
clock = pygame.time.Clock()
WIDTH,HEIGHT = 800,800
window = pygame.display.set_mode((WIDTH,HEIGHT))
def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

class Part:
    def __init__(self,x,y,rad,id):
        self.x = x
        self.y = y
        self.rad = rad
        self.dx = 0
        self.dy = 0
        self.id = id
    def draw(self,window):
        if self.id == "head":
                pygame.draw.circle(window,pygame.Color(255,255,0),(self.x,self.y),self.rad)
                pygame.draw.circle(window,pygame.Color(255,100,10),(self.x,self.y),self.rad-10)
                pygame.draw.circle(window,pygame.Color(0,0,0),(self.x,self.y-7),5)
                pygame.draw.circle(window,pygame.Color(0,0,0),(self.x,self.y+7),5)
        if self.id == "body":
                pygame.draw.circle(window,pygame.Color(255,255,0),(self.x,self.y),self.rad)
                pygame.draw.circle(window,pygame.Color(255,100,10),(self.x,self.y),self.rad-10)


class Snake:
    def __init__(self,rad,krugovi,x,y,):
        self.rad = rad
        self.krugovi = krugovi
        self.distance = 8
        self.body = [Part(x,y,self.rad,"head")]
        for i in range(krugovi-1):
            self.body.append(Part(x-self.distance*i,y,self.rad,"body"))
    def draw(self,window):
        for i in range(len(self.body)):
            self.body[i].draw(window)
            
    def move(self, keys):
        
        for i in range(len(self.body)-1,0,-1):
            self.body[i] = self.body[i-1]
            
        self.body[0].x += self.body[0].dx
        self.body[0].y += self.body[0].dy
        if keys[pygame.K_DOWN] and self.body[0].dy != -self.distance or keys[pygame.K_s] and self.body[0].dy != -self.distance:
            self.body[0].dx = 0
            self.body[0].dy = self.distance
        if keys[pygame.K_UP] and self.body[0].dy != self.distance or keys[pygame.K_w] and self.body[0].dy != self.distance:
            self.body[0].dx = 0
            self.body[0].dy = -self.distance
        if keys[pygame.K_RIGHT] and self.body[0].dx != -self.distance or keys[pygame.K_d] and self.body[0].dx != -self.distance:
            self.body[0].dx = self.distance
            self.body[0].dy = 0
        if keys[pygame.K_LEFT] and self.body[0].dx != self.distance or keys[pygame.K_a] and self.body[0].dx != self.distance:
            self.body[0].dx = -self.distance
            self.body[0].dy = 0
        
        #update body
        
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
        


class text:
    def __init__(self,window):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.window = window
    def draw(self):
        pass
s1 = Snake(30,5,0.15,0)
apple = []
score = 0
game = 1
x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
a1 = Apple(x_a,y_a,35)
apple.append(a1)
while game:
    window.fill("White")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:            exit()
    if keys[pygame.K_ESCAPE]:        exit()
    if collison(a1.x,a1.y,a1.rad,s1.body[0].x,s1.body[0].y,s1.rad):
        x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
        y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
        a1 = Apple(x_a,y_a,35)
        s1.krugovi += 1
        score+=1
    s1.move(keys)
    
    s1.draw(window)
    a1.draw(window)
    pygame.display.update()
    clock.tick(60)
    