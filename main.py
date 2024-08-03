import os
import pygame
import random
import math
import time
import json
pygame.init()
pygame.mixer.init()
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
    
sound0 = pygame.mixer.Sound('game1.mp3')
sound1 = pygame.mixer.Sound('Eat_apple.wav')
sound2 = pygame.mixer.Sound('game_music.wav')
    
    
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
        
        self.sprite_img2 = pygame.image.load('snakegame.png')
        self.width2 = self.sprite_img.get_width()*self.scale
        self.height2 = self.sprite_img.get_height()*self.scale
        self.scaled_img2 = pygame.transform.scale(self.sprite_img2, (self.width2, self.height2))
        
        self.width2 = self.scaled_img2.get_width()
        self.height2 = self.scaled_img2.get_height()
        
        self.width1 = self.scaled_img1.get_width()
        self.height1 = self.scaled_img1.get_height()
    def draw(self,shop,game):
        if shop == 1:
            window.blit(self.scaled_img1,(0,0))
        if shop == 0 and game == 0:
            window.blit(self.scaled_img2, (-10 ,0))
        if game == 1:
            self.width = self.scaled_img.get_width()
            self.height = self.scaled_img.get_height()
            window.blit(self.scaled_img, (0,0))
            
            
            
            
            
            
            
class Part:
    def __init__(self,x,y,rad,id):
        self.x = x
        self.y = y
        self.rad = rad
        self.scale= 0.085
        self.sprite_img = pygame.image.load('ghae.png')
        self.width = self.sprite_img.get_width()*self.scale
        self.height = self.sprite_img.get_height()*self.scale
        self.scaled_img = pygame.transform.scale(self.sprite_img, (self.width, self.height))
        self.dx = 0
        self.dy = 0
        self.id = id
    def draw(self,window,color,color1):
        info = read()
        if info["skins"]["geon"] == 2:
            pygame.draw.circle(window,pygame.Color("White"),(self.x,self.y),25)
            pygame.draw.circle(window,pygame.Color("Red"),(self.x,self.y),15)
            pygame.draw.circle(window,pygame.Color("White"),(self.x,self.y),5)
            
        if info["skins"]["blod"] == 2:
            pygame.draw.circle(window,pygame.Color(229,184,11),(self.x,self.y),25)
            pygame.draw.circle(window,pygame.Color(0,0,125),(self.x,self.y),15)
            
            
        if info["skins"]["basic"] == 2:
            pygame.draw.circle(window,pygame.Color(0,235,0),(self.x,self.y),25)
            pygame.draw.circle(window,pygame.Color(0,75,0),(self.x,self.y),15)
        if info["skins"]["geon"] != 2 and info["skins"]["blod"] != 2 and info["skins"]["basic"] != 2:
            window.blit(self.scaled_img, (self.x-self.rad,self.y-self.rad))
        if self.id == "head":
            pygame.draw.circle(window,pygame.Color(0,0,0),(self.x,self.y-7),5)
            pygame.draw.circle(window,pygame.Color(0,0,0),(self.x,self.y+7),5)
                
                
                
                
                
                
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
            self.body[i].draw(window,"Yellow",(255,100,10))
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
                    shutdown(info)
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
            shutdown(info)

            
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
    def __init__(self,x,y,width,height,ID,text,cost,reward,type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ID = ID
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 45)
        self.text = text
        self.cost = cost
        self.reward = reward
        self.type = type
        self.ux = 0
        self.uy = 0
    def draw_m(self,window):
        if self.ID == "main_menu":
            pygame.draw.rect(window,"Black",pygame.Rect(self.x,self.y,self.width,self.height))
    def draw_s(self,window):
        if self.ID == "shop":
            pygame.draw.rect(window,"Black",pygame.Rect(self.x,self.y,self.width,self.height))
    def draw_d(self,window):
        if self.ID == "dressing_room":
            pygame.draw.rect(window,"Black",pygame.Rect(self.x,self.y,self.width,self.height))
    def draw_t(self,window,main,shop):
        info = read()
        self.scale = 0.25
        self.scale1 = 0.2
        self.sprite_img = pygame.image.load('check.png')
        self.width1 = self.sprite_img.get_width()*self.scale
        self.height1 = self.sprite_img.get_height()*self.scale1
        self.scaled_img1 = pygame.transform.scale(self.sprite_img, (self.width1, self.height1))
        
        
        
        if self.width == 150:
            self.ux = 23
        if self.height == 100:
            self.uy = 15
        if self.text == "<" or self.text == ">":
            text_surface = pygame.font.SysFont('Comic Sans MS', 125).render(f"{self.text}", True, (255, 255, 255))
            window.blit(text_surface,(self.x+15,self.y-50))
        else:
            text_surface = self.myfont2.render(f"{self.text}", True, (255, 255, 255))
            window.blit(text_surface,(self.x+self.ux,self.y+self.uy))
        if shop == 1:
            if self.cost != 0:
                if self.type == "skin":
                    text_surface1 = self.myfont2.render(f"{self.cost}", True, (255, 255, 255))
                    window.blit(text_surface1,(self.x+self.ux+25,self.y+self.uy+175))
                    if info["skins"][self.reward] != 0:
                        window.blit(self.scaled_img1,(self.x+self.width//4,self.y+self.height*3))
                else:
                    text_surface1 = self.myfont2.render(f"{self.cost}", True, (255, 255, 255))
                    window.blit(text_surface1,(self.x+self.ux+25,self.y+self.uy+100))
                    if info["upgrades"][self.reward] != 0:
                        window.blit(self.scaled_img1,(self.x+self.width//4,self.y+self.height*2))
        self.ux = 0
        self.uy = 0
        



l_buttons = []
button = Button(75,630,150,100,"main_menu","Play",0,"","")
l_buttons.append(button)
button = Button(575,630,150,100,"main_menu","Shop",0,"","")
l_buttons.append(button)
button = Button(40,175,150,100,"shop","Flame",150,"geon","skin")
l_buttons.append(button)
button = Button(215,175,150,100,"shop","Blod",150,"blod","skin")
l_buttons.append(button)
button = Button(390,175,150,100,"shop","Basic",50,"basic","skin")
l_buttons.append(button)
button = Button(565,175,150,100,"shop","Fruit",50,"fruit","upgrade")
l_buttons.append(button)
button = Button(40,575,325,100,"shop","Dressing room",0,"","")
l_buttons.append(button)
button = Button(40,325,75,100,"dressing_room","<",0,"","")
l_buttons.append(button)
button = Button(640,325,75,100,"dressing_room",">",0,"","")
l_buttons.append(button)
button = Button(265,450,150,100,"dressing_room","Equip",0,"","")
l_buttons.append(button)



class Text:
    def __init__(self,window):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 45)
        self.window = window
    def draw_score(self,kru,game_info,score):
        text_surface = self.myfont1.render(f"Score: {score}", True, (0, 0, 0))
        self.window.blit(text_surface,(10,10))
        hs = game_info["highscore"]
        if hs<score:
            hs = score
        text_surface1 = self.myfont1.render(f"Highscore: {int(hs)}", True, (0, 0, 0))
        self.window.blit(text_surface1,(10,30))
    def draw_button_text(self,window):
        text_surface = self.myfont.render(f"Main Menu", True, (255, 0, 0))
        self.window.blit(text_surface,(225,0))
        
s1 = Snake(25,5,100,100)
apple = []
score = 0
shop = 0
game = 1

def draw_samps(samp,color,color1,color2):
        pygame.draw.circle(window,pygame.Color(color),(340,375),25)
        pygame.draw.circle(window,pygame.Color(color1),(340,375),15)
        if samp == 0:
                pygame.draw.circle(window,pygame.Color(color2),(340,375),5)

def draw_samples(x,y,color,color1,color2,rad,third):
    pygame.draw.circle(window,pygame.Color(color),(x,y),rad)
    pygame.draw.circle(window,pygame.Color(color1),(x,y),rad-10)
    if third == True:
            pygame.draw.circle(window,pygame.Color(color2),(x,y),rad-20)

def write_upgrades(info,reward):
    info["upgrades"][reward] = 1
    f = open("test.json", "w")
    info = json.dumps(info)
    f.write(info)
    f.close()


def write_skins(info,reward):
    info["skins"][reward] = 1
    f = open("test.json", "w")
    info = json.dumps(info)
    f.write(info)
    f.close()



def read(): # returns all gane info 
    f = open("test.json", "r")
    res = f.read()
    res = json.loads(res)
    f.close()
    return res
    
def write(info,score,gold):
    global minus
    hs = info["highscore"]
    if score*(info["upgrades"]['fruit']+1)>hs:
        info["highscore"] = score
    info["gold"] += (score-minus)
    minus = 0
    f = open("test.json", "w")
    info = json.dumps(info)
    f.write(info)
    f.close()


def shutdown(info):
    global sound1
    global sound0
    global shop
    global game
    global main_menu
    global score
    global dressing_room
    write(info,score,info['gold'])
    score = 0
    game = 0
    main_menu = 1
    dressing_room = 0
    shop = 0
    sound0.stop()
    sound1.stop()


#sound0 = pygame.mixer.Sound('sci_fi.wav')
#sound1 = pygame.mixer.Sound('Eat_apple.wav')
#sound2 = pygame.mixer.Sound('game_music.wav')

def not_bought(window):
    myfont = pygame.font.SysFont('Comic Sans MS', 45)
    text_surface = myfont.render(f"Not Bought", True, (255, 255, 255))
    window.blit(text_surface,(240,600))

SOUND = 1
count = 0
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
dressing_room = 0
sample = 0

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


minus = 0
while True:
    if main_menu == 1:
        if SOUND == 1:
            sound2.play()
        window.fill("Blue")
        b1.draw(shop,game)
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
        if button_colision(l_buttons[0].width,l_buttons[0].height,l_buttons[0].x,l_buttons[0].y,mousePos,mouseState):
            game = 1
            main_menu = 0
            shop = 0
            dressing_room = 0
            spawn_immunity = 300
            started_moving = False
            s1.body[0].x = 100
            s1.body[0].y = 100
            s1.krugovi = 5
            s1.body[0].dx = 0
            s1.body[0].dy = 0
            score = 0
            sound1.stop()
            sound2.stop()
            del s1.body
            s1.body = [(Part(100,100,25,"head"))]
            for i in range(600):
                s1.head_pos.append([s1.body[0].x,s1.body[0].y])
            for i in range(s1.krugovi-1):
                s1.body.append((Part(100,100,25,"body")))
        if button_colision(l_buttons[1].width,l_buttons[1].height,l_buttons[1].x,l_buttons[1].y,mousePos,mouseState):
            game = 0
            main_menu = 0
            shop = 1
            dressing_room = 0
        for i in range(len(l_buttons)):
            if l_buttons[i].ID == "main_menu":
                l_buttons[i].draw_t(window,main_menu,shop)
        minus = 0
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................

    if shop == 1:
        if SOUND == 1:
            sound2.play()
        window.fill("White")
        b1.draw(shop,game)
        text_surface = pygame.font.SysFont("Comic Sans MS", 25).render(f'Gold: {info["gold"]-minus}', True, (0, 0, 0))
        window.blit(text_surface,(10,10))
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        if wait <= 0:
            for event in events:
                if event.type == pygame.QUIT:
                    shutdown(info)
                    shutdown(info)
                    sound0.stop()
                    sound1.stop()
                    wait = 15
            if keys[pygame.K_ESCAPE]:
                shutdown(info)
                sound0.stop()
                sound1.stop()
                wait = 15
        shopk.draw(window)
        for i in range(len(l_buttons)):
            l_buttons[i].draw_s(window)
        if wait >= 0:
            wait-=1
            
        

        draw_samples(l_buttons[2].x+l_buttons[2].width//2,l_buttons[2].y+l_buttons[2].height*1.5,(255,255,255),(255,0,0),(255,255,255),s1.rad,True)
        draw_samples(l_buttons[3].x+l_buttons[3].width//2,l_buttons[3].y+l_buttons[3].height*1.5,(229,184,11),(0,0,125),(255,255,255),s1.rad,False)
        draw_samples(l_buttons[4].x+l_buttons[4].width//2,l_buttons[4].y+l_buttons[4].height*1.5,(0,235,0),(0,75,0),(255,255,255),s1.rad,False)

        for i in range(len(l_buttons)):
            if l_buttons[i].ID == "shop":
                l_buttons[i].draw_t(window,main_menu,shop)
                if button_colision(l_buttons[i].width,l_buttons[i].height,l_buttons[i].x,l_buttons[i].y,mousePos,mouseState):
                    if l_buttons[i].type == "skin" or l_buttons[i].type == "upgrade":
                        info = read()
                        gold = info["gold"]
                        if l_buttons[i].type == "skin":
                            if info["skins"][l_buttons[i].reward] == 0:
                                if gold-minus >= l_buttons[i].cost:
                                    minus+=l_buttons[i].cost
                                    write_skins(info,l_buttons[i].reward)
                                
                                
                        else:
                            if info["upgrades"][l_buttons[i].reward] == 0:
                                if gold-minus >= l_buttons[i].cost:
                                    minus+=l_buttons[i].cost
                                    write_upgrades(info,l_buttons[i].reward)
                        
                    
                    
                    else:
                        game = 0
                        main_menu = 0
                        shop = 0
                        dressing_room = 1

    if dressing_room == 1:
        if SOUND == 1:
            sound2.play()
        window.fill("White")
        b1.draw(dressing_room,game)
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                score = 0
                game = 0
                main_menu = 0
                dressing_room = 0
                shop = 1
                wait = 30
        if keys[pygame.K_ESCAPE]:
            score = 0
            game = 0
            main_menu = 0
            dressing_room = 0
            shop = 1
            wait = 30
        for i in range(len(l_buttons)):
            l_buttons[i].draw_d(window)
        if wait >= 0:
            wait-=1
        for i in range(len(l_buttons)):
            if l_buttons[i].ID == "dressing_room":
                l_buttons[i].draw_t(window,main_menu,shop)
        if wait <= 0:
            if button_colision(l_buttons[7].width,l_buttons[7].height,l_buttons[7].x,l_buttons[7].y,mousePos,mouseState):
                sample-=1
                wait = 30
            if button_colision(l_buttons[8].width,l_buttons[8].height,l_buttons[8].x,l_buttons[8].y,mousePos,mouseState):
                sample+=1
                wait = 30
            if button_colision(l_buttons[9].width,l_buttons[9].height,l_buttons[9].x,l_buttons[9].y,mousePos,mouseState):
                wait = 30
                if sample == 0:
                    info = read()
                    if info["skins"]["geon"] == 1:
                        info["skins"]["geon"] = 2
                        
                        if info["skins"]["blod"] == 2:
                            info["skins"]["blod"] = 1
                            
                        if info["skins"]["basic"] == 2:
                            info["skins"]["basic"] = 1
                            
                        f = open("test.json", "w")
                        info = json.dumps(info)
                        f.write(info)
                        f.close()
                        
                    else:
                        info = read()
                        if info["skins"]["geon"] == 2:
                            info["skins"]["geon"] = 1
                            f = open("test.json", "w")
                            info = json.dumps(info)
                            f.write(info)
                            f.close()
                        
                if sample == 1:
                    info = read()
                    if info["skins"]["blod"] == 1:
                        info["skins"]["blod"] = 2
                        
                        if info["skins"]["geon"] == 2:
                            info["skins"]["geon"] = 1
                            
                        if info["skins"]["basic"] == 2:
                            info["skins"]["basic"] = 1
                            
                        f = open("test.json", "w")
                        info = json.dumps(info)
                        f.write(info)
                        f.close()
                    
                    else:
                        info = read()
                        if info["skins"]["blod"] == 2:
                            info["skins"]["blod"] = 1
                            f = open("test.json", "w")
                            info = json.dumps(info)
                            f.write(info)
                            f.close()
                        
                if sample == 2:
                    info = read()
                    if info["skins"]["basic"] == 1:
                        info["skins"]["basic"] = 2
                        
                        if info["skins"]["blod"] == 2:
                            info["skins"]["blod"] = 1
                            
                        if info["skins"]["geon"] == 2:
                            info["skins"]["geon"] = 1
                            
                        
                        f = open("test.json", "w")
                        info = json.dumps(info)
                        f.write(info)
                        f.close()
                        
                    else:
                        info = read()
                        if info["skins"]["basic"] == 2:
                            info["skins"]["basic"] = 1
                            f = open("test.json", "w")
                            info = json.dumps(info)
                            f.write(info)
                            f.close()
        
        if sample == 0:
            info = read()
            draw_samps(sample,(255,255,255),(255,0,0),(255,255,255))
            if info["skins"]["geon"] == 0:
                not_bought(window)
        if sample == 1:
            info = read()
            draw_samps(sample,(229,184,11),(0,0,125),(255,255,255))
            if info["skins"]["blod"] == 0:
                not_bought(window)
        if sample == 2:
            info = read()
            draw_samps(sample,(0,235,0),(0,75,0),(255,255,255))
            if info["skins"]["basic"] == 0:
                not_bought(window)
        if sample == -1:
            sample = 2
        if sample == 3:
            sample = 0
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
#.............................
    if game == 1:
        if count==0:
            if SOUND == 1:
                sound0.play()
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
                shutdown(info)
                wait = 30
        if keys[pygame.K_ESCAPE]:
            shutdown(info)
            wait = 30
            
            
        # Apple collision
        
        if collison(a1.x,a1.y,a1.rad,s1.body[0].x,s1.body[0].y,s1.rad):
            x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
            y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
            
            sound0.stop()
            sound2.stop()
            sound1.play()
            count = 5
            for i in range(s1.krugovi):
                if collison(x_a,y_a,a1.rad,s1.body[i].x,s1.body[i].y,s1.rad):
                    x_a = random.randint(s1.rad+s1.rad//2,WIDTH-s1.rad-s1.rad//2)
                    y_a = random.randint(s1.rad+s1.rad//2,HEIGHT-s1.rad-s1.rad//2)
            
            a1 = Apple(x_a,y_a,35)
            s1.krugovi += 1
            s1.body.append(Part(-50,-50,s1.rad,"body"))
            s1.amount_to_track+=60
            info = read()
            score+=(1*(info["upgrades"]['fruit']+1))
        if count!=0:
            count-=1
        s1.move(keys)
        s1.draw(window)
        a1.draw(window)
        t1.draw_score(s1.krugovi,info,score)
    pygame.display.update()
    clock.tick(60)