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
 
    snake_List = []
    Length_of_snake = 1
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("Hai Perso! Premi ESC per uscire o C per continuare", red)
            Your_score(Length_of_snake - 1)
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
                x.append(round(random.randrange(0, dis_width - block) / 200.0) * 200.0)
                y.append(round(random.randrange(0, dis_height - block) / 200.0) * 200.0)
                c.append(green)

        dis.fill(black)
        for ct in range(len(x)):
            x[ct]+=x1_change
            y[ct]+=y1_change
            
            if x[ct]>=dis_width-block:
                x[ct]=dis_width-block
            if x[ct]<0:
                x[ct]=0
            if y[ct]>=dis_height-block:
                y[ct]=dis_height-block
            if y[ct]<0:
                y[ct]=0
        
        pygame.draw.rect(dis, c[ct], [x[ct], y[ct], block, block])
        pygame.display.update()
                
        for ct1 in range(len(x)-1):
            for ct2 in range(ct1+1, len(x)-1):
                if(x[ct1]==x[ct2]) and (y[ct1]==y[ct2]) and (c[ct1]==c[ct2]):
                    c[ct2]=change_color(c[ct2])
                    del x[ct1]
                    del y[ct1]
                    del c[ct1]
                elif(x[ct1]==x[ct2]) and (y[ct1]==y[ct2]) and (c[ct1]!=c[ct2]):
                    x[ct2]+=x1_change
                    y[ct2]+=y1_change
            

        
        
        clock.tick(transition_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()