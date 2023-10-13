import pygame

pygame.init()

FPS = 60

clock = pygame.time.Clock()

def main():
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event. type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()