from GUI.GameGUI import *


def draw_text(text, screen_, x, y):
    font_ = pygame.font.SysFont('', 20)
    text_obj = font_.render(text, True, BLACK)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    screen_.blit(text_obj, text_rect)


class Button:
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = BLACK
        self.clicked = False
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), outline)
            pygame.draw.rect(screen, self.color, (self.x + outline, self.y + outline, self.width - (outline * 2),
                                                  self.height - (outline * 2)))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            text_x = self.x + (self.width / 2)
            text_y = self.y + (self.height / 2)
            draw_text(self.text, screen, text_x, text_y)

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def button_event(self, event_):
        pos = pygame.mouse.get_pos()
        if event_.type == pygame.MOUSEBUTTONDOWN:
            if self.is_over(pos):
                self.clicked = True
        if event_.type == pygame.MOUSEMOTION:
            if self.is_over(pos):
                self.text.color = LIGHT_RED
            else:
                self.text.color = BLACK
