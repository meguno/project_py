import pygame
pygame.init()

#clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Tetris")
#icon = pygame.image.load('pictures/tetris.png')
#pygame.display.set_icon(icon)

bg = pygame.image.load('pictures/back.png')


from shapes import Block

block = Block(0, 0, (255, 0, 0), 40)

# from field import Field
# field = Field(400, 400, 40)
# field.add_block(block)


run_program = True
while run_program:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run_program = False

    screen.blit(bg, (0, 0))

    block.draw(screen)
    
    pygame.display.update()


pygame.quit()
