import pygame
import main
import src.nodes as nodes

current_line = []
all_lines = pygame.sprite.Group()

class Line(pygame.sprite.Sprite):
    def __init__(self, startNode = None, endNode = None, length = 0):
        pygame.sprite.Sprite.__init__(self, all_lines)
        self.image = pygame.Surface((abs(endNode.posx-startNode.posx), abs(endNode.posy-startNode.posy)), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.startNode = startNode
        self.endNode = endNode
        self.length = length
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        
    def _draw_line(self):
        if self.startNode != None and self.endNode != None: # Draws a line if both start and end node are present
            pygame.draw.line(main.SCREEN, (255,255,255), (self.startNode.posx, self.startNode.posy), (self.endNode.posx, self.endNode.posy), main.LINE_WIDTH)