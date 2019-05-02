from pygame import *

screen = display.set_mode((600,600))
running = True
font.init()
f = font.SysFont('Arial', 30)
mixer.init()
sound = mixer.Sound("chaching.wav")

cookie_pos = (300,300)

cookies = [transform.smoothscale(image.load("cookie_up.png"), (300,300)),
           transform.smoothscale(image.load("cookie_down.png"), (300,300))
]

score = 0
start = time.get_ticks()
clock = time.Clock()
while running:
    screen.fill(0)
    clock.tick(60)
    pressed = False
    for e in event.get():
        if e.type ==QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            x, y = e.pos
            if 150 <= x <= 450:
                if 150 <= y <= 450:
                    if 30 - seconds > 0:
                        pressed = True
                        sound.play()
                        score += 1
    if pressed:
        screen.blit(cookies[1], (150, 150))
    else:
        screen.blit(cookies[0], (150, 150))
    seconds = (time.get_ticks() - start) // 1000

    time_text = f.render("Time: " + str(30 - seconds), False, (255,255,255))
    score_text = f.render("Score: " + str(score), False, (255,255,255))
    if 30 - seconds <= 0:
        time_text = f.render("Time: " + str(0), False, (255,255,255))
       
    screen.blit(score_text, (0,0))
    screen.blit(time_text, (200,0))

    display.flip()
quit()



