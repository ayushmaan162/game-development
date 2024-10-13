import pygame
from pygame.locals import *
import random
import time
score=0
pygame.init()
font=pygame.font.SysFont("Algerian",50)
font2=pygame.font.SysFont("Adobe Garamond Pro",25)
text=font.render("SCORE:"+str(score),True,"dark blue")
screen=pygame.display.set_mode((700,500))
class fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fish.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect=self.image.get_rect()
class plasticbag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plasticbag.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
class food(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
fd=["lilfish.png","plankton.png","seaweed.png"]
edibles=pygame.sprite.Group()
plastic=pygame.sprite.Group()
all=pygame.sprite.Group()
mfish=fish()
all.add(mfish)
for I in range(15):
    item=food(random.choice(fd))
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    edibles.add(item)
    all.add(item)
for I in range(18):
    item=plasticbag()
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    plastic.add(item)
    all.add(item)
run=True
clock=pygame.time.Clock()
start=time.time()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    duration=time.time()-start
    if duration>=30:
        if score>=10:
            text=font.render("YOU WIN!!",True,"light green")
        else:
            text=font.render("YOU LOSE!!",True,"Red")
        screen.blit(text,(250,75))
    else:
        bg=pygame.image.load("oceanbg.jpg")
        bg=pygame.transform.scale(bg,(700,500))
        screen.blit(bg,(0,0))
        all.draw(screen)
        dis=font2.render("time remaining:"+str(30-int(duration)),True,"purple")
        screen.blit(dis,(530,10))
        khold=pygame.key.get_pressed()
        if khold[K_UP]:
            if mfish.rect.y>0:
                mfish.rect.y-=8
        if khold[K_DOWN]:
            if mfish.rect.y<400:
                mfish.rect.y+=8
        if khold[K_LEFT]:
            if mfish.rect.x>0:
                mfish.rect.x-=8
        if khold[K_RIGHT]:
            if mfish.rect.x<600:
                mfish.rect.x+=8
        #checking collision
        elist=pygame.sprite.spritecollide(mfish,edibles,True)
        plist=pygame.sprite.spritecollide(mfish,plastic,True)
        for I in elist:
            score+=1
            text=font.render("SCORE:"+str(score),True,"dark blue")
        for R in plist:
            score-=1
            text=font.render("SCORE:"+str(score),True,"dark blue")
        screen.blit(text,(250,10))
    pygame.display.update()

pygame.quit()

