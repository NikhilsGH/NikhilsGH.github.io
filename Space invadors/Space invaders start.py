import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders Formation")

# Define colors
green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define Box class
class Box(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()


        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Invader(Box):
    def __init__(self, color, width, height, x, y):
        super().__init__(color, width, height)


        self.rect.x = x
        self.rect.y = y
        self.direction = 1  # Initial direction (1 for right, -1 for left)

    # Method to move the invader left or right
    def move(self):
        self.rect.x += self.direction * 5  # Adjust the movement speed as needed


        if self.rect.left < 0 or self.rect.right > width:
            self.rect.y += 50 
            self.direction *= -1 

# Create a shooter sprite
class Shooter(Box):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.rect.x = 350  #
        self.rect.y = 575 

class Shield(Box):
    def __init__(self, color, width, height, x, y):
        super().__init__(color, width, height)
        self.rect.x = x
        self.rect.y = y

all_sprites = pygame.sprite.Group()


invader_width, invader_height = 50, 50
rows, cols = 3, 8
spacing = 50 

invaders = []

for row in range(rows):
    for col in range(cols):
        x = col * (invader_width + spacing)
        y = row * (invader_height + spacing)
        invader = Invader(green, invader_width, invader_height, x, y)
        all_sprites.add(invader)
        invaders.append(invader)


shooter_width, shooter_height = 50, 20
shooter = Shooter(white, shooter_width, shooter_height)
all_sprites.add(shooter)


shield_width, shield_height = 100, 50
shield_spacing = 200

for i in range(4):
    x = i * (shield_width + shield_spacing)
    y = height - shield_height - spacing  
    shield = Shield(red, shield_width, shield_height, x, y)
    all_sprites.add(shield)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    for invader in invaders:
        invader.move()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        shooter.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        shooter.rect.x += 5

    all_sprites.update()

    screen.fill((44, 45, 90))  
    all_sprites.draw(screen)  

    pygame.display.flip()


    pygame.time.Clock().tick(60)
