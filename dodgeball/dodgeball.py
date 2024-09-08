import pygame
from pygame.locals import *
import os
pygame.font.init()
WIDTH,HEIGHT=700,500
Screen=pygame.display.set_mode((WIDTH,HEIGHT))
#colours
green=(0,255,0)
black=(0,0,0)
red=(255,0,0)
yellow=(0,125,125)
border=pygame.Rect(WIDTH//2,0,10,HEIGHT)
#variables
spd=10
ball=7
max=5
pw,ph=40,50
#font
hf=pygame.font.SysFont('comicsans',35)
wnf=pygame.font.SysFont('Alberobelloserif',50)
p1=pygame.image.load("dodgeball p1.png")
p2=pygame.image.load("dodgeball p2.png")
arena=pygame.transform.scale(pygame.image.load("dodgeball arena.jpg"),(WIDTH,HEIGHT))
h1=5
h2=5
class pm(pygame.sprite.Sprite):
    def __init__(self,image,angle,x,y):
        super().__init__()
        self.image=pygame.transform.rotate(pygame.transform.scale(image,(pw,ph)),angle)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def horizontal(self,vel,player):
        self.rect.x+=vel
        if player==1:
            if self.rect.left<=0 or self.rect.right>=border.left:
                self.rect.move_ip(-vel,0)
        if player==2:
            if self.rect.left<=border.right or self.rect.right>=WIDTH:
                self.rect.move_ip(-vel,0)  
    def vertical(self,vel):
        self.rect.move_ip(0,vel)
        if self.rect.top<=0 or self.rect.bottom>=500:
            self.rect.move_ip(0,-vel)
pl1=pm(p1,0,100,200)
pl2=pm(p2,0,600,200)
sprites=pygame.sprite.Group()
sprites.add(pl1)
sprites.add(pl2)
run=True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    sprites.draw(Screen)
    pygame.display.update()
pygame.quit()
