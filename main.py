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
    
    if dist >= (r1 + r2 - (((r1+r2)/2)*0.2)):
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False
clock = pygame.time.Clock()
WIDTH,HEIGHT = 765,765
window = pygame.display.set_mode((WIDTH,HEIGHT))
def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False
    
class Backround:
    def __init__(self,window):
        self.window = window
        self.scale = 3.5
        self.sprite_img = pygame.image.load('gra.png')
        self.width = self.sprite_img.get_width()*self.scale
        self.height = self.sprite_img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.sprite_img, (self.width, self.height))
    def draw(self):
        self.width = self.scaled_img.get_width()
        self.height = self.scaled_img.get_height()
        window.blit(self.scaled_img, (0,0))
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
    def __init__(self,rad,krugovi,x,y):
        self.rad = rad
        self.krugovi = krugovi
        self.distance = 7
        self.speed = 5
        self.head_pos = []
        self.amount_to_track = 600
        self.body = [Part(x,y,self.rad,"head")]
        for i in range(600):
            self.head_pos.append([self.body[0].x,self.body[0].y])
        for i in range(krugovi-1):
            self.body.append(Part(x-self.distance*i,y,self.rad,"body"))
    def draw(self,window):
        for i in range(len(self.body)-1,-1,-1):
            self.body[i].draw(window)
    def move(self, keys):
        global started_moving
        tmp_start_x = self.body[0].x
        tmp_start_y = self.body[0].y
        
        if len(self.head_pos)>self.amount_to_track:
            del self.head_pos[0]
        for i in range(1,self.krugovi):
            self.body[i].x = self.head_pos[len(self.head_pos)-self.distance*i][0]
            self.body[i].y = self.head_pos[len(self.head_pos)-self.distance*i][1]
        for i in range(2,self.krugovi):
            if spawn_immunity<=0:
                if collison(self.body[0].x,self.body[0].y,self.rad,self.body[i].x,self.body[i].y,self.rad):
                    shutdown()
                    pass

        self.body[0].x += self.body[0].dx
        self.body[0].y += self.body[0].dy
        if keys[pygame.K_DOWN] and self.body[0].dy != -self.speed or keys[pygame.K_s] and self.body[0].dy != -self.speed:
            self.body[0].dx = 0
            self.body[0].dy = self.speed
        if keys[pygame.K_UP] and self.body[0].dy != self.speed or keys[pygame.K_w] and self.body[0].dy != self.speed:
            self.body[0].dx = 0
            self.body[0].dy = -self.speed
        if keys[pygame.K_RIGHT] and self.body[0].dx != -self.speed or keys[pygame.K_d] and self.body[0].dx != -self.speed:
            self.body[0].dx = self.speed
            self.body[0].dy = 0
        if keys[pygame.K_LEFT] and self.body[0].dx != self.speed or keys[pygame.K_a] and self.body[0].dx != self.speed:
            self.body[0].dx = -self.speed
            self.body[0].dy = 0
        if self.body[0].x < self.rad or self.body[0].x > WIDTH-self.rad or self.body[0].y < self.rad or self.body[0].y > HEIGHT-self.rad:
            shutdown()

            
        self.head_pos.append([self.body[0].x,self.body[0].y])
        if tmp_start_x != self.body[0].x or tmp_start_y != self.body[0].y:
            started_moving=True
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
        
        
class Button:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,window):
        pygame.draw.rect(window,"Black",pygame.Rect(self.x,self.y,self.width,self.height))
        
l_buttons = []
button = Button(307,200,150,100)
l_buttons.append(button)
button = Button(307,375,150,100)
l_buttons.append(button)

class Text:
    def __init__(self,window):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 45)
        self.window = window
    def draw_score(self,kru,score):
        text_surface = self.myfont1.render(f"Score: {int(kru-5)}", True, (0, 0, 0))
        self.window.blit(text_surface,(10,10))
        hs = read()
        if hs<score:
            hs = score
        text_surface1 = self.myfont1.render(f"Highscore: {int(hs)}", True, (0, 0, 0))
        self.window.blit(text_surface1,(10,30))
    def draw_button_text(self,window):
        text_surface = self.myfont.render(f"Main Menu", True, (255, 0, 0))
        self.window.blit(text_surface,(225,50))
        
        text_surface1 = self.myfont2.render(f"Play", True, (255, 255, 255))
        self.window.blit(text_surface1,(330,210))
        
        text_surface2 = self.myfont2.render(f"Shop", True, (255, 255, 255))
        self.window.blit(text_surface2,(330,385))
s1 = Snake(25,5,100,100)
apple = []
score = 0

game = 1

def read():
    f = open("test.txt", "r")
    highscore = f.read()
    hk = int(highscore)
    f.close()
    return hk
    
def write(highscore):
    f = open("test.txt", "w")
    f.write(str(highscore))
    hk = int(highscore)
    f.close()
    return hk

def shutdown():
    global game
    global main_menu
    hs = read()
    if score > hs:
        write(score)
    game = 0
    main_menu = 1

b1 = Backround(window)
t1 = Text(window)
x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
a1 = Apple(x_a,y_a,35)
apple.append(a1)
spawn_immunity = 300
started_moving = False
main_menu = 0
wait = 0




while True:
    if main_menu == 1:
        window.fill("White")
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                if wait <= 0:
                    exit()
                
        if keys[pygame.K_ESCAPE]:
            if wait <= 0:
                exit()
        for i in range(len(l_buttons)):
            l_buttons[i].draw(window)
        t1.draw_button_text(window)
        if wait >= 0:
            wait-=1
        if button_colision(150,100,307,200,mousePos,mouseState):
            game = 1
            main_menu = 0
            spawn_immunity = 300
            started_moving = False
            s1.body[0].x = 100
            s1.body[0].y = 100
            s1.krugovi = 5
            s1.body[0].dx = 0
            s1.body[0].dy = 0
            score = 0
            del s1.body
            s1.body = [(Part(100,100,25,"head"))]
            for i in range(600):
                s1.head_pos.append([s1.body[0].x,s1.body[0].y])
            for i in range(s1.krugovi-1):
                s1.body.append((Part(100,100,25,"body")))

#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
    if game == 1:
        if started_moving == True:
            spawn_immunity -=1
        window.fill("White")
        b1.draw()
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                shutdown()
                wait = 90
        if keys[pygame.K_ESCAPE]:
            shutdown()
            wait = 90
        if collison(a1.x,a1.y,a1.rad,s1.body[0].x,s1.body[0].y,s1.rad):
            x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
            y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
            for i in range(s1.krugovi):
                if collison(x_a,y_a,a1.rad,s1.body[i].x,s1.body[i].y,s1.rad):
                    x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
                    y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
            a1 = Apple(x_a,y_a,35)
            s1.krugovi += 1
            s1.body.append(Part(-50,-50,s1.rad,"body"))
            s1.amount_to_track+=60
            score+=1
        s1.move(keys)
        s1.draw(window)
        a1.draw(window)
        t1.draw_score(s1.krugovi,score)
    pygame.display.update()
    clock.tick(60)