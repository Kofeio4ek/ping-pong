import pygame
class Button():
    def __init__(
            self, x=0, y=0, width=10, height=10, text='Normal', color_normal=(0, 128, 0), 
            color_hover=(0, 100, 0), center_x=True, text_color=(75, 0, 130),
            font = 'Arial', font_size=20, border_radius=10
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.border_radius = border_radius
        self.font_name = font 
        self.font_size = font_size
        if center_x:
            w_width, w_height = pygame.display.get_window_size()
            window_rect = pygame.Rect(0, 0, w_width, w_height)
            self.rect.centerx = window_rect.centerx
        self.is_hovered = False

    def draw(self, window):
        text_font = pygame.font.SysFont(self.font_name, self.font_size)
        text_image = text_font.render(self.text, True, self.text_color)
        text_rect = text_image.get_rect()
        text_rect.center = self.rect.center
        if self.is_hovered:
            color = self.color_hover
        else:
            color = self.color_normal
        pygame.draw.rect(window, color, self.rect, border_radius = self.border_radius)
        window.blit(text_image, (text_rect.x, text_rect.y))

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.is_hovered = True
                else:
                    self.is_hovered = False 

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False    
    
    pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((100, 100, 255))
clock = pygame.time.Clock()

btn = Button(y=70, width=150, height=50, text='Начать игру', font_size=25 )
if __name__ == '__main__':
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        
        btn.update(events)
        if btn.is_clicked(events):
            print('НАЖАТО!')
        btn.draw(window)

        clock.tick(60)
        pygame.display.update()