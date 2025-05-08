import pygame
import random
import os

# Colors should be present in (r,g,b) format
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Snake variables
snake_x = 200
snake_y = 200
snake_length = 10
snake_width = 10
velocity_x = 0
velocity_y = 0
fps = 50    # Low fps tends to less changes on screen but hight fps need higher processing. So, fps should be medium

# Food variables
food_x = random.randint(0,900)
food_y = random.randint(0,500)

# Clock variable changes screen with time
clock = pygame.time.Clock()

# initializing the pygame
pygame.init()

game_window = pygame.display.set_mode((900,500))
pygame.display.set_caption("Snake Game")
pygame.display.update()

# game variables
game_over = False
game_quit = False

# score variable
score = 0
print(f"Current Score:  {10*score}")

# function to show score on game screen
font = pygame.font.SysFont(None,30)

def show_score(text, color, x, y):
    # 2nd paramater (AntiAliasing) : high to low rsolution conversion
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

while not game_quit:

    # To convert the black screen into white screen
    game_window.fill(white)
    show_score(f"Score: {score}", red, 20, 20)

    # pygame.draw.rect(current_game_window, rectangle_color, x_coordinate, y_coordinate, rectangle_length, rectangle_right)
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_length, snake_width])
    pygame.draw.rect(game_window, red, [food_x, food_y, 10, 10])
    pygame.display.update()

    # Some event generation
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_quit = True

        # Handling direction key events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0
            elif event.key == pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
            elif event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 5
            elif event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -5
        
    # Changing the position of snake
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y 

    # Resetting the snake positions if snake goes out of window
    if snake_x < 0:
        snake_x = 900
    elif snake_x > 900:
        snake_x = 0
    elif snake_y < 0:
        snake_y = 500
    elif snake_y > 500:
        snake_y = 0

    # Logic for eating the food
    if abs(snake_x-food_x)<=6 and abs(snake_y-food_y) <=6:
        score = score + 10
        food_x = random.randint(0,900)
        food_y = random.randint(0,500)

    # setting the frames per second (fps) for clock variable
    clock.tick(fps)

pygame.quit()
quit()