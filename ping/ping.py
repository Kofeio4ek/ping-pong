from pygame import *
import random
from test import Button
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
        if keys[self.key_up] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[self.key_down] and self.rect.y < 395:
            self.rect.y += self.speed

platform_1 = Player('platform.png', 30, 400, 20, 100)
platform_2 = Player('platform.png', 670, 400, 20, 100, 5, K_UP, K_DOWN)
ball = Player('ping.png', 400, 200, 50, 49, 4,)

font.init()
font = font.Font(None, 40)
win_reset = font.render(
    'platform_1-WIN', True, (0,250,0)
)
lost_reset = font.render(
    'platform_2-WIN', True, (0,250,0)
)

btn_start = Button(y=150, width=150, height=40, text="Начать игру", font_size=25)
btn_exit = Button(y=270, width=150, height=40, text="Выйти", font_size=25)
btn_restart = Button(y=250, width=150, height=40, text="Начать заново", font_size=25)
btn_credits = Button(y=210, width=150, height=40, text="Об авторе", font_size=25)
btn_continue = Button(y=220, width=150, height=40, text="Продолжить", font_size=25)
btn_exit_in_pause = Button(y=280, width=150, height=40, text="Выйти", font_size=25)

speed_y = 3
speed_x = 3
finish = False 
run = True

def game_run():
    global speed_x, speed_y
    window.fill(bc)
    platform_1.update()
    platform_2.update()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(ball, platform_1) or sprite.collide_rect(ball, platform_2):
        speed_x *= -1
        speed_y *= 1 
    if ball.rect.y > 500-50 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 650:
        window.blit(win_reset, (200, 200))
    if ball.rect.x < 0:
        window.blit(lost_reset, (200, 200))
    platform_1.update()
    platform_1.reset()
    platform_2.update()
    platform_2.reset()
    ball.reset()

def pause(events):
    window.fill(bc)
    btn_continue.update(events)
    btn_exit_in_pause.update(events)
    btn_continue.draw(window)
    btn_exit_in_pause.draw(window)
    global stage
    if btn_continue.is_clicked(events):
        stage = 'game'
    if btn_exit_in_pause.is_clicked(events):
        stage = 'menu'
def menu(events):
    window.fill(bc)
    btn_start.update(events)
    btn_exit.update(events)
    btn_credits.update(events)
    btn_credits.draw(window)
    btn_exit.draw(window)
    btn_start.draw(window)
    global stage
    if btn_start.is_clicked(events):
        stage = 'game'
    if btn_exit.is_clicked(events):
        stage = 'off'
    if btn_credits.is_clicked(events):
        stage = 'avtor'
stage = 'menu'
while stage != 'off':
    events = event.get()
    window.fill(bc)
    for e in events:   
        if e.type == QUIT:
            stage = 'off'
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause'
    if stage == 'menu':
        menu(events)
    if stage == 'game':
        game_run()
    if stage == 'off':
        QUIT()
    if stage == 'pause':
        pause(events)
    display.update()
    clock.tick(FPS)