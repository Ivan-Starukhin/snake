import pygame
import random as r

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)

def draw_things(game, screen):
    for i_barrier in game.barriers:
        pygame.draw.rect(screen, black, pygame.Rect(i_barrier.x, i_barrier.y, 10, 10))
        #pygame.draw.circle(screen, yellow, (i_food.x - 5, i_food.y - 5), 5)
    for i_food in game.food:
        pygame.draw.rect(screen, red, pygame.Rect(i_food.x, i_food.y, 10, 10))

def draw_snake(game, screen):
    for i in game.snake.location:
        pygame.draw.rect(screen, green, pygame.Rect(i.x, i.y, 10, 10))