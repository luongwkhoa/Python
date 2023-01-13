import pygame, random

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
pygame.display.set_caption('Flappy Bird')
img = pygame.image.load('FlappyBird/Img/Flappy_Bird_icon.png')
pygame.display.set_icon(img)
screen= pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('FlappyBird/Font/Flappy_Bird.ttf',35)

#Background
bg = pygame.image.load('FlappyBird/Img/background.png').convert()
bg = pygame.transform.scale2x(bg)

#Bot
floor = pygame.image.load('FlappyBird/Img/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#Bird
bird_down = pygame.transform.scale2x(pygame.image.load('FlappyBird/Img/downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('FlappyBird/Img/midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('FlappyBird/Img/upflap.png').convert_alpha())
bird_list= [bird_down,bird_mid,bird_up] #0 1 2
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,384))

#Timer of Bird 
birdflap = pygame.USEREVENT
pygame.time.set_timer(birdflap, 1)

#Pipe
pipe_surface = pygame.image.load('FlappyBird/Img/pipe.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list =[]

#Timmer pipe
spawnpipe= pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1000)
pipe_height = [200, 300, 400]

#End Game Screen
game_over_surface = pygame.transform.scale2x(pygame.image.load('FlappyBird/Img/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(216,384))

#Sound
flap_sound = pygame.mixer.Sound('FlappyBird/Sound/wing.wav')
hit_sound = pygame.mixer.Sound('FlappyBird/Sound/hit.wav')
score_sound = pygame.mixer.Sound('FlappyBird/Sound/point.wav')
score_sound_countdown = 100

#Variable
gravity = 0.25 #gravitation
bird_movement = 0 #movement
game_active = True #run
score = 0 #score player
high_score = 0

def Draw_Floor(): #Vẽ cỏ bên dưới
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))

def Create_Pipe(): #Tạo các đường ống
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop =(500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop =(500,random_pipe_pos-650))
    return bottom_pipe, top_pipe

def Draw_Pipe(pipes): #Vẽ các đường ống
    for pipe in pipes:
        if pipe.bottom >= 600 : 
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def Check_Collision(pipes): #Phát hiện và kiểm tra va chạm
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True
    
def Move_Pipe(pipes): #Di chuyển của các đường ống
	for pipe in pipes :
		pipe.centerx -= 5
	return pipes 

def Rotate_Bird(bird1): #Di chuyển của Bird
	new_bird = pygame.transform.rotozoom(bird1, -bird_movement * 1, 1)
	return new_bird

def Bird_Animation(): #Hiệu ứng của Bird
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect

def Score_Display(game_state): #Hiển thị điểm
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)

    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,50)) #Score postion
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (216,120)) #High Score postion
        screen.blit(high_score_surface,high_score_rect)

def Update_Score(score,high_score): #Kiểm tra và cập nhật điểm cao nhất
    if score > high_score:
        high_score = score
    return high_score

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement =-7
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                game_active = True 
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0 
                score = 0 

        if event.type == spawnpipe:
            pipe_list.extend(Create_Pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index =0 
            bird, bird_rect = Bird_Animation()    
            
    screen.blit(bg,(0,0))
    if game_active:
        #Bird
        bird_movement += gravity
        rotated_bird = Rotate_Bird(bird)       
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active= Check_Collision(pipe_list)
        
        #Pipe
        pipe_list = Move_Pipe(pipe_list)
        Draw_Pipe(pipe_list)
        score += 0.01
        Score_Display('main game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = Update_Score(score,high_score)
        Score_Display('game_over')

    #Bot
    floor_x_pos -= 1
    Draw_Floor()
    if floor_x_pos <= -432:
        floor_x_pos =0
    
    pygame.display.update()
    clock.tick(120)