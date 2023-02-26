#Importing liabraries
import pygame
import time
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1000,700))
pygame.display.set_caption('N_test')
pygame.display.update()
pygame.mixer.init()

#Loading images
idel = pygame.image.load('ninja_sprites/idel.png')
idel = pygame.transform.scale(idel,(55,100)).convert_alpha()
rest = [idel,idel,idel,idel,idel,idel,idel,idel,idel,idel]
idel_mask = pygame.mask.from_surface(idel)

#Runnig forward images
rx,ry = 75,100
run0 = pygame.image.load('ninja_sprites/Run_000.png')
run0 = pygame.transform.scale(run0,(rx,ry)).convert_alpha()

run1 = pygame.image.load('ninja_sprites/Run_001.png')
run1 = pygame.transform.scale(run1,(rx,ry)).convert_alpha()

run2 = pygame.image.load('ninja_sprites/Run_002.png')
run2 = pygame.transform.scale(run2,(rx,ry)).convert_alpha()

run3 = pygame.image.load('ninja_sprites/Run_003.png')
run3 = pygame.transform.scale(run3,(rx,ry)).convert_alpha()

run4 = pygame.image.load('ninja_sprites/Run_004.png')
run4 = pygame.transform.scale(run4,(rx,ry)).convert_alpha()

run5 = pygame.image.load('ninja_sprites/Run_005.png')
run5 = pygame.transform.scale(run5,(rx,ry)).convert_alpha()

run6 = pygame.image.load('ninja_sprites/Run_006.png')
run6 = pygame.transform.scale(run6,(rx,ry)).convert_alpha()

run7 = pygame.image.load('ninja_sprites/Run_007.png')
run7 = pygame.transform.scale(run7,(rx,ry)).convert_alpha()

run8 = pygame.image.load('ninja_sprites/Run_008.png')
run8 = pygame.transform.scale(run8,(rx,ry)).convert_alpha()

run9 = pygame.image.load('ninja_sprites/Run_009.png')
run9 = pygame.transform.scale(run9,(rx,ry)).convert_alpha()
run_mask = pygame.mask.from_surface(run3)
run_forward = [run0,run1,run2,run3,run4,run5,run6,run7,run8,run9]

#Running backward images
run00 = pygame.image.load('ninja_sprites/Run_0.png')
run00 = pygame.transform.scale(run00,(rx,ry)).convert_alpha()

run01 = pygame.image.load('ninja_sprites/Run_1.png')
run01 = pygame.transform.scale(run01,(rx,ry)).convert_alpha()

run02 = pygame.image.load('ninja_sprites/Run_2.png')
run02 = pygame.transform.scale(run02,(rx,ry)).convert_alpha()

run03 = pygame.image.load('ninja_sprites/Run_3.png')
run03 = pygame.transform.scale(run03,(rx,ry)).convert_alpha()

run04 = pygame.image.load('ninja_sprites/Run_4.png')
run04 = pygame.transform.scale(run04,(rx,ry)).convert_alpha()

run05 = pygame.image.load('ninja_sprites/Run_5.png')
run05 = pygame.transform.scale(run05,(rx,ry)).convert_alpha()

run06 = pygame.image.load('ninja_sprites/Run_6.png')
run06 = pygame.transform.scale(run06,(rx,ry)).convert_alpha()

run07 = pygame.image.load('ninja_sprites/Run_7.png')
run07 = pygame.transform.scale(run07,(rx,ry)).convert_alpha()

run08 = pygame.image.load('ninja_sprites/Run_8.png')
run08 = pygame.transform.scale(run08,(rx,ry)).convert_alpha()

run09 = pygame.image.load('ninja_sprites/Run_9.png')
run09 = pygame.transform.scale(run09,(rx,ry)).convert_alpha()
run_backward = [run00,run01,run02,run03,run04,run05,run06,run07,run08,run09]

#Climbing images 
rx,ry = 75,100
climb0 = pygame.image.load('ninja_sprites/Climb_000.png')
climb0 = pygame.transform.scale(climb0,(rx,ry)).convert_alpha()

climb1 = pygame.image.load('ninja_sprites/Climb_001.png')
climb1 = pygame.transform.scale(climb1,(rx,ry)).convert_alpha()

climb2 = pygame.image.load('ninja_sprites/Climb_002.png')
climb2 = pygame.transform.scale(climb2,(rx,ry)).convert_alpha()

climb3 = pygame.image.load('ninja_sprites/Climb_003.png')
climb3 = pygame.transform.scale(climb3,(rx,ry)).convert_alpha()

climb4 = pygame.image.load('ninja_sprites/Climb_004.png')
climb4 = pygame.transform.scale(climb4,(rx,ry)).convert_alpha()

climb5 = pygame.image.load('ninja_sprites/Climb_005.png')
climb5 = pygame.transform.scale(climb5,(rx,ry)).convert_alpha()

climb6 = pygame.image.load('ninja_sprites/Climb_006.png')
climb6 = pygame.transform.scale(climb6,(rx,ry)).convert_alpha()

climb7 = pygame.image.load('ninja_sprites/Climb_007.png')
climb7 = pygame.transform.scale(climb7,(rx,ry)).convert_alpha()

climb8 = pygame.image.load('ninja_sprites/Climb_008.png')
climb8 = pygame.transform.scale(climb8,(rx,ry)).convert_alpha()

climb9 = pygame.image.load('ninja_sprites/Climb_009.png')
climb9 = pygame.transform.scale(climb9,(rx,ry)).convert_alpha()
climbing = [climb0,climb1,climb2,climb3,climb4,climb5,climb6,climb7,climb8,climb9]

#Attacking images
rx,ry = 105,110
attack0 = pygame.image.load('ninja_sprites/Attack__000.png')
attack0 = pygame.transform.scale(attack0,(rx,ry)).convert_alpha()

attack1 = pygame.image.load('ninja_sprites/Attack__001.png')
attack1 = pygame.transform.scale(attack1,(rx,ry)).convert_alpha()

attack2 = pygame.image.load('ninja_sprites/Attack__002.png')
attack2 = pygame.transform.scale(attack2,(rx,ry)).convert_alpha()

attack3 = pygame.image.load('ninja_sprites/Attack__003.png')
attack3 = pygame.transform.scale(attack3,(rx,ry)).convert_alpha()

attack4 = pygame.image.load('ninja_sprites/Attack__004.png')
attack4 = pygame.transform.scale(attack4,(rx,ry)).convert_alpha()

attack5 = pygame.image.load('ninja_sprites/Attack__005.png')
attack5 = pygame.transform.scale(attack5,(rx,ry)).convert_alpha()

attack6 = pygame.image.load('ninja_sprites/Attack__006.png')
attack6 = pygame.transform.scale(attack6,(rx,ry)).convert_alpha()

attack7 = pygame.image.load('ninja_sprites/Attack__007.png')
attack7 = pygame.transform.scale(attack7,(rx,ry)).convert_alpha()

attack8 = pygame.image.load('ninja_sprites/Attack__008.png')
attack8 = pygame.transform.scale(attack8,(rx,ry)).convert_alpha()

attack9 = pygame.image.load('ninja_sprites/Attack__009.png')
attack9 = pygame.transform.scale(attack9,(rx,ry)).convert_alpha()
attacking = [attack0,attack1,attack2,attack3,attack4,attack5,attack6,attack7,attack8,attack9]

#Throwing images 
rx,ry = 75,100
Throw = pygame.image.load('ninja_sprites/Throw.png')
Throw = pygame.transform.scale(Throw,(rx,ry)).convert_alpha()
throwing = [Throw,Throw,Throw,Throw,Throw,Throw,Throw,Throw,Throw,Throw]

#Sliding images
sx,sy = 90,110
slidef = pygame.image.load('ninja_sprites/slidef.png')
slidef = pygame.transform.scale(slidef,(sx,sy)).convert_alpha()
slideb = pygame.image.load('ninja_sprites/slideb.png')
slideb = pygame.transform.scale(slideb,(sx,sy)).convert_alpha()
slide_forward = [slidef,slidef,slidef,slidef,slidef,slidef,slidef,slidef,slidef,slidef]
slide_backward = [slideb,slideb,slideb,slideb,slideb,slideb,slideb,slideb,slideb,slideb]
sliding_mask = pygame.mask.from_surface(slidef)

#Kunai knife images
kx,ky = 70,20
kunai = pygame.image.load('ninja_sprites/Kunai.png')
kunai = pygame.transform.scale(kunai,(kx,ky)).convert_alpha()

#Gliding images
gx,gy = 90,100
glide = pygame.image.load('ninja_sprites/glide.png')
glide = pygame.transform.scale(glide,(gx,gy)).convert_alpha()
gliding = [glide,glide,glide,glide,glide,glide,glide,glide,glide,glide]

#Jumpimg images
jump = pygame.image.load('ninja_sprites/jump.png')
jump = pygame.transform.scale(jump,(gx,gy)).convert_alpha()
jumping = [jump,jump,jump,jump,jump,jump,jump,jump,jump,jump]
jump_mask = pygame.mask.from_surface(jump)

#Dead images
dead = pygame.image.load('ninja_sprites/dead.png')
dead = pygame.transform.scale(dead,(100,130)).convert_alpha()

#Blast images
blast = pygame.image.load('ninja_sprites/blast.png')
blast = pygame.transform.scale(blast,(100,130)).convert_alpha()


#Platform images
platform = pygame.image.load('ninja_sprites/Base.png').convert_alpha()
platform = pygame.transform.scale(platform,(1010,100)).convert_alpha()
#Game over images
gameover = pygame.image.load('ninja_sprites/game_over.png').convert_alpha()
gameover = pygame.transform.scale(gameover,(1000,700)).convert_alpha()

#Obstacles images
#Void image
void = pygame.image.load('ninja_sprites/void.png')
void = pygame.transform.scale(void,(150,100)).convert_alpha()
#Tower image
tower = pygame.image.load('ninja_sprites/tower.png')
tower = pygame.transform.scale(tower,(600,700)).convert_alpha()
tower_mask = pygame.mask.from_surface(tower)
#Cave image
cave = pygame.image.load('ninja_sprites/cave3.png').convert_alpha()
cave = pygame.transform.scale(cave,(2000,526)).convert_alpha()
cave_mask = pygame.mask.from_surface(cave)
#Mine images
mine = pygame.image.load('ninja_sprites/mine.png').convert_alpha()
mine = pygame.transform.scale(mine,(60,60)).convert_alpha()
mine_mask = pygame.mask.from_surface(mine)
#spiky_monster_a
spiky_monster_a = pygame.image.load('ninja_sprites/spiky_monster_a.png').convert_alpha()
spiky_monster_a = pygame.transform.scale(spiky_monster_a,(80,50)).convert_alpha()
a_mask = pygame.mask.from_surface(spiky_monster_a)
#spiky_monster_b
spiky_monster_b = pygame.image.load('ninja_sprites/spiky_monster_b.png').convert_alpha()
spiky_monster_b = pygame.transform.scale(spiky_monster_b,(80,50)).convert_alpha()
b_mask = pygame.mask.from_surface(spiky_monster_b)
#Spikes image
spikes = pygame.image.load('ninja_sprites/spikes.png').convert_alpha()
spikes = pygame.transform.scale(spikes,(100,50)).convert_alpha()
spikes_mask = pygame.mask.from_surface(spikes)
#Bat images
bat = pygame.image.load('ninja_sprites/bat.png').convert_alpha()
bat = pygame.transform.scale(bat,(60,70)).convert_alpha()
bat_mask = pygame.mask.from_surface(bat)
#Ghost images
ghost = pygame.image.load('ninja_sprites/ghost.png').convert_alpha()
ghost = pygame.transform.scale(ghost,(150,100)).convert_alpha()
ghost_mask = pygame.mask.from_surface(ghost)
#Spikes image
big_thorn = pygame.image.load('ninja_sprites/big_thorn.png').convert_alpha()
big_thorn = pygame.transform.scale(big_thorn,(80,150)).convert_alpha()
big_thorn_mask = pygame.mask.from_surface(big_thorn)
#Castle image
castle = pygame.image.load('ninja_sprites/castle2.png').convert_alpha()
castle = pygame.transform.scale(castle,(600,500)).convert_alpha()
#Decorating obstacles
#Fireworks
fireworks = pygame.image.load('ninja_sprites/fireworks.png').convert_alpha()
fireworks = pygame.transform.scale(fireworks,(200,200)).convert_alpha()


#Updating kunai
def update_kunai(kunai):
    kunai_speed = 15
    for i in range(len(kunai)):
        kunai[i][0] = kunai[i][0] + kunai_speed
    return kunai


#Pause game
def pause_game():
    stop = pygame.mixer.Sound('ninja_sound/pause.wav')
    stop.play()
    #Load pause button
    pause = pygame.image.load('sprites/pause.png')
    pause = pygame.transform.scale(pause,(200,200)).convert_alpha()
    window.blit(pause,(400,250))
    pygame.display.update()
    pause = 1
    while(pause):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_p):
                    pause = 0
                    break
    start = pygame.mixer.Sound('ninja_sound/play.wav')
    start.play()

#Game over
def game_over():
    window.blit(gameover,(0,0))
    pygame.mixer.music.load('ninja_sound/game_over.mp3')
    pygame.mixer.music.play()
    pygame.display.update()
    while(1):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    start_game()
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    quit()
    

#Ninja dead
def death(ninja_x,ninja_y):
    pygame.mixer.stop()
    die = pygame.mixer.Sound('ninja_sound/death1.wav')
    die.play()
    
    window.blit(dead,(ninja_x,485))
    pygame.display.update()
    time.sleep(1)
    game_over()


#Ninja falls
def fall(ninja_x,ninja_y,ox,oy):
    pygame.mixer.stop()
    die = pygame.mixer.Sound('ninja_sound/death1.wav')
    die.play()
    fps = 30
    blue = (160,160,200)
    clk = pygame.time.Clock()
    while(1):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    start()
        window.fill(blue)
        window.blit(platform,(0,600))
        window.blit(void,(ox,oy))
        window.blit(jump,(ninja_x,ninja_y))
        ninja_y += 10
        pygame.display.update()
        clk.tick(fps)
        if(ninja_y >= 700):
            game_over()
            
#Ninja blasted
def blasted (ninja_x,ninja_y):
    pygame.mixer.stop()
    explode = pygame.mixer.Sound('ninja_sound/explode.mp3')
    explode.play()
    window.blit(blast,(ninja_x,ninja_y))
    pygame.display.update()
    time.sleep(1)
    die = pygame.mixer.Sound('ninja_sound/death1.wav')
    die.play()
    window.blit(dead,(ninja_x,485))
    pygame.display.update()
    time.sleep(0.5)
    game_over()
    
def victory():
    fire = pygame.mixer.Sound('ninja_sound/fireworks.wav')
    pygame.mixer.stop()
    pygame.mixer.music.load('ninja_sound/victory.wav')
    pygame.mixer.music.play()
    window.blit(fireworks,(0,250))
    fire.play()
    time.sleep(0.5)
    pygame.display.update()
    window.blit(fireworks,(400,0))
    fire.play()
    time.sleep(0.5)
    pygame.display.update()
    window.blit(fireworks,(800,300))
    fire.play()
    time.sleep(0.5)
    pygame.display.update()
    while(1):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    start_game()
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    quit()
                        
    
    
    
#Game on
def game_on() :
    #Colours
    blue = (160,160,200)
    
    #Image iterator
    i = 0

    #State of a player jump,run etc.
    state = rest
    jmp = 0
    foot = pygame.mixer.Sound('ninja_sound/foot.mp3')

    #Ninja co-ordinates
    ninja_x,ninja_y = 100,0
    speed = 10 
    move_x = 0
    move_y = 0 

    #Obstacle variables
    o = 0
    o_x = [600,1600,1000,1400,1200,1100,1500,1000,1200,1200]
    o_y = [600,600,550,600,600,580,580,600,-100,0]
    obstacle = [void,void,spikes,void,void,mine,mine,void,tower,cave]
    ox = [1200,1200,1000,2000,1700,1000,1000,1000,1000,1900]
    oy = [550,600,550,550,580,-100,600,600,450,580]
    obstacle2 = [spikes,void,spikes,spikes,mine,tower,void,void,big_thorn,mine]
    o2 = 0
    catch = 0
    collided = 0
    fall1 = [0,1,3,4,7]
    fall2 = [1,6,7]
    dies1 = [2]
    dies2 = [0,2,3,8]
    blast1 = [5,6]
    blast2 = [4,9]

    #Base variables
    base_x,base_y = 0,600
    base_x2 = 1000
    castle_x = 1000
    
    #Kunai list
    kunai_list = []
    slide = 0
    sword_sound = pygame.mixer.Sound('ninja_sound/sword.wav')

    #Enemy switches
    ex = 500
    ex2 = ex + 300
    enemy_speed = 4
    enemy = [1,1,1,1,1,1,1]
    sound_flag = [1,1,1,1,1,1]

 
    #Backgroound music and clock
    clk = pygame.time.Clock()
    pygame.mixer.music.load('ninja_sound/turtle.mp3')
    pygame.mixer.music.play(-1)
    foot1 = pygame.mixer.Sound('ninja_sound/foot.mp3')
    foot2 = pygame.mixer.Sound('ninja_sound/foot.mp3')
    sword_sound = pygame.mixer.Sound('ninja_sound/sword.wav')
    kunai_sound = pygame.mixer.Sound('ninja_sound/kunai.mp3')
    jump_sound = pygame.mixer.Sound('ninja_sound/jump.wav')
    while(1):
        #Caturing keyboard and mouse events 
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_p) :
                    pygame.mixer.music.pause()
                    pause_game()
                    pygame.mixer.music.unpause()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_r) :
                    start_game()
                    
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    quit()
                    
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_LEFT and ninja_x >= 0) :
                    if(ninja_y >= 500):
                        foot1.play(-1)
                    if(ninja_y <= 500 and ninja_y >= 300):
                        state = jumping
                    else:
                        state = run_backward
                        
                    move_x = -speed
                    slide = -1

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_RIGHT) :
                    if(ninja_y >= 500):
                        foot2.play(-1)
                    if(ninja_y <= 500 and ninja_y >= 300):
                        state = jumping
                    else:
                        state = run_forward
                        
                    move_x = speed
                    slide = 1
            #Sliding
            if (event.type == pygame.KEYDOWN) :
                if (event.key == K_DOWN) :
                    state = slide_forward
                    if(slide== -1):
                        state = slide_backward
                        slide = 0
                    if(slide == 1):
                        state = slide_forward
                        slide = 0
                    
                   

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_UP and catch) :
                    state = climbing
                    move_y = -speed
                    

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_DOWN and catch) :
                    state = climbing
                    move_y = speed

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_f) :
                    kunai_sound.play()
                    new_kunai = [ninja_x,ninja_y+20]
                    kunai_list.append(new_kunai)
                    state = throwing
                    
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_s) :
                    
                    sword_sound.play(-1)
                    state = attacking
            
                
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_SPACE and ninja_y >= 500) :
                    
                    jump_sound.play()
                    jmp = 1
                    state = jumping
                    ninja_y -= 210
                    
            #Change state to rest if ninja is not jumping or running
            if (event.type == pygame.KEYUP and not (jmp) and not(catch)) :
                    state = rest
                    move_x = 0
                    pygame.mixer.Sound.stop(sword_sound)
            if (event.type == pygame.KEYUP) :
                if(event.key == pygame.K_LEFT):
                   pygame.mixer.Sound.stop(foot1)
                   pygame.mixer.Sound.stop(sword_sound)
                if(event.key == pygame.K_RIGHT):
                   pygame.mixer.Sound.stop(foot2)
                   pygame.mixer.Sound.stop(sword_sound)
            
                state = rest
                move_x = 0
                move_y = 0

        #Setting a background
        window.fill(blue)

        if(ninja_x >= 400):
            base_x -= move_x
            base_x2 -= move_x
        if(base_x <= -1000):
            base_x = 1000
        if (base_x2 <= -1000):
            base_x2 = 1000
            
        window.blit(platform,(base_x,base_y))
        window.blit(platform,(base_x2,base_y))
        #Display obstacle_1
        if(ninja_x >=400):
            o_x[o] -= move_x
        window.blit(obstacle[o],(o_x[o],o_y[o]))
        if (o_x[o] < -400):
            if(o+1 < len(obstacle)):
                o += 1


        #Obstacle with falling type
        if(o in  fall1 and ninja_x >= o_x[o] and ninja_x <= o_x[o]+90 and ninja_y >= 500):
            fall(ninja_x,ninja_y,o_x[o],o_y[o])
        #Obstacle with spikes
        if(o in dies1):
            offset = (ninja_x - o_x[o],ninja_y - o_y[o])
            collide = spikes_mask.overlap(idel_mask,offset)
            if (collide):
                death(ninja_x,ninja_y)     
        #Obstacle mines
        if(o in blast1):
            offset = (ninja_x - o_x[o],ninja_y - o_y[o])
            collide = mine_mask.overlap(idel_mask,offset)
            if (collide):
                blasted(ninja_x,ninja_y)
            
        #If tower is catched
        if(o == 8):
            offset = (int(ninja_x-o_x[o]),int(ninja_y-o_y[o]))
            collide = tower_mask.overlap(idel_mask,offset)
            if (collide):
                catch = 1
            
            else:
                catch = 0
        if(o == 9):
            offset = (int(ninja_x-o_x[o]),int(ninja_y-o_y[o]))
            collide = cave_mask.overlap(idel_mask,offset)
            if(collide):
                if(state == slide_forward or state == slide_backward):
                    pass
                else:
                    death(ninja_x,ninja_y)
            



                

        #Display obstacle_2
        if(ninja_x >=400):
            ox[o2] -= move_x
        window.blit(obstacle2[o2],(ox[o2],oy[o2]))
        if (ox[o2] < -400):
            if(o2+1 < len(obstacle2)):
                o2 += 1
        if(o2 in  fall2 and ninja_x >= ox[o2] and ninja_x <= ox[o2]+85 and ninja_y >= 500):
            fall(ninja_x,ninja_y,ox[o2],oy[o2])
        
        if(o2 in dies2):
            offset = (ninja_x - ox[o2],ninja_y - oy[o2])
            collide = spikes_mask.overlap(idel_mask,offset)
            if (collide):
                death(ninja_x,ninja_y)
                
        #Obstacle mines
        if(o2 in blast2):
            offset = (ninja_x - ox[o2],ninja_y - oy[o2])
            collide = mine_mask.overlap(idel_mask,offset)
            if (collide):
                blasted(ninja_x,ninja_y)
        
        #If tower is catched
        if(o2 == 5):
            offset = (int(ninja_x-ox[o2]),int(ninja_y-oy[o2]))
            collide = tower_mask.overlap(idel_mask,offset)
            if (collide):
                catch = 1
            
            else:
                catch = 0
        #Big thorn
        if(o2 == 8):
            offset = (ninja_x - ox[o2],ninja_y - oy[o2])
            collide = big_thorn_mask.overlap(idel_mask,offset)
            if (collide):
                death(ninja_x,ninja_y)

    


        #Checking enemy events
        #1st enemy spiky monster b
        if(enemy[0]):
            window.blit(spiky_monster_b,(ex,550))
            offset = (ninja_x - ex,ninja_y - 550)
            collide = b_mask.overlap(idel_mask,offset)
            if (collide):
                if(state == attacking):
                    enemy[0] = 0
                    ex =1000
                    ex2 = ex+200
                else:
                    death(ninja_x,ninja_y)
            
            ex -= enemy_speed
            if(ex <= -100):
                ex =1000
                ex2 = ex+300
                enemy[0] = 0
                enemy_speed = 4

        #2nd enemy two spiky monsters
        if(enemy[1] and ox[0] <= 0):
            window.blit(spiky_monster_a,(ex,550))
            window.blit(spiky_monster_b,(ex2,550))
            offset = (ninja_x - ex,ninja_y - 550)
            collide = a_mask.overlap(idel_mask,offset)
            
            if (collide):
                if(state == attacking):
                    enemy[1] = 0
                    ex =1000
                    ex2 = ex+300
                else:
                    death(ninja_x,ninja_y)
            
            offset = (ninja_x - ex2,ninja_y - 550)
            collide = b_mask.overlap(idel_mask,offset)
            if (collide):
                if(state == attacking):
                    enemy[1] = 0
                    ex =1000
                    ex2 = ex+300
                else:
                    death(ninja_x,ninja_y)
                    
            ex -= enemy_speed
            ex2 -= enemy_speed
            if(ex2 <= -100):
                ex =1000
                ex2 = ex+300
                enemy[1] = 0

        #3rd enemy two bats
        if(enemy[2] and ox[2] <= 0):
            window.blit(bat,(ex,440))
            window.blit(bat,(ex2,440))
            offset = (ninja_x - ex,ninja_y - 550)
            collide = bat_mask.overlap(idel_mask,offset)
            if(sound_flag[0]):
                bat_sound = pygame.mixer.Sound('ninja_sound/bat.mp3')
                bat_sound.play()
                sound_flag[0] = 0
            #If ninja is sliding
            #Bat1 appears
            if (state == slide_forward or state == slide_backward):
                collide = 0
            if (collide):
                death(ninja_x,ninja_y)
                
            offset = (ninja_x - ex2,ninja_y - 550)
            collide = bat_mask.overlap(idel_mask,offset)
            #If ninja is sliding
            #Bat 2 appears
            if (state == slide_forward or state == slide_backward):
                collide = 0
            if (collide):
                death(ninja_x,ninja_y)
            ex -= enemy_speed
            ex2 -= enemy_speed
            if(ex2 <= -100):
                ex =1000
                ex2 = ex+350
                enemy[2] = 0

        #4th enemy spiky monster and bat
        if(enemy[3] and o_x[3] <= 0):
            #Spike monster
            window.blit(spiky_monster_a,(ex,550))
            offset = (ninja_x - ex,ninja_y - 550)
            collide = a_mask.overlap(idel_mask,offset)
            if (collide):
                if(state == attacking):
                    enemy[3] = 0
                    ex =1000
                    ex2 = ex+300
                else:
                    death(ninja_x,ninja_y)
                
            window.blit(bat,(ex2,440))
            offset = (ninja_x - ex2,ninja_y - 550)
            collide = bat_mask.overlap(idel_mask,offset)
            #If ninja is sliding
            #Bat appears
            if(sound_flag[1]):
                bat_sound = pygame.mixer.Sound('ninja_sound/bat.mp3')
                bat_sound.play()
                sound_flag[1] = 0 
            if (state == slide_forward or state == slide_backward):
                collide = 0
            if (collide):
                death(ninja_x,ninja_y)
            ex -= enemy_speed
            ex2 -= enemy_speed
            if(ex2 <= -100):
                ex =1000
                ex2 = ex+350
                enemy[3] = 0

        #5th enemy two spiky monsters
        if(enemy[4] and ox[4] <= 700):
            window.blit(spiky_monster_a,(ex,550))
            window.blit(spiky_monster_b,(ex2,550))
            offset = (ninja_x - ex,ninja_y - 550)
            collide = a_mask.overlap(idel_mask,offset)
            
            if (collide):
                if(state == attacking):
                    enemy[4] = 0
                    ex =1000
                    ex2 = ex+200
                else:
                    death(ninja_x,ninja_y)
            
            offset = (ninja_x - ex2,ninja_y - 550)
            collide = b_mask.overlap(idel_mask,offset)
            if (collide):
                if(state == attacking):
                    enemy[4] = 0
                    ex =1000
                    ex2 = ex+200
                else:
                    death(ninja_x,ninja_y)
                    
            ex -= enemy_speed
            ex2 -= enemy_speed
            if(ex2 <= -100):
                ex =1000
                ex2 = ex+200
                enemy[4] = 0

        #6th enemy ghost
        if(enemy[5] and ox[5] <= 500):
            window.blit(ghost,(ex,500))
            offset = (ninja_x - ex,ninja_y - 500)
            collide = ghost_mask.overlap(idel_mask,offset)
            if(collide):
                if(state == attacking):
                    enemy[5] = 0
                    ex =1000
                    ex2 = ex+200
                else:
                    death(ninja_x,ninja_y)
            if(sound_flag[3]):
                ghost_sound = pygame.mixer.Sound('ninja_sound/ghost.mp3')
                ghost_sound.play()
                sound_flag[3] = 0
            ex -= enemy_speed+2
            if(ex <= -200):
                ex =1000
                ex2 = ex+200
                enemy[5] = 0

        #7th enemy ghost
        if(enemy[6] and o_x[8] <= 500):
            window.blit(ghost,(ex,500))
            offset = (ninja_x - ex,ninja_y - 500)
            collide = ghost_mask.overlap(idel_mask,offset)
            if(collide):
                if(state == attacking):
                    enemy[6] = 0
                    ex =1000
                    ex2 = ex+200
                else:
                    death(ninja_x,ninja_y)
            if(sound_flag[4]):
                ghost_sound = pygame.mixer.Sound('ninja_sound/ghost.mp3')
                ghost_sound.play()
                sound_flag[4] = 0
            ex -= enemy_speed+2
            if(ex <= -200):
                ex =1000
                ex2 = ex+200
                enemy[6] = 0

        
                
        
        #Victory
        if(o_x[9]<= -1500):
            window.blit(castle,(castle_x,100))
            castle_x -= move_x
            if(castle_x <= 170):
                victory()
            
        
        
        #Displaying kunai
        for j in range(len(kunai_list)):
            window.blit(kunai,(kunai_list[j][0],kunai_list[j][1]))

        kunai_list = update_kunai(kunai_list)
        if(len(kunai_list)  and kunai_list[0][0] >= 1000):
            del kunai_list[0]
            
       
        #Ninja running
        ninja_x += move_x
        #Ninja climbing
        if (state == climbing):
            ninja_y += move_y  
        #TO restrict ninja in window
        if (ninja_x >= 400):
            ninja_x = 400
        if (ninja_x <= 5):
            ninja_x = 5
        if (ninja_y >= 500):
            ninja_y = 500
        #Displaying ninja state
        window.blit(state[i],(ninja_x,ninja_y))
        if(i >= 9):
            i=0 
        i += 1
        #Keeping ninja on a ground 
        if (ninja_y <= 500 and not(catch)):
            ninja_y += 10
            # If ninja is on the ground change state to rest and set jump flag to false
            if (ninja_y == 500 and not(catch)):
                jmp = 0
                state = rest
        #Gliding ninja on higher altitude
        if(ninja_y <= 100):
            state = gliding 
        
            
       
        pygame.display.update()
        clk.tick(30)



def start_game():
    start = pygame.image.load('ninja_sprites/start.png')
    start = pygame.transform.scale(start,(1000,700)).convert_alpha()
    window.blit(start,(0,0))
    pygame.mixer.music.load('ninja_sound/start.mp3')
    pygame.mixer.music.play(-1)
    pygame.display.update()
    while(1):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_KP_ENTER) :
                    game_on()
                    
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_ESCAPE) :
                    pygame.quit()
                    quit()
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_v) :
                    victory()
    

start_game()




