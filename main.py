import pygame
from constants import *

def main():
    print('Starting asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    frames = 0
    pygame.font.init()
    font = pygame.font.SysFont('Consolas', 32)
    
    playing = True
    while playing:
        # event = pygame.event.poll()
        # if event.type == pygame.QUIT:
        #     playing = False
        frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((127,127,255))
        txt = font.render(str(frames), False, (32, 32, 32))
        screen.blit(txt, (20,20))
        pygame.display.flip()

        dt = clock.tick(30)/1000


















if __name__ == "__main__":
    main()