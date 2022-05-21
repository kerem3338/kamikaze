import engine
import pygame
import os
import json
import sys

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Kamikaze")

pl=engine.Player(screen)
e1=engine.Entity(0,0,32,32,(255,0,0))
s1=engine.Solid(32,0,32,32,(0,255,0))
class Level1:
    intro={"text":"Menü"}
    def load():
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_UP:
                        pl.move("up")
                    if i.key == pygame.K_DOWN:
                        pl.move("down")
                    if i.key == pygame.K_LEFT:
                        pl.move("left")
                    if i.key == pygame.K_RIGHT:
                        pl.move("right")        

            pl.check_border_collision()
            screen.fill(engine.bg_color)
            pl.draw()
            e1.draw(screen)
            s1.draw(screen)
            

            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(10)
lv=engine.Level(Level1,screen)
while True:
    lv.load()