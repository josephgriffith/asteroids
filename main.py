import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from random import randrange
from time import sleep

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
    font = pygame.font.Font('/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf', 32)
    

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    ordinance = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, rocks)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, ordinance)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # print(player.containers)
    # sizes = [4,8,16,32]
    # asteroids = Asteroid(randrange(0, SCREEN_WIDTH), randrange(0, SCREEN_HEIGHT), randrange(8, 32, 8))
    field = AsteroidField()

    playing = True
    while playing:
        # event = pygame.event.poll()
        # if event.type == pygame.QUIT:
        #     playing = False
        frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((128,16,255))
        screen.blit(font.render(str(frames), False, (32, 32, 32)), (20,20))
        screen.blit(font.render(str(player.rotation), False, (32, 32, 32)), (20,40))

        for u in updatables:
            u.update(dt)
        for r in rocks:
            if player.collision(r):
                screen.blit(font.render('YOU DIED.', False, (255, 128, 128)), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                sleep(3)
                sys.exit('Game over!')
        for d in drawables:
            d.draw(screen)

        # print(player.position)

        pygame.display.flip()
        dt = clock.tick(30)/1000
    while True:
        pass

















if __name__ == "__main__":
    main()