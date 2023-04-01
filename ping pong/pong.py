from pygame import *
import random
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('ping pong')

bc = (144, 200, 150)
window.fill(bc)
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, _image, x=0, y=0, width = 50, height = 50):
        super().__init__() 
        self.image = transform.scale(image.load(_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def __init__(self, _image, x=0, y=0, width = 50, height = 50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(_image, x, y, width, height) 
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= self.speed
        if keys[self.key_down]:
            self.rect.y += self.speed

platform_1 = Player('platform.png', 30, 430, 20, 100)
platform_2 = Player('platform.png', 670, 430, 20, 100, 5, K_UP, K_DOWN)

run = True
while run:
    window.fill(bc)
    for e in event.get():   
        if e.type == QUIT:
            run = False

    platform_1.update()
    platform_1.reset()
    platform_2.update()
    platform_2.reset()
    display.update()
    clock.tick(FPS)