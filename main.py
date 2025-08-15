from menu import Menu
import pygame
pygame.init()

# clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Tetris")
icon = pygame.image.load('pictures/tetris.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('pictures/back.png')


menu = Menu(screen, 700, 700)
project_running = True
game_running = False

while project_running:
    if not game_running:
        menu.draw()
        action = menu.handle_events()
        if action == "Start Game":
            game_running = True
        elif action == "Quit":
            project_running = False
            pygame.quit()
    else:
        pass
