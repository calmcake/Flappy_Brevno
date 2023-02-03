# Flappy brevno - копия игры "Flappy Bird"
# Код достаточно плохой, так как это первый "серьзный" проект

import pygame 
import sys
from random import randint

pygame.init()

f1 = pygame.font.Font(None, 40)
f2 = pygame.font.Font(None, 60)
game_over = f1.render("ИГРА ОКОНЧЕНА ВЫ ПРОИГРАЛИ", True, (255, 0, 0))
counter = 0
scree = pygame.display.set_mode((800, 800))
hero = pygame.image.load('sprites/calm_state.png')
bg = pygame.image.load('sprites/bg.png')
pipe_down = pygame.image.load('sprites/pipe_down.png')
pipe_up = pygame.image.load('sprites/pipe_up.png')


game_state = True
y_hero_position = 0
x_pipe_position = 800
possible_pipe_positions = [[-280, 650], [-430, 430], [-150, 690]]
y_pipes_position = possible_pipe_positions[randint(0, 2)]


scree.blit(hero, (30, y_hero_position))

while True:
    gravity = 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not (y_hero_position <= 10):
                    hero = pygame.image.load('sprites/jump.png')
                    y_hero_position -= 90
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                hero = pygame.image.load('sprites/calm_state.png')
 
    if y_hero_position <= 800 - 129 and game_state:
        y_hero_position += gravity
        x_pipe_position -= 1
        counter_str = f2.render(str(counter), True, (255, 255, 255))

        scree.blit(bg, (0, 0))
        scree.blit(pipe_up, (x_pipe_position, y_pipes_position[0]))
        scree.blit(pipe_down, (x_pipe_position, y_pipes_position[1]))
        scree.blit(hero, (30, y_hero_position))
        scree.blit(counter_str, (20, 20))

        if x_pipe_position - 171 == 30:
            counter += 1

        if x_pipe_position == -126:
            x_pipe_position = 800
            y_pipes_position = possible_pipe_positions[randint(0, 2)]

    else:
        gravity = 0
    
    if (y_hero_position <= y_pipes_position[0] + 600) and x_pipe_position == 171:
        game_state = False
        scree.fill((0, 0, 0))
        scree.blit(game_over, (200, 200))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = True
                    x_pipe_position = 800
                    y_hero_position = 0
                    counter = 0   

    elif (y_hero_position >= y_pipes_position[1] - 129) and x_pipe_position == 171:
        game_state = False
        scree.fill((0, 0, 0))
        scree.blit(game_over, (200, 200))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = True
                    x_pipe_position = 800
                    y_hero_position = 0
                    counter = 0   

    pygame.display.update()




# w - 171
# h - 129