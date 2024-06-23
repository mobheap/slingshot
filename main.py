import pygame
import math
from game.planet import Planet
from game.spacecraft import Spacecraft

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1600, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot")

PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 500
PLANET_SIZE = 50
OBJ_SIZE = 5
VEL_SCALE = 100

BG = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET_IMAGE = pygame.image.load("assets/jupiter.png")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.mixer.music.load("assets/space-ambience.mp3")
pygame.mixer.music.play(-1)

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    return Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS, OBJ_SIZE, RED)

def main():
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS, PLANET_IMAGE, PLANET_SIZE)
    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)

        for obj in objects[:]:
            obj.draw(win)
            obj.move(planet, G)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x) ** 2 + (obj.y - planet.y) ** 2) <= PLANET_SIZE
            if off_screen or collided:
                objects.remove(obj)

        planet.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
