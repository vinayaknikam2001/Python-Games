#Importing libraries
import pygame
import random
import time
import sys

#Setting game window
pygame.init()
window = pygame.display.set_mode((1000,700))
pygame.display.set_caption('Ping_Pong_Game')
pygame.display.update()
pygame.mixer.init()

#Loading bar images
size_x,size_y = 20,100
right_bar = pygame.image.load('sprites/right_bar.png')
right_bar = pygame.transform.scale(right_bar,(size_x,size_y)).convert_alpha()
left_bar = pygame.image.load('sprites/left_bar.png')
left_bar = pygame.transform.scale(left_bar,(size_x,size_y)).convert_alpha()

#Load ball image
ball = pygame.image.load('sprites/ball.png')
ball = pygame.transform.scale(ball,(30,30)).convert_alpha()

#Load table image
table = pygame.image.load('sprites/table.png')
table = pygame.transform.scale(table,(1000,640)).convert_alpha()

#Load table image
startp = pygame.image.load('sprites/startp.png')
startp = pygame.transform.scale(startp,(600,320)).convert_alpha()


#Load pause button
pause = pygame.image.load('sprites/pause.png')
pause = pygame.transform.scale(pause,(200,200)).convert_alpha()

#Load score number sprites
no_0 = pygame.image.load('sprites/0.png')
no_0 = pygame.transform.scale(no_0,(50,50)).convert_alpha()
no_1 = pygame.image.load('sprites/1.png')
no_1 = pygame.transform.scale(no_1,(50,50)).convert_alpha()
no_2 = pygame.image.load('sprites/2.png')
no_2 = pygame.transform.scale(no_2,(50,50)).convert_alpha()
no_3 = pygame.image.load('sprites/3.png')
no_3 = pygame.transform.scale(no_3,(50,50)).convert_alpha()
score = [no_0,no_1,no_2,no_3]

#Load boy images
flip_0 = pygame.image.load('sprites/flip0.png')
flip_0 = pygame.transform.scale(flip_0,(115,165)).convert_alpha()
flip_1 = pygame.image.load('sprites/flip1.png')
flip_1 = pygame.transform.scale(flip_1,(115,165)).convert_alpha()
flip_2 = pygame.image.load('sprites/flip2.png')
flip_2 = pygame.transform.scale(flip_2,(115,165)).convert_alpha()
flip_3 = pygame.image.load('sprites/flip3.png')
flip_3 = pygame.transform.scale(flip_3,(115,165)).convert_alpha()
flip_4 = pygame.image.load('sprites/flip4.png')
flip_4 = pygame.transform.scale(flip_4,(115,165)).convert_alpha()
flip_5 = pygame.image.load('sprites/flip5.png')
flip_5 = pygame.transform.scale(flip_5,(115,165)).convert_alpha()
boy = [flip_0,flip_1,flip_2,flip_3,flip_4,flip_5]

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

    

#Game over 
def game_over(score_1,score_2):
    green = (0,255,0)
    violet = (40,5,40)
    fps = 5
    i = 0
    clk = pygame.time.Clock()

    #If player1 wins
    if (score_1 > score_2):
        winner = str('Player 1 wins match')
    #If player2 wins
    else :
        winner = str('Player 2 wins match')

    while(1):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN) :
                    if (event.key == pygame.K_ESCAPE) :
                        pygame.quit()
                        sys.exit()

                if (event.type == pygame.KEYDOWN) :
                    if (event.key == pygame.K_r) :
                        pygame.mixer.music.stop()
                        start_game()

            if (i > 5):
                i = 0

            #Display font and images
            font = pygame.font.SysFont('timesnewroman',50)
            font = font.render(winner,True,green)
            
            window.fill(violet)
            window.blit(score[score_1],(350,300))
            window.blit(score[score_2],(650,300))
            window.blit(boy[i],(200,400))
            window.blit(font,(300,200))

            font = pygame.font.SysFont('timesnewroman',50)
            replay = str('Press R to replay')
            font = font.render(replay,True,green)
            window.blit(font,(350,600))
            pygame.display.update()
            
            i += 1
            clk.tick(fps)
            

    
    
def game_on():
    #Bar varibles
    left_x,left_y = 20,290
    right_x,right_y = 960,290
    l_speed = 0
    r_speed = 0
    bar_speed = 4

    #Ball variables
    ball_x,ball_y = 460,330
    ch = random.choice([1,-1])
    b_speedx = 5*ch
    ch = random.choice([1,-1])
    b_speedy = 5*ch

    #Font & Score variables
    font1 = pygame.font.SysFont('timesnewroman',25)
    font2 = pygame.font.SysFont('timesnewroman',25)
    score_1 = score_2 = 0

    #Colours
    green = (0,200,0)
    violet = (40,5,40)
    
    #Game clock & FPS
    fps = 60
    clk = pygame.time.Clock()

    while(1):
        #Caturing keyboard and mouse events 
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    sys.exit()
                    
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_p) :
                    window.blit(pause,(400,250))
                    pygame.display.update()
                    pause_game() 

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_w) :
                    l_speed = bar_speed*-1
                    
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_s) :
                    l_speed = bar_speed
                    
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_UP) :
                    r_speed = bar_speed*-1
                    
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_DOWN) :
                    r_speed = bar_speed
                    
            if (event.type == pygame.KEYUP) :
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    r_speed = 0
                if (event.key == pygame.K_w or event.key == pygame.K_s):
                    l_speed = 0
         
        
          
        left_y += l_speed
        right_y += r_speed


        #To restrict bar from moving out of screen
        if(left_y < 40):
            left_y = 40
        if(left_y > 560):
            left_y = 560
        if(right_y < 40):
            right_y = 40
        if(right_y > 560):
            right_y = 560

        #To reflect ball when hitted to edges of screen
        if(ball_y <= 40):
            b_speedy *= -1
            pygame.mixer.music.load('sprites/tap.mp3')
            pygame.mixer.music.play()
        if(ball_y >= 630):
            b_speedy *= -1
            pygame.mixer.music.load('sprites/tap.mp3')
            pygame.mixer.music.play()


        #Collision of ball to right bar
        if(ball_x+30 >= right_x and ball_y+30 >= right_y and ball_y <= right_y + 100):
            b_speedx *= -1
            pygame.mixer.music.load('sprites/ping.mp3')
            pygame.mixer.music.play()
            
        
        #Collision of ball to left bar
        if(ball_x <= left_x+20 and ball_y+30 >= left_y and ball_y <= left_y + 100):
            b_speedx *= -1
            pygame.mixer.music.load('sprites/ping.mp3')
            pygame.mixer.music.play()


        #Creates new ball
        if(ball_x <= -30):
            score_2 += 1
            time.sleep(1)
            ball_x,ball_y = 460,330
            pygame.mixer.music.load('sprites/newball.mp3')
            pygame.mixer.music.play()

            
            
        #Creates new ball
        if(ball_x >= 1000):
            score_1 += 1
            time.sleep(1)
            ball_x,ball_y = 460,330
            pygame.mixer.music.load('sprites/newball.mp3')
            pygame.mixer.music.play()

        ball_x += b_speedx
        ball_y += b_speedy
            
        

        #Display game score and colours
        window.fill(violet)
        sc1 = ['Player_1 : ',score_1]
        sc1 = str(sc1)
        str1 = font1.render(sc1,True,green)
        window.blit(str1,(0,0))
        sc2 = ['Player_2 : ',score_2]
        sc2 = str(sc2)
        str2 = font2.render(sc2,True,green)
        window.blit(str2,(800,0))

        
        
        #Display game ball and bars 
        window.blit(table,(0,30))
        window.blit(ball,(ball_x,ball_y))
        window.blit(left_bar,(left_x,left_y))
        window.blit(right_bar,(right_x,right_y))
        pygame.display.update()

        #Game over condtion
        if (score_1 == 3 or score_2 == 3):
            time.sleep(1)
            pygame.mixer.music.load('sprites/winner.mp3')
            pygame.mixer.music.play()
            game_over(score_1,score_2)
        clk.tick(fps)



def start_game():
    violet = (40,5,40)
    ball_x,ball_y = 670,140

    #Load game title and fonts
    start = pygame.image.load('sprites/start_button.png')
    title = pygame.image.load('sprites/title.png')
 
    while(1):
        #Capturing keyboard and mouse events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    sys.exit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_SPACE) :
                    game_on()

        #Display game title and images
        window.fill(violet)
        window.blit(table,(0,30))
        window.blit(startp,(0,250))
        window.blit(title,(220,120))
        window.blit(ball,(ball_x,ball_y))
        window.blit(start,(250,600))
        pygame.display.update()
            


start_game()


                    
        
