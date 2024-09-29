import pygame
from pygame.locals import *
import random
import time
pygame.init()
screen=pygame.display.set_mode((700,500))
class fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fish.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,20))
        self.rect=self.image.get_rect()
class plasticbag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plasticbag.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(15,25))
        self.rect=self.image.get_rect()
class food(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(15,25))
        self.rect=self.image.get_rect()
fd=["lilfish.png","plankton.png","seaweed.png"]
edibles=pygame.sprite.Group()
plastic=pygame.sprite.Group()
all=pygame.sprite.Group()
for I in range(50):
    item=food(random.choice(fd))
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    edibles.add(item)
    all.add(item)
for I in range(50):
    item=plasticbag()
    item.rect.x=random.randint(20,680)
    item.rect.y=random.randint(20,480)
    edibles.add(item)
    all.add(item)