import pygame
import random

pygame.init()

# Constants 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYZER_SIZE = 20
RESOURCE_SIZE = 10
ENEMY_SIZE = 20
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK= (0,0,0)

ENEMYSPEED = 5
PLAYERSPEED = 10

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


# player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y =y
        self.color = WHITE
        self.health = 100

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,PLAYZER_SIZE, PLAYZER_SIZE))

    def move(self,x,y):
        self.x += x
        self.y += y


# Reasource class
class Reascource:
    def __init__(self):
        self.x = random.randint(0,SCREEN_WIDTH - RESOURCE_SIZE)
        self.y = random.randint(0,SCREEN_HEIGHT- RESOURCE_SIZE)
        self.color = RED

    def draw(self):
        pygame.draw.rect(screen, self.color,(self.x , self.y, RESOURCE_SIZE, RESOURCE_SIZE))

    #ENEMY CLASS
class Enemy:
    def __init__(self):
        self.x = random.randint(0,SCREEN_WIDTH - ENEMY_SIZE)
        self.y = random.randint(0,SCREEN_HEIGHT-ENEMY_SIZE)
        self.color = GREEN
        self.speed = ENEMYSPEED

    def draw(self):
        pygame.draw.rect(screen, self.color,(self.x , self.y, ENEMY_SIZE,ENEMY_SIZE))

    def move(self):
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)