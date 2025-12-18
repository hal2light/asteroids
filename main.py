import pygame
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroidfield import *
import sys
from shot import *




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        dt = clock.tick(60) / 1000
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
                       

if __name__ == "__main__":
    main()
