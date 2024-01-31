import pygame
import src.nodes as nodes

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

CIRC_RAD = 30

all_nodes = pygame.sprite.Group()

def update():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                newNode = nodes.Node(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], CIRC_RAD, len(all_nodes.sprites()))
                # Check for collisions without removing sprites
                collide = pygame.sprite.spritecollide(newNode, all_nodes, dokill=False)
                # If there are no collisions, draw the node
                print("We are here")
                if not collide:
                    print("We here")
                    newNode._draw_node()
                    # Add the new node to the group
                    all_nodes.add(newNode)
                else:
                    newNode._remove_node()

                break

        # Update the display outside of the event loop
        pygame.display.flip()
        CLOCK.tick(30)
            
    pygame.quit()

def display():
    pygame.init()
    update()

if __name__ == "__main__":
    display()
