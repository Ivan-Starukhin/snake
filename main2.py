import pygame
import random as r
import time
from game_info import game_info
from game_info import point2d
from game_processor import game_processor
import visualizer2

field_size = 500
count_barriers_foods = 30
fps = 10 #speed
time_begin = time.time()

game = game_info(i_field_size=field_size)

#create random barriers and food
for _ in range(count_barriers_foods):
    pair1 = [r.randrange(1, field_size//10)*10, r.randrange(1, field_size//10)*10]
    pair2 = [r.randrange(1, field_size//10)*10, r.randrange(1, field_size//10)*10]
    game.food.append(point2d(pair1[0], pair1[1]))
    game.barriers.append(point2d(pair2[0], pair2[1]))   

#delete food matching with barriers
for item in game.barriers:
    if item in game.food:
        game.food.remove(item) 

processor = game_processor()

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)

#create the window
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 50)
pygame.init()

text_surface = my_font.render("Let`s play!", False, red)
screen = pygame.display.set_mode((field_size, field_size))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

screen.fill(white)
screen.blit(text_surface, text_surface.get_rect(center=(field_size/2, field_size/2)))
visualizer2.draw_things(game, screen)
visualizer2.draw_snake(game, screen)
pygame.display.update()
clock.tick(3)
time.sleep(3)

command='down'
#main block
while game.is_valid:    
    screen.fill(white)

    game = processor.run(game, command)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.is_valid = False
            print('quit')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                command = 'down'

            if event.key == pygame.K_DOWN:
                command = 'up'

            if event.key == pygame.K_LEFT:
                command = 'left'

            if event.key == pygame.K_RIGHT:
                command = 'right'

            if event.key == pygame.K_RETURN:
                game.is_valid = False
                print("enter")
            if event.key == pygame.K_SPACE:
                fps+=5

    pygame.event.clear()

    #add new food
    if len(game.food) < 20:
        pair = [r.randrange(1, field_size//10)*10, r.randrange(1, field_size//10)*10]
        game.food.append(point2d(pair[0], pair[1]))

    #visualize the snake and field
    visualizer2.draw_things(game, screen)
    visualizer2.draw_snake(game, screen)
    #show game time
    timing = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface = timing.render(f'Game time: {(time.time() - time_begin):.0f}', True, (200,200,200))
    screen.blit(text_surface, (10, 10))

    pygame.display.update()
    clock.tick(fps)

text_surface = my_font.render("Game over!", False, (200,20,20))
screen.blit(text_surface, text_surface.get_rect(center=(field_size/2, field_size/2)))
pygame.display.update()
clock.tick(2)
pygame.quit()
quit()
