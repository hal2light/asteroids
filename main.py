import pygame
from constants import *
from logger import log_state
from player import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2, PLAYER_RADIUS)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        dt = clock.tick(60) / 1000
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
                       

if __name__ == "__main__":
    main()
