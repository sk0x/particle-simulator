import pygame
from pygame.locals import *
import physicsim

def main():
    pygame.init()
    width, height = 1000, 800
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    env = physicsim.Enviroment(width, height)
    env.addParticle(11)
    selected_particle = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                selected_particle = env.findParticle()
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_particle = None

        screen.fill(env.color)
        for p in env.particles:
            pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), p.size, p.thickness)
            env.updateParticle()
            if selected_particle:
                x, y = pygame.mouse.get_pos()
                selected_particle.mouseMove(x, y)
        pygame.display.flip()
        clock.tick(60)
    return


if __name__ == "__main__":
    main()
