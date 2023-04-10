import pygame
import time
import random


pygame.init()

#rgb colors
green = (0, 255, 0)
red = (255, 0 ,0)
black = (0, 0 ,0)
white = (255, 255, 255)

#window size
width = 800
height = 600

#snake properties
snake_block = 10
snake_speed = 20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python Snake by MariusB5")
font_style = pygame.font.SysFont('Courier', 20)
clock = pygame.time.Clock()


def message(text, color):
    message_var = font_style.render(text, True, color)
    screen.blit(message_var, [170, 280])


def game_loop():
    #the game function
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_moved = 0
    y1_moved = 0

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            screen.fill(black)
            message('GAME OVER! Press Q to quit or R to restart', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            #print(event)
            #prints in the console every action from the program

            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                #KEYDOWN referring to any key from the keyboard
                if event.key == pygame.K_LEFT:
                    x1_moved = -snake_block
                    y1_moved = 0
                elif event.key == pygame.K_RIGHT:
                    x1_moved = snake_block
                    y1_moved = 0
                elif event.key == pygame.K_UP:
                    y1_moved = -snake_block
                    x1_moved = 0
                elif event.key == pygame.K_DOWN:
                    y1_moved = snake_block
                    x1_moved = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_moved
        y1 += y1_moved
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(screen, green, [x1, y1, snake_block, snake_block])
        #[] first two numbers is the position on the screen
        #[] second two numbers is the size of the rectangle
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print ("Tasty!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
