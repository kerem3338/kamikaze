import json
import os
import pygame
import inspect
import time
import sys
from pathlib import Path


pygame.init()

bg_color = pygame.Color("black")
global current_level
current_level = ""

class Resources:
    def __init__(self,dir:os.path):
        self.dir=dir
        self.SOURCEPATH = Path(__file__).parents[0]

    def source_path(self,path):
        return os.path.abspath(os.path.join(self.SOURCEPATH, path))
    def getfile(self,filename):
        if filename in os.listdir(self.dir):
            return open(os.path.join(self.dir,filename),'r')
        else:
            raise FileNotFoundError("File not found in Resources directory: "+filename)
class Text:
    def __init__(self, text, pos, font_size=20, color=pygame.Color("white")):
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = self.pos
    def render(self,screen:pygame.Surface):
        screen.blit(self.surface,self.rect)


class Level:
    def __init__(self,level,screen:pygame.Surface):
        self.level = level
        self.screen = screen
        self.load()

    def load_intro(self):
        if self.level.__dict__.get("intro"):
            t=Text(self.level.intro["text"],(self.screen.get_width()//2,self.screen.get_height()//2))
            timer_start=time.time()
           
            while True:
                if time.time()-timer_start>=2:
                    break
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if i.type == pygame.KEYDOWN:
                        if i.key == pygame.K_RETURN:
                            self.load()
                self.screen.fill(bg_color)
                t.render(self.screen)
                pygame.display.update()
                pygame.time.delay(10)
                pygame.display.flip()
                
            print("Level intro finished")
        else:
            print("No intro for this level")
    def load(self):
        self.load_intro()
        self.level.load()
        
	
class Json:
    def __init__(self,file:os.path):
        self.filename=file
        self.file=open(file,"w",encoding="utf-8")
        self.json_data=json.load(self.file.read())

    def delete(self,object):
        del self.json_data[object]
        self.file.seek(0)
        self.truncate()
        self.file.write(json.dumps(self.json_data))

    def update(self,object,value):
        self.json_data[object]=value
        self.file.seek(0)
        self.truncate()
        self.file.write(json.dumps(self.json_data))
    def close(self):
        self.file.close()


class Player:
    def __init__(self,screen):
        self.screen=screen
        self.player_data={
            "location": {"x": 0, "y": 0},
            "inventory": [],
            "health": 100,
            "max_health": 100,
            
        }
        self.player=pygame.Rect(self.player_data["location"]["x"],self.player_data["location"]["y"],32,32)

    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),self.player)

    def update_rect(self):
        self.player=pygame.Rect(self.player_data["location"]["x"],self.player_data["location"]["y"],32,32)

    def check_border_collision(self):
        if self.player.x < 0:
            self.player.x = 0
        elif self.player.x > self.screen.get_width() - self.player.width:
            self.player.x = self.screen.get_width() - self.player.width
        if self.player.y < 0:
            self.player.y = 0
        elif self.player.y > self.screen.get_height() - self.player.height:
            self.player.y = self.screen.get_height() - self.player.height

    def move(self,direction):
        if direction=="up":
            self.player_data["location"]["y"]-=32
        elif direction=="down":
            self.player_data["location"]["y"]+=32
        elif direction=="left":
            self.player_data["location"]["x"]-=32
        elif direction=="right":
            self.player_data["location"]["x"]+=32
        self.update_rect()
class Solid:
    def __init__(self,x,y,width,height,color:pygame.Color):
        self.solid=pygame.Rect(x,y,width,height)
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self,screen:pygame.Surface):
        pygame.draw.rect(screen,self.color,self.solid)

    def update_rect(self):
        self.solid=pygame.Rect(self.x,self.y,self.width,self.height)

    def check_collision(self,player:pygame.Rect):
        if player.colliderect(self.solid):
            return True
        else:
            return False
class Entity:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    
    def draw(self,screen:pygame.Surface):
        pygame.draw.rect(screen,self.color,self.rect)

    def update_rect(self):
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
