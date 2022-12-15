import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 0, 213)
 
dis_width = 800
dis_height = 800
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('2048')
 
clock = pygame.time.Clock()
 
block = 200
transition_speed = 2
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
    
def BubbleSort(x, y, c, s):
    if(len(x)>1):
        if(s=="<"):
            for ct in range(len(x)-1):
                for ct2 in range(0, len(x)-ct-1):
                    if x[ct2] < x[ct2 + 1]:
                        x[ct2], x[ct2 + 1] = x[ct2 + 1], x[ct2]
                        y[ct2], y[ct2 + 1] = y[ct2 + 1], y[ct2]
                        c[ct2], c[ct2 + 1] = c[ct2 + 1], c[ct2]
        if(s==">"):
            for ct in range(len(x)):
                for ct2 in range(0, len(x)-ct):
                    if x[ct2] < x[ct2 + 1]:
                        x[ct2], x[ct2 + 1] = x[ct2 + 1], x[ct2]
                        y[ct2], y[ct2 + 1] = y[ct2 + 1], y[ct2]
                        c[ct2], c[ct2 + 1] = c[ct2 + 1], c[ct2]
    return x, y, c
                    
def Shihft(x, y, c, change):
    min=0
    max=dis_width-block
    
    for ct in range(3):
        r=0
        for ct2 in range(len(x)-1):
            x[ct2]+=change
            m=ct2+r
            if x[m]>=max:
                x[m]=max
                if(len(x)>1):
                    if(c[m]!=c[cmt2+1]):
                        max=x[m]-block
            if x[m]<min:
                x[m]=min
                if(len(x)>1):
                    if(c[m]!=c[m+1]):
                        min=x[m]+block
            
            if(c[m]==c[m+1] and x[m]==x[m+1] and y[m]==y[m+1]):
                del x[m]
                del y[m]
                del c[m]
                c[m+1]=change_color
                r-=1
            else:
                pygame.draw.rect(dis, green, [x[m], y[m], block, block])
                pygame.display.update()
                clock.tick(transition_speed)
        return x, y, c
        
def change_color(c):
    if c==(0, 255, 0):
        return (50, 0, 213)
    elif c==(50, 0, 213):
        return (255, 255, 100)
    elif c==(255, 255, 100):
        return (255, 0, 0)
    else:
        return (0, 255, 0)
 
def gameLoop():
    game_over = False
    game_close = False
 
    x = []
    y = []
    c = []
    
    x.append(round(random.randrange(0, dis_width - block) / 200.0) * 200.0)
    y.append(round(random.randrange(0, dis_height - block) / 200.0) * 200.0)
    c.append(green)
    pygame.draw.rect(dis, c[0], [x[0], y[0], block, block])
    pygame.display.update()
 
    x1_change = 0
    y1_change = 0
    
    points=0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("Hai Perso! Premi ESC per uscire o C per continuare", red)
            Your_score(points - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = True
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0
                if(x1_change<0):
                    x, y, c=BubbleSort(x, y, c, "<")
                    x, y, c=Shihft(x, y, c, x1_change)
                if(x1_change>0):
                    x, y, c=BubbleSort(x, y, c, ">")
                    x, y, c=Shihft(x, y, c, x1_change)
                if(y1_change<0):
                    x, y, c=BubbleSort(y, x, c, "<")
                    x, y, c=Shihft(y, y, c, y1_change)
                if(y1_change>0):
                    x, y, c=BubbleSort(y, x, c, ">")
                    x, y, c=Shihft(y, y, c, y1_change)
                x.append(round(random.randrange(0, dis_width - block) / 200.0) * 200.0)
                y.append(round(random.randrange(0, dis_height - block) / 200.0) * 200.0)
                c.append(green)
                pygame.display.update()
              
    clock.tick(transition_speed)    
 
    pygame.quit()
    quit()
 
 
gameLoop()