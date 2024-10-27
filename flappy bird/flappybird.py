import pygame
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500,700))
pygame.display.set_caption("Flappy Bird")
font=pygame.font.SysFont("Aptos Black",15)
#defining game variables
groundscroll=0
scrollspeed=4
flying=False
gameover=False
pipegap=125
pipefrequency=1500
lastpipe=pygame.time.get_ticks()-pipefrequency
score=0
passpipe=False
bg=pygame.image.load("bg.png")
ground=pygame.image.load("ground")
restart=pygame.image.load("restart.png")
#function for text
def text(txt,font,colour,x,y):
    t=font.render(txt,True,colour)
    screen.blit(t,(x,y))
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for I in range(1,4):
            img=pygame.image.load(f"bird{I}.png")
            self.images.append(img)
