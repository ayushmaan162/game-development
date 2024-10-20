import pygame
pygame.init()
HEIGHT=500
WIDTH=700
screen=pygame.display.set_mode((700,500))
bg=pygame.transform.scale(pygame.image.load("bg.jpeg"),(700,500))
cricket=pygame.transform.scale(pygame.image.load("cricket.png"),(90,90))
football=pygame.transform.scale(pygame.image.load("football.png"),(75,90))
rugby=pygame.transform.scale(pygame.image.load("rugby.png"),(90,90))
font=pygame.font.SysFont("Berlin Sans FB",35)
text1=font.render("FOOTBALL",True,(255,140,0))
text2=font.render("RUGBY",True,(255,140,0))
text3=font.render("CRICKET",True,(255,140,0))
screen.blit(bg,(0,0))
screen.blit(cricket,(142,100))
screen.blit(football,(150,200))
screen.blit(rugby,(143,300))
screen.blit(text1,(420,120))
screen.blit(text2,(420,220))
screen.blit(text3,(420,320))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"beige",(pos),20,0)
            pygame.display.update()