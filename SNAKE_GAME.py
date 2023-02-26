#Importing required packages
import pygame
import random
import time
import sys

#Setting up game window
pygame.init()
gameWindow = pygame.display.set_mode((900,600))
pygame.display.set_caption('SNAKE_GAME')


#Loading audios & Images
pygame.mixer.init()
bg_img = pygame.image.load('sprites/bg.jpg')
bg_img = pygame.transform.scale(bg_img,(900,600)).convert_alpha()
st_img = pygame.image.load('sprites/start_snake.png')
st_img = pygame.transform.scale(st_img,(900,600)).convert_alpha()
end_img= pygame.image.load('sprites/end.jpg').convert_alpha()
end_img= pygame.transform.scale(end_img,(900,600)).convert_alpha()
pause = pygame.image.load('sprites/pause.png')
pause = pygame.transform.scale(pause,(200,200)).convert_alpha()


#Colours
red    = (255,0,0) ;  blue   = (0,0,255) ; yellow = (255,255,0)   ;   green  = (0,200,0)  ;   black  = (0,0,0)

#Variables
key = 1
snake_x = 50
snake_y = 50
speedx  = 5
speedy  = 0
foodx  = random.randint(50,830)     ;     foody = random.randint(60,520)  ; food_size = 8          
snake_size = 10
fps = 30
exit_g = False
score =0 
clk = pygame.time.Clock()

#Snake list :
snk = []     ;   snk_len = 2

    

#Displaying snake body
def snake_body(snk):
    for x,y in snk:
        pygame.draw.circle(gameWindow,blue,(x,y),snake_size)



#Pause game function
def pause_game():
    #Playing pause sound
    stop = pygame.mixer.Sound('sprites/pause.wav')
    stop.play()

    #Loading pause button image
    pause = pygame.image.load('sprites/pause.png')
    pause = pygame.transform.scale(pause,(200,200)).convert_alpha()
    gameWindow.blit(pause,(350,200))
    
    pygame.display.update()
    pause = 1
    while(pause):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_p):
                    pause = 0
                    break
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    #Playing play sound
    start = pygame.mixer.Sound('sprites/play.wav')
    start.play()


#Game game_over function
def game_over():
    #Loading mario die sound
    pygame.mixer.music.load('sprites/mario_dies.mp3')
    pygame.mixer.music.play()

    #Synchronising music and background
    time.sleep(3)

    #Gameover png
    gameWindow.blit(end_img,(0,0))
    pygame.display.update()
    while (1):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_game()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        
        
           


def game_on():
    #Loading background mario music
    pygame.mixer.music.load('sprites/mario_overworld.mp3')
    pygame.mixer.music.play(-1)
    food = pygame.mixer.Sound('sprites/food.mp3')

    #score
    font = pygame.font.SysFont('timesnewroman',30)
    #Colours
    red    = (255,0,0) ;  blue   = (0,0,255) ; yellow = (255,255,0)   ;   green  = (0,200,0)  ;   black  = (0,0,0)

    #Variables
    key = 1
    snake_x = 50
    snake_y = 50
    speedx  = 5
    speedy  = 0
    foodx  = random.randint(50,830)     ;     foody = random.randint(60,520)  ; food_size = 8 ;          
    snake_size = 10
    fps = 30
    exit_g = False
    score =0 
    clk = pygame.time.Clock()

    #Snake list :
    snk = []     ;   snk_len = 2

    
    while not exit_g:
        #Capturing events
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and key != 1):  # left arrow key
                if event.key == pygame.K_LEFT:
                    speedx = -5
                    speedy = 0
                    key = 2

            if (event.type == pygame.KEYDOWN and key != 2):  # left arrow key
                if event.key == pygame.K_RIGHT:
                    speedx = 5
                    speedy = 0
                    key = 1

            if (event.type == pygame.KEYDOWN and key != 3):  # left arrow key
                if event.key == pygame.K_UP:
                    speedy = -5
                    speedx = 0
                    key = 4

            if (event.type == pygame.KEYDOWN and key != 4):  # left arrow key
                if event.key == pygame.K_DOWN:
                    speedy = 5
                    speedx = 0
                    key = 3

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                    pause_game()
                    pygame.mixer.music.unpause()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Updating snake 
        snake_x = snake_x + speedx
        snake_y = snake_y + speedy
        snk_jaw = []
        snk_jaw.append(snake_x)
        snk_jaw.append(snake_y)
        snk.append(snk_jaw)
        
        #Removing extra element of snake body
        if (len(snk) > snk_len):
            del snk[0]

        #Detecting game over
        if (snk_jaw in snk[:len(snk) - 1]):
            game_over()

        #Detecting collision with border
        if (snake_x > 860 or snake_y > 550):
            game_over()
        if (snake_x < 35 or snake_y < 40):
            game_over()

        #Checking collision with food
        if (abs(snake_x - foodx) < 15 and abs(snake_y - foody) < 15):
            food.play();
            foodx = random.randint(50, 830);    foody = random.randint(60, 520)
            snk_len += 7
            score += 5

        #Updating score
        lst = ['Score :-', score]
        scr = str(lst)

        #Updating background
        gameWindow.blit(bg_img, [0, 0])

        #Displaying score 
        x = font.render(scr, True, green)
        gameWindow.blit(x, [0, 0])

        #Drawing food
        pygame.draw.circle(gameWindow, red, (foodx ,foody) ,food_size)

        #Drawing snake body
        snake_body(snk)

        #Updating display
        pygame.display.update()
        clk.tick(fps)
            
    
    

    



#Start game function
def start_game():
    
    gameWindow.blit(st_img,(0,0))
    pygame.display.update()
    esc = 1
    while(esc):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    esc = 0
                    break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    game_on()

start_game() 


                
