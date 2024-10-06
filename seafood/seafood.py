import pygame
from pygame.locals import *
import random
import time
score=0
pygame.init()
font=pygame.font.SysFont("Algerian",50)
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
for I in range(20):
    item=food(random.choice(fd))
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    edibles.add(item)
    all.add(item)
for I in range(30):
    item=plasticbag()
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    plastic.add(item)
    all.add(item)
run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
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
    
    bg=pygame.image.load("oceanbg.jpg")
    bg=pygame.transform.scale(bg,(700,500))
    screen.blit(bg,(0,0))
    all.draw(screen)
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

for I in range(50):
    item=plasticbag()
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    edibles.add(item)
    all.add(item)
