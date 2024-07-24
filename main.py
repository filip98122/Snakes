import os
import pygame
import random
import math
import time
import json
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
        
        self.sprite_img1 = pygame.image.load('store.png')
        self.width1 = self.sprite_img.get_width()*self.scale
        self.height1 = self.sprite_img.get_height()*self.scale
        self.scaled_img1 = pygame.transform.scale(self.sprite_img1, (self.width1, self.height1))
        
        self.width = self.scaled_img1.get_width()
        self.height = self.scaled_img1.get_height()
    def draw(self,shop,game):
        if shop == 1:
            window.blit(self.scaled_img1,(0,0))
        if game == 1:
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
                    shutdown(info,score)
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
            shutdown(info,score)

            
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
        
    
    
    
    
    
class Storekeeper:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sprite_img = pygame.image.load('sopkeeper.png')
        self.width = self.sprite_img.get_width()*0.23
        self.height = self.sprite_img.get_height()*0.23
        self.scaled_img = pygame.transform.scale(self.sprite_img, (self.width, self.height))
    def draw(self,window):
        self.width = self.scaled_img.get_width()
        self.height =self.scaled_img.get_height()
        window.blit(self.scaled_img, (self.x - self.width/2, self.y - self.height/2))
        
shopk = Storekeeper(625,605)







class Button:
    def __init__(self,x,y,width,height,ID,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ID = ID
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 45)
        self.text = text
    def draw_m(self,window):
        if self.ID == "main_menu":
            pygame.draw.rect(window,"Black",pygame.Rect(self.x,self.y,self.width,self.height))
    def draw_s(self,window):
        if self.ID == "shop":
            pygame.draw.rect(window,"Black",pygame.Rect(self.x,self.y,self.width,self.height))
    def draw_t(self,window,main,shop):
        text_surface = self.myfont2.render(f"{self.text}", True, (255, 255, 255))
        window.blit(text_surface,(self.x,self.y))
        
        
l_buttons = []
button = Button(330,200,150,100,"main_menu","Play")
l_buttons.append(button)
button = Button(330,375,150,100,"main_menu","Shop")
l_buttons.append(button)
button = Button(40,175,150,100,"shop","Geon")
l_buttons.append(button)
button = Button(215,175,150,100,"shop","Blod")
l_buttons.append(button)
button = Button(390,175,150,100,"shop","Starter")
l_buttons.append(button)
button = Button(565,175,150,100,"shop","Fruit")
l_buttons.append(button)


class Text:
    def __init__(self,window):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 45)
        self.window = window
    def draw_score(self,kru,game_info,score):
        text_surface = self.myfont1.render(f"Score: {int(kru-5)}", True, (0, 0, 0))
        self.window.blit(text_surface,(10,10))
        hs = game_info["highscore"]
        if hs<score:
            hs = score
        text_surface1 = self.myfont1.render(f"Highscore: {int(hs)}", True, (0, 0, 0))
        self.window.blit(text_surface1,(10,30))
    def draw_button_text(self,window):
        text_surface = self.myfont.render(f"Main Menu", True, (255, 0, 0))
        self.window.blit(text_surface,(225,50))
        
s1 = Snake(25,5,100,100)
apple = []
score = 0
shop = 0
game = 1

def read(): # returns all gane info 
    f = open("test.json", "r")
    res = f.read()
    res = json.loads(res)
    f.close()
    return res
    
def write(info,score):
    hs = info["highscore"]
    if score>hs:
        info["highscore"] = score
    f = open("test.json", "w")
    info = json.dumps(info)
    f.write(info)
    f.close()


def shutdown(info,score):
    global shop
    global game
    global main_menu
    if score > info["highscore"]:
        write(info,score)
    game = 0
    main_menu = 1
    shop = 0

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


dict_1 = {
    "gold": 0,
    "highscore": 41,
    "upgrades": {
        "fruit": 0
    }
}

file = open("test.json","r")
info = json.loads(file.read())
file.close()


def save(stats):
    file = open("test.json","w")
    json_object = json.dumps(stats)
    file.write(json_object)
    file.close()



while True:
    if main_menu == 1:
        window.fill("Blue")
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
            l_buttons[i].draw_m(window)
        t1.draw_button_text(window)
        if wait >= 0:
            wait-=1
        if button_colision(150,100,307,200,mousePos,mouseState):
            game = 1
            main_menu = 0
            shop = 0
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
        if button_colision(150,100,307,375,mousePos,mouseState):
            game = 0
            main_menu = 0
            shop = 1
        for i in range(len(l_buttons)):
            if l_buttons[i].ID == "main_menu":
                l_buttons[i].draw_t(window,main_menu,shop)
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................

    if shop == 1:
        window.fill("White")
        b1.draw(shop,game)
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                shutdown(info,score)
                wait = 30
        if keys[pygame.K_ESCAPE]:
            shutdown(info,score)
            wait = 30
        shopk.draw(window)
        for i in range(len(l_buttons)):
            l_buttons[i].draw_s(window)
            
        for i in range(len(l_buttons)):
            if l_buttons[i].ID == "shop":
                l_buttons[i].draw_t(window,main_menu,shop)








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
        b1.draw(shop,game)
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                shutdown(info,score)
                wait = 30
        if keys[pygame.K_ESCAPE]:
            shutdown(info,score)
            wait = 30
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
        t1.draw_score(s1.krugovi,info,score)
    pygame.display.update()
    clock.tick(60)