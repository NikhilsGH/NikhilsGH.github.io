import pygame
import random
pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))
canvas.fill((0, 50, 100))
x = 0
y = 0
speed_x = 0.1
speed_y = 0.1

# TITLE OF CANVAS
pygame.display.set_caption("Nikhils game")
exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    
    x += speed_x 
    y += speed_y
    
    if x <= 0 or x >= 500:
        speed_x = -speed_x
    if y <= 0 or y >= 500:
        speed_y = -speed_y
    
    canvas.fill((0, 50, 100))
    pygame.draw.circle(canvas, (255, 165, 0), (x, y), 20)
    
    pygame.display.update()


pygame.quit()
