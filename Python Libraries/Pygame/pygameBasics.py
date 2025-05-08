import pygame

x = pygame.init()

game_window = pygame.display.set_mode((800,500))
pygame.display.set_caption("My first game")
pygame.display.update()

# game variables
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            print("Exit Key Pressed!")
            exit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left Key Pressed!")
            elif event.key == pygame.K_RIGHT:
                print("Right Key Pressed!")
            elif event.key == pygame.K_UP:
                print("UP Key Pressed!")
            elif event.key == pygame.K_DOWN:
                print("DOWN Key Pressed!")

pygame.quit()
quit()