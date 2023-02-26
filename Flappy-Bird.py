import pygame
import time
import random
import os
import sys

pygame.init()
window = pygame.display.set_mode((1000,700))
pygame.display.set_caption('Flappy_Bird')
pygame.display.update()
pygame.mixer.init()


#Game images & sprites
sizex,sizey = 75,50
pipes_x,pipes_y = 80,400
br1 = pygame.image.load('sprites/bird1.png').convert_alpha()
br1 = pygame.transform.scale(br1,(sizex,sizey)).convert_alpha()

br2 = pygame.image.load('sprites/bird2.png').convert_alpha()
br2 = pygame.transform.scale(br2,(sizex,sizey)).convert_alpha()

bg_img = pygame.image.load('sprites/bkg.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img,(1000,700)).convert_alpha()

st_img = pygame.image.load('sprites/start.png').convert_alpha()
st_img = pygame.transform.scale(st_img,(1000,700)).convert_alpha()

ground = pygame.image.load('sprites/ground.png').convert_alpha()
ground = pygame.transform.scale(ground,(1000,72)).convert_alpha()

pipe = pygame.image.load('sprites/greenpipe.png').convert_alpha()
pipe = pygame.transform.scale(pipe,(pipes_x,pipes_y)).convert_alpha()

pipe2 = pygame.image.load('sprites/greenpipe.png').convert_alpha()
pipe2 = pygame.transform.scale(pipe2,(pipes_x,pipes_y)).convert_alpha()
pipe2 = pygame.transform.rotate(pipe2,180).convert_alpha()

pause = pygame.image.load('sprites/pause.png')
pause = pygame.transform.scale(pause,(200,200)).convert_alpha()



#Checking if bird is crashed to pipe
def is_crashed(upper_crash,height,lower_crash):
    b_beak = 360
    b_tail = 310
    for i in range(0,len(upper_crash),3):
        if(b_beak >= upper_crash[i] and b_beak <= upper_crash[i+1] and height+45 <= upper_crash[i+2] ):
            return True
        if(b_tail >= upper_crash[i] and b_tail <= upper_crash[i+1] and height+40 <= upper_crash[i+2] ):
            return True
    for i in range(0,len(lower_crash),3):
        if(b_beak >= lower_crash[i] and b_beak <= lower_crash[i+1] and height+50 >= lower_crash[i+2] ):    
            return True
        if(b_tail >= lower_crash[i] and b_tail <= lower_crash[i+1] and height+50 >= lower_crash[i+2] ):    
            return True
    
    return False

#Creating new pipe
def get_pipe (lower_pipes,pipex_list,lower_crash):
    x_speed = 5 
    for x in range(0,len(lower_pipes),2):
        lower_pipes[x] = lower_pipes[x]-x_speed
    i = 1
    for x in range(0,len(lower_crash)):
        if( i%3 != 0):
            lower_crash[x] = lower_crash[x]-x_speed
        i += 1
        
    pipex_list= [x-x_speed for x in pipex_list]
    return lower_pipes,pipex_list,lower_crash


def get_upper_pipe(upper_pipes,upper_crash):
    x_speed = 5
    for x in range(0,len(upper_pipes),2):
        upper_pipes[x] = upper_pipes[x]-x_speed
    i = 1
    for x in range(0,len(upper_crash)):
        if( i%3 != 0):
            upper_crash[x] = upper_crash[x]-x_speed
        i += 1
        
    return upper_pipes,upper_crash
    
    

#Pause game
def pause_game():
    pygame.mixer.music.load('sprites/pause.wav')
    pygame.mixer.music.play()
    
    pause = 1
    while(pause):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = 0
                    break
    pygame.mixer.music.load('sprites/play.wav')
    pygame.mixer.music.play()

                

def game_over(ft,high_score,score):
    #Game variables
    clk = pygame.time.Clock()
    fps = 40
    white = (255,255,255)
    colour = (0,0,0)
    digit = 0
    height = 300
    esc = 1
    game_over = pygame.image.load('sprites/game over.png').convert_alpha()
    game_over = pygame.transform.scale(game_over,(600,300)).convert_alpha()

    score = pygame.image.load('sprites/score.png').convert_alpha()
    score = pygame.transform.scale(score,(600,300)).convert_alpha()
    with open ('high_score.txt','w') as f:
        high_score = f.write(str(high_score))
    
    
   

    pygame.mixer.music.load('sprites/hit.mp3')
    pygame.mixer.music.play()
    time.sleep(0.5)
    window.fill(white)
    pygame.display.update()
    time.sleep(0.05)
    pygame.mixer.music.load('sprites/bird_falls.wav')
    pygame.mixer.music.play()
    font = pygame.font.SysFont('timesnewroman',70)

    #Score font
    with open ('high_score.txt','r') as f:
        high_score = f.read()
    font = pygame.font.SysFont('timesnewroman',60)
    sc  = str(high_score)
   
    while(1):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_r) :
                    start_game()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    sys.exit()
                    
        window.blit(bg_img,(0,0))
        window.blit(game_over,(200,10))
        window.blit(score,(100,300))
        window.blit(ft,(530,390))
        
        scr = font.render(sc,True,colour)
        window.blit(scr,(580,460))
       
        
        br1 = pygame.image.load('sprites/bird1.png').convert_alpha()
        br1 = pygame.transform.scale(br1,(sizex,sizey)).convert_alpha()

        br1 = pygame.transform.rotate(br1,-45).convert_alpha()
        window.blit(br1,(300,height))

        if(height<550):
            height += 10
        pygame.display.update()
        clk.tick(fps) 
    
    


def game_on():
    #Game variables
    bird = [br1,br1,br1,br1,br1,br1,br1,br1,br2,br2,br2,br2,br2,br2,br2,br2]
    clk = pygame.time.Clock()
    fps = 35
    x_speed = 5
    y_speed = 15
    score = 0
    colour = (0,0,0)
    
    digit = 0
    height = 300

    #Pipe lists
    lower_pipes = [1000,300]
    upper_crash = [1000,1000+80,-252+400]
    upper_pipes = [1000,-300]
    lower_crash = [1000,1000+80,300]
    pipex_list  = [1000] 
    gx1=0
    gx2=1000
    xlr8  = 1
    dx=0

    #Score font
    with open ('high_score.txt','r') as f:
        high_score = f.read()
        
    font = pygame.font.SysFont('timesnewroman',70)

    #Gameloop
    while(1):
        #Catching events
        xlr8 =1
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    sys.exit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_SPACE) :
                    dx = -8
                    pygame.mixer.music.load('sprites/fly.mp3')
                    pygame.mixer.music.play()
        
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_p) :
                    window.blit(pause,(415,250))
                    pygame.display.update()
                    pause_game()
                    
        

        if(digit == 14):
            digit = 0

        dx += 0.5
        if(height<550):
            height += dx

        

    

        window.blit(bg_img,(0,0))
     

        for x in range(0,len(lower_pipes),2):
            window.blit(pipe,(lower_pipes[x],lower_pipes[x+1]))
            window.blit(pipe2,(upper_pipes[x],upper_pipes[x+1]))
          
       
        window.blit(ground,(gx1,628))
        window.blit(ground,(gx2,628))

        window.blit(bird[digit],(300,height))

        sc  = str(score)
        ft = font.render(sc,True,colour)
        window.blit(ft,(495,150))
        
        pygame.display.update()

    
        
        digit += 1
        gx1 -= x_speed
        gx2 -= x_speed
        if (gx1==-1000):
            gx1=1000
        if (gx2==-1000):
            gx2=1000

       
        lower_pipes,pipex_list,lower_crash = get_pipe(lower_pipes,pipex_list,lower_crash)
        upper_pipes,upper_crash = get_upper_pipe(upper_pipes,upper_crash)

        
        if(280 in pipex_list):
            score += 1
            point = pygame.mixer.Sound('sprites/point.wav')
            point.play()
    
        
                    
        if(lower_pipes[len(lower_pipes)-2] == 650):
            lower_pipes.append(1000)
            lower_crash.append(1000)
            lower_crash.append(1000+80)
            temp = random.randint(230,600)
            lower_pipes.append(temp)
            
            lower_crash.append(temp)
            
            pipex_list.append(1000)
            
            upper_pipes.append(1000)
            upper_crash.append(1000)
            upper_crash.append(1000+80)
            temp = temp - 600
            upper_pipes.append(temp)
            temp = temp + 450
            
            upper_crash.append(temp)
        

            
        if(lower_pipes[0] < -80):
            del lower_pipes[0]
            del lower_pipes[0]
            del lower_crash[0]
            del lower_crash[0]
            del lower_crash[0]
            
            del pipex_list[0]
            
            del upper_pipes[0]
            del upper_pipes[0]
            del upper_crash[0]
            del upper_crash[0]
            del upper_crash[0]
    
        if (score > int(high_score)):
            high_score = score

        flag = is_crashed(upper_crash,height,lower_crash)
        if(flag):
            game_over(ft,high_score,score)


        if(height <10):
            game_over(ft,high_score,score)

        clk.tick(fps)
        

def start_game():
    #Game variables
    bird = [br1,br1,br1,br1,br1,br1,br1,br1,br2,br2,br2,br2,br2,br2,br2,br2]
    clk = pygame.time.Clock()
    fps = 45
   
    digit = 0
    height = 300
    

    
    esc = 1 
    while(esc):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_SPACE) :
                    game_on()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    sys.exit()
        
        if (digit == 14):
            digit = 0
        window.blit(st_img,(0,0))
       
         
        window.blit(bird[digit],(300,height))
        pygame.display.update()
        
        digit += 1
        clk.tick(fps)


start_game()
