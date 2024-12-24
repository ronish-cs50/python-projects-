import random
import pygame
import time
import threading

#initializes pygame
pygame.init()

#creates a screen in the main window of 500x500
screen = pygame.display.set_mode((500,500))
running = True
enemies = [] #all the enemies
fonts = pygame.font.SysFont("comicsans", 20)
ENEMY_WIDTH, ENEMY_HEIGHT = 30, 30
ENEMY_COLOR = (200,10,10)
FPS = 60
clock = pygame.time.Clock()

def render_points(points):
    
    text = fonts.render(f"Points: {points}", 1, (255,255,255))
    screen.blit(text, (10,10))
        
def show_enemy():
    #draws all the enimies in the list on screen
    
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)

#creates enemy
def create_enemy():
    while True:
        x = random.randint(0,450)
        y = random.randint(0,450)
        enemy = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT) #creates an enemy rectangle
        enemies.append(enemy) #adds the enemy to the list of enemies
        time.sleep(1) #waits 1 seconds before creating another enemy

def main():
    points = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                for enemy in enemies:
                    if enemy.collidepoint(pygame.mouse.get_pos()):
                        enemies.remove(enemy)
                        points += 1
            if len(enemies) >= 10:
                phrase = fonts.render("Game Over", 1, (255,255,255))
                screen.blit(phrase, (200,200))
                pygame.display.flip()
                time.sleep(3)
                points = 0
                enemies.clear()

        screen.fill((0, 0, 0))
        render_points(points)
        show_enemy()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    while running:
        phrase = fonts.render("Click to start", 1, (255,255,255))
        for event in pygame.event.get():
            screen.blit(phrase, (200,200))
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                enemy_thread = threading.Thread(target=create_enemy)
                enemy_thread.daemon = True
                enemy_thread.start()
                main()
                break
        pygame.display.flip()
               