import pygame
import main

class Node(pygame.sprite.Sprite):
    def __init__(self, posx, posy, rad, label):
        pygame.sprite.Sprite.__init__(self, main.all_nodes) # Initialises Sprite object and adds to all_nodes
        self.image = pygame.Surface((rad*2,rad*2))
        self.rect = self.image.get_rect(center=(posx, posy))
        self.posx = posx
        self.posy = posy
        self.radius = rad
        self.label = label
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        
    def _remove_node(self):
        main.all_nodes.remove(self) # Removes node
        
    def _draw_node(self):
        # Clear the image surface
        self.image.fill((0, 0, 0, 0))  # Fills the surface with a fully transparent color

        # Draw the circle on the image
        pygame.draw.circle(self.image, (0, 255, 0), (self.image.get_width() // 2, self.image.get_height() // 2), self.radius)

        # Draw the text on the image
        text_surface = self.font.render(str(self.label), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
        self.image.blit(text_surface, text_rect)

        # Update the rect to match the new image size
        self.rect = self.image.get_rect(center=self.rect.center)

        # Blit the image onto the main display
        main.SCREEN.blit(self.image, self.rect.topleft)
        
    def __repr__(self):
        return f"{self.label}"
        