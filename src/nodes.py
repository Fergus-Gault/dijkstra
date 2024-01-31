import pygame
import main
import src.lines as lines
import math

class Node(pygame.sprite.Sprite):
    def __init__(self, posx, posy, rad, label):
        pygame.sprite.Sprite.__init__(self, main.all_nodes) # Initialises Sprite object and adds to all_nodes
        self.image = pygame.Surface((rad*2,rad*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(posx, posy))
        self.posx = posx
        self.posy = posy
        self.radius = rad
        self.label = label
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.rect.collidepoint(event.pos):
                    drawLine(self)
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                if self.rect.collidepoint(event.pos):
                    self._remove_node()
                    
        
    def _remove_node(self):
        main.all_nodes.remove(self) # Removes node
        
    def _draw_node(self):
        # Clear the image surface
        self.image.fill((0, 0, 0, 0))

        # Draw the circle on the image
        pygame.draw.circle(self.image, (0, 255, 0), (self.image.get_width() // 2, self.image.get_height() // 2), self.radius)

        # Draw the text on the image
        text_surface = self.font.render(str(self.label), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
        self.image.blit(text_surface, text_rect)

        # Update the rect to match the new image size
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def __repr__(self):
        return f"{self.label}"
        
def drawLine(node):
    if len(lines.current_line) == 1:
        dist = get_dist(lines.current_line[0], node)
        newLine = lines.Line(lines.current_line[0], node, dist)
        newLine._draw_line()
        lines.current_line = []
    else:
        lines.current_line.append(node)
        
def get_dist(node1, node2):
    return math.floor(math.sqrt(abs((node1.posx-node2.posx))^2+abs((node1.posy-node2.posy))^2))
    