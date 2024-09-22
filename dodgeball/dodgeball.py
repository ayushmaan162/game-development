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
wnf=pygame.font.SysFont('Alberobelloserif',70)
p1=pygame.image.load("dodgeball p1.png")
p2=pygame.image.load("dodgeball p2.png")
arena=pygame.transform.scale(pygame.image.load("dodgeball arena.jpg"),(WIDTH,HEIGHT))
border=pygame.Rect(350,0,10,500)
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
pl1=pm(p1,0,100,350)
pl2=pm(p2,0,600,350)
sprites=pygame.sprite.Group()
sprites.add(pl1)
sprites.add(pl2)
run=True
def bg():
    Screen.blit(arena,(0,0))
    pygame.draw.rect(Screen,"red",border)
    pl1text=hf.render("Health:"+str(h1),1,"green")
    pl2text=hf.render("Health:"+str(h2),2,"green")
    Screen.blit(pl1text,(100,10))
    Screen.blit(pl2text,(460,10))
pl1ball=[]
pl2ball=[]   
def bal():
    for ball in pl1ball:
        pygame.draw.circle(Screen,"red",(ball["x"],ball["y"]),10)
        ball["x"]+=5
    for ball in pl2ball:
        pygame.draw.circle(Screen,"yellow",(ball["x"],ball["y"]),10)
        ball["x"]-=5
pl1_hit=pygame.USEREVENT+1
pl2_hit=pygame.USEREVENT+2
def bctrl():
    global h1,h2
    for ball in pl2ball:
        ball_rect=pygame.Rect(ball["x"],ball["y"],10,10)
        if pl1.rect.colliderect(ball_rect):
            h1-=1
            pl2ball.remove(ball)
        elif ball["x"]<0:
            pl2ball.remove(ball)
    for ball in pl1ball:
        ball_rect=pygame.Rect(ball["x"],ball["y"],10,10)
        if pl2.rect.colliderect(ball_rect):
            pygame.event.post(pygame.event.Event(pl2_hit))
            pl1ball.remove(ball)
        elif ball["x"]<0:
            pl1ball.remove(ball)
    for b1 in pl1ball:
        b1_rect=pygame.Rect(b1["x"],b1["y"],10,10)
        for b2 in pl2ball:
            b2_rect=pygame.Rect(b2["x"],b2["y"],10,10)
            if b1_rect.colliderect(b2_rect):
                pl1ball.remove(b1)
                pl2ball.remove(b2)
def winner(txt):
    text=wnf.render(txt,1,"lime")
    Screen.blit(text,(200,250))
    pygame.display.update()
    pygame.time.delay(5000)
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type==KEYDOWN:
            if event.key==K_LCTRL:
                ball={'x':pl1.rect.x+pl1.rect.width,'y':pl1.rect.y+pl1.rect.height//2}
                pl1ball.append(ball)
            if event.key==K_RCTRL:
                ball={'x':pl2.rect.x,'y':pl2.rect.y+pl2.rect.height//2}
                pl2ball.append(ball)
        if event.type==pl1_hit:
            h1-=1
        if event.type==pl2_hit:
            h2-=1
    key=pygame.key.get_pressed()
    if key[K_a]:
        pl1.horizontal(-1,1)
    if key[K_d]:
        pl1.horizontal(1,1)
    if key[K_w]:
        pl1.vertical(-1)
    if key[K_s]:
        pl1.vertical(1)
    #player2
    if key[K_LEFT]:
        pl2.horizontal(-1,2)
    if key[K_RIGHT]:
        pl2.horizontal(1,2)
    if key[K_UP]:
        pl2.vertical(-1)
    if key[K_DOWN]:
        pl2.vertical(1)
    bg()
    sprites.draw(Screen)
    bal()
    bctrl()
    if h1<=-1:
        wntxt="PLAYER 2 WINS"
        winner(wntxt)
        run=False
    if h2<=-1:
        wntxt="PLAYER 1 WINS"
        winner(wntxt)
        run=False
    pygame.display.update()
pygame.quit()
