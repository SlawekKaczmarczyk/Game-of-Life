import pygame
import random

pygame.init()

BLACK = (0,0,0)
GREY = (127,127,127)
ORANGE = (255,165,0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def generate(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0,GRID_WIDTH)) for _ in range(num)])


def draw_grid(positions):
    for position in positions:
        column, row = position
        top_left = (column * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, ORANGE, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK,(0, row * TILE_SIZE),(WIDTH, row * TILE_SIZE))
    
    for column in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK,(column * TILE_SIZE, 0),(column * TILE_SIZE, HEIGHT))


def main():
    running = True

    positions =set()
    positions.add((15,15))
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event. type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                column = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (column, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                
                if event.key == pygame.K_c: #clear position
                    positions = set()
                    playing = False

                if event.key == pygame.K_r: #random position generating
                    positions = generate(random.randrange(2,5) * GRID_WIDTH)
                    playing = False


        screen.fill(GREY)            
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()