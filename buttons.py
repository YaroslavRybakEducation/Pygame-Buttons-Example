import pygame

class Buttons:
    def __init__(self, x, y, width, height, img_path, hover_path = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.hover_image = self.image

        if hover_path:
            self.hover_image = pygame.image.load(hover_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

        self.rect = self.image.get_rect(topleft = (x, y))
        self.is_hovering = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovering else self.image
        screen.blit(current_image, (self.rect.topleft))

    def check_hover(self, pos):
        self.is_hovering = self.rect.collidepoint(pos)

    def event_handling(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovering:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))