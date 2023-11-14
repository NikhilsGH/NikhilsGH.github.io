import pygame
import math

pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((800, 500))
colour = (103, 230, 240)
canvas.fill(colour)

# TITLE OF CANVAS
pygame.display.set_caption("Nikhil's Game")
exit_game = False

# Define sun parameters
sun_radius = 60
radius = 600  # Increased radius for the circular motion
speed = 0.0009  # Speed of the circular motion
time = 0

  # Speed of the circular motion


while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    # Update sun position in a circular motion on the top sector
    sun_x = int(radius * math.cos(speed * time)) + 400  # Circular motion along x-axis
    sun_y = int(radius * math.sin(speed * time)) + 600  # Circular motion along y-axis
    moon_x = int((int(radius * math.cos(speed * time)) + 400) - 800)  # Circular motion along x-axis
    moon_y = int((int(radius * math.sin(speed * time)) + 600) - 600)  # Circular motion along y-axis
    print(sun_x)
    canvas.fill((103, 230, 240))
    if sun_x > 800:
        canvas.fill((0,0,0))
        pygame.draw.circle(canvas, (127, 127, 127), (moon_x, moon_y), sun_radius)
    else:
        pygame.draw.circle(canvas, (255, 255, 0), (sun_x, sun_y), sun_radius)

    # Update time for circular motion
        # Clear canvas
        # Draw door

    

    pygame.draw.rect(canvas, (170, 74, 68), [200, 300, 350, 200], 0)
    pygame.draw.polygon(canvas, (170, 74, 68), [(200, 300), (550, 300), (375, 100)])

    pygame.draw.rect(canvas, (100, 50, 0), [350, 400, 50, 100])
    # Draw windows
    pygame.draw.rect(canvas, (255, 255, 255), [250, 330, 50, 50])
    pygame.draw.rect(canvas, (255, 255, 255), [475, 330, 50, 50])

    # Draw garden
    pygame.draw.rect(canvas, (0, 255, 0), [0, 400, 200, 100])
    pygame.draw.rect(canvas, (0, 255, 0), [550, 400, 250, 100])


    time += 1

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()