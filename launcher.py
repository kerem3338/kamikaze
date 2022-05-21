"""
Game by Zoda

Source: Wikipedia
"""
import engine
import texts
import pygame
import os
import json
import sys

pygame.init()
Resources = engine.Resources("resources")
Levels=engine.LevelManager()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Kamikaze")
pygame.display.set_icon(pygame.image.load(Resources.getfile("icon.png")))

class Story:
    intro={"text":"","wait":0}
    def __init__(self):
        self.end=False
    def load(self):
        engine.event()
        while True:
            if self.end:
                engine.kill_event()
                break
            
            else: pass
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            
            screen.fill(engine.bg_color)
            story_text=engine.Text(texts.texts["story_text_1"],(screen.get_width()//2,screen.get_height()//2))
            story_text.render(screen)
            pygame.display.update()
            pygame.time.delay(1000)
            engine.darken(screen)
            story_text=engine.Text(texts.texts["story_text_2"],(screen.get_width()//2,screen.get_height()//2))
            story_text.render(screen)
            pygame.display.update()
            pygame.time.delay(1000)
            engine.darken(screen)
            self.end=True

class Story2:
    intro={"text":"Bölüm 1"}
    def __init__(self):
        pass
    def load(self):
        pl=engine.Player(screen)
    
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_LEFT:
                        pl.move("left",16)
                    if i.key == pygame.K_RIGHT:
                        pl.move("right",16)
            
            if pl.check_border_collision(False):
                break
            
            pl.check_border_collision()
            screen.fill(engine.bg_color)
            pl.draw()
            pygame.display.update()
            pygame.time.delay(10)
            pl.move("down",0.5)

            
class Story3:
    intro={
        "text":"Bölüm 2",
    }
    def __init__(self):
       pass

    def load_once(self):
        self.bg=pygame.image.load(Resources.getfile("ship.png"))
        self.bg=pygame.transform.scale(self.bg,(screen.get_width(),screen.get_height()))

    def load(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill((0,0,0))
            screen.blit(self.bg,(100,0))
            pygame.display.update()
        

story=engine.Level(Story,screen)
story2=engine.Level(Story2,screen)
story3=engine.Level(Story3,screen)

Levels.add(story)
Levels.add(story2)
Levels.add(story3)
Levels.skip([story,story2])
Levels.start()