# import pygame
 
# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#   for event in pygame.event.get():
#    if event.type == pygame.QUIT\
#    or event.type == pygame.MOUSEBUTTONUP\
#    or event.type == pygame.KEYUP:
#     run = False

import pygame
import random
 
# Initialisierung von pygame
pygame.init()
 
# Bildschirmgröße und Spielfeldparameter
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PLANE_WIDTH = 50
PLANE_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
 
# Farben
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
 
# Flugzeug-Klasse
class Plane:
    def __init__(self):
        self.image = pygame.Surface((PLANE_WIDTH, PLANE_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
 
    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - PLANE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLANE_WIDTH
 
# Hindernis-Klasse
class Obstacle:
    def __init__(self, x):
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, 0))
 
    def move(self):
        self.rect.y += 5
 
# Hauptspiel-Schleife
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flugzeugspiel")
clock = pygame.time.Clock()
plane = Plane()
obstacles = []
score = 0
 
# Hindernisse generieren
def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    obstacles.append(Obstacle(x))
 
# Spiel-Loop
running = True
while running:
    screen.fill(BLACK)
    screen.blit(plane.image, plane.rect)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plane.move(-5)
    if keys[pygame.K_RIGHT]:
        plane.move(5)
 
    for obstacle in obstacles[:]:
        obstacle.move()
        screen.blit(obstacle.image, obstacle.rect)
 
        # Überprüfung auf Kollision mit dem Flugzeug
        if obstacle.rect.colliderect(plane.rect):
            print(f"Spiel beendet! Dein Score: {score}")
            running = False
 
        # Hindernisse entfernen, wenn sie den Bildschirm verlassen haben
        if obstacle.rect.y > SCREEN_HEIGHT:
            obstacles.remove(obstacle)
            score += 1
 
    # Zufällige Hindernisse generieren
    if random.randint(1, 20) == 1:
        create_obstacle()
 
    # Score anzeigen
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
 
    pygame.display.flip()
    clock.tick(30)
 
pygame.quit()