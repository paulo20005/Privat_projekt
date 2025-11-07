import pygame
import random

class Snake:
    def __init__(self):
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = "RIGHT"
    
    def move(self):
        head = self.body[0]
        if self.direction == "RIGHT":
            new_head = (head[0] + 10, head[1])
        # ... rest of movement logic
        self.body.insert(0, new_head)
        self.body.pop()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.snake = Snake()
        self.food = self.spawn_food()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        # Draw snake
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
        # Draw food
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food[0], self.food[1], 10, 10))
        pygame.display.update()