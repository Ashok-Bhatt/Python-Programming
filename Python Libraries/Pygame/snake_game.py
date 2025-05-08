import pygame
import random
import os

# Colors should be present in (r,g,b) format
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# initializing the music
pygame.mixer.init()

# initializing the pygame
pygame.init()

game_window = pygame.display.set_mode((900,500))

pygame.display.set_caption("Snake Game")
pygame.display.update()

# function to show score on game screen
font = pygame.font.SysFont(None,30)

# Clock variable changes screen with time
clock = pygame.time.Clock()

def show_text(text, color, x, y):
    # 2nd paramater (AntiAliasing) : high to low rsolution conversion
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def draw_snake(gameWindow, snake_list, color, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():

    # Snake variables
    snake_x = 200
    snake_y = 200
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    fps = 30

    # Food variables
    food_x = random.randint(100,800)
    food_y = random.randint(100,400)

    # game variables
    game_over = False
    game_quit = False

    # score variable
    score = 0

    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt","w") as file:
            file.write("0")

    with open("high_score.txt","r") as file:
        high_score = file.read()

    # snake length variables
    snake_list = []
    snake_length = 1

    while not game_quit:
        
        if game_over:

            # Updating the high score to file
            with open("high_score.txt", "w") as file:
                file.write(high_score)

            game_window.fill(white)
            show_text("Game Over!", black, 100, 100)
            show_text("Press Enter to replay!", black, 100, 150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            # Some event generation
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_quit = True

                # Handling direction key events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x!=-5:
                        velocity_x = 5
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT and velocity_x!=5:
                        velocity_x = -5
                        velocity_y = 0
                    elif event.key == pygame.K_DOWN and velocity_y!=-5:
                        velocity_x = 0
                        velocity_y = 5
                    elif event.key == pygame.K_UP and velocity_y!=5:
                        velocity_x = 0
                        velocity_y = -5
                
            # Changing the position of snake
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y 

            # To convert the black screen into white screen
            game_window.fill(white)
            show_text(f"Score: {score}", red, 20, 20)
            show_text(f"High Score: {high_score}", red, 20, 50)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            # Logic for eating the food
            if abs(snake_x-food_x)<=6 and abs(snake_y-food_y)<=6:
                score = score + 10
                if (score > int(high_score)):
                    high_score = str(score)
                food_x = random.randint(100,800)
                food_y = random.randint(100,400)
                snake_length = snake_length + 5

            if len(snake_list) > snake_length:
                del snake_list[0]

            if snake_list[-1] in snake_list[:-1]:
                game_over = True

            # pygame.draw.rect(current_game_window, rectangle_color, x_coordinate, y_coordinate, rectangle_length, rectangle_right)
            # pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_length, snake_width])

            # Handling the collisions
            if (snake_x < 0 or snake_x>900 or snake_y<0 or snake_y>500):
                game_over = True

            pygame.draw.rect(game_window, red, [food_x, food_y, 10, 10])
            draw_snake(game_window, snake_list, black, snake_size)

        pygame.display.update()
        # setting the frames per second (fps) for clock variable
        clock.tick(fps)
    pygame.quit()
    quit()

gameloop()