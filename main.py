import pygame
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Tetris")
icon = pygame.image.load('pictures/tetris.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('pictures/back.png')
bg_x = 0


run_program = True
while run_program:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 700, 0))

    pygame.display.update()

    bg_x -= 0.6
    if bg_x == -700:
        bg_x = 0

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run_program = False

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_p or i.key == pygame.K_y or i.key == pygame.K_g or i.key == pygame.K_a or i.key == pygame.K_m or i.key == pygame.K_e:
                print(pygame.key.name(i.key))

        # if i.type == pygame.MOUSEBUTTONDOWN:
        #     my_pos = i.pos
        #     my_button = i.button
        #     print(f"Позиция мыши: {my_pos}")
        #     print(f"Идентификатор кнопки мыши: {my_button}")
        clock.tick(20)


pygame.quit()
