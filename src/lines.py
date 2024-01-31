import pygame
import main
import src.nodes as nodes

all_lines = pygame.sprite.Group()
current_line = []

class Line(pygame.sprite.Sprite):
    def __init__(self, startNode = None, endNode = None):
        pygame.sprite.Sprite.__init__(self, all_lines)
        self.startNode = startNode
        self.endNode = endNode
        
    def _draw_line(self):
        if self.startNode != None and self.endNode != None:
            pygame.draw.line(main.SCREEN, (255,255,255), (self.startNode.posx, self.startNode.posy), (self.endNode.posx, self.endNode.posy), main.LINE_WIDTH)