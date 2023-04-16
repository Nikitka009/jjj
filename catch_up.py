from pygame import *

window = display.set_mode((700, 500))
FPS = 120
clock = time.Clock()
display.set_caption('Крысенышь')
background = transform.scale(image.load('background.png'), (700, 500))
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

run = True
speed = 10
x1, y1 = 100, 250
x2, y2 = 500, 250

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            run = False
    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x2 > 0:
        x2 -= speed
    if key_pressed[K_RIGHT] and x2 < 595:
        x2 += speed
    if key_pressed[K_UP] and y2 > 0:
        y2 -= speed
    if key_pressed[K_DOWN] and y2 < 385:
        y2 += speed

    if key_pressed[K_a] and x1 > 0:
        x1 -= speed
    if key_pressed[K_d] and x1 < 595:
        x1 += speed
    if key_pressed[K_w] and y1 > 0:
        y1 -= speed
    if key_pressed[K_s] and y1 < 385:
        y1 += speed
    display.update()
    clock.tick(FPS)