import engine
import texts
import pygame
import os
import json
import sys

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Kamikaze")


class Story:
    intro={"text":"","wait":0}
    end=False
    def load():
        engine.event()
        while True:
            if Story.end:
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
            Story.end=True

class Story2:
    intro={"text":"Bölüm 1"}
    def load():
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
    def __init__(self):
        self.intro={"text":"Bölüm 2"}
    def load():
        print("ok")
        sys.exit()

story=engine.Level(Story,screen)
story2=engine.Level(Story2,screen)
story3=engine.Level(Story3,screen)

#story.load()
story3.load()
