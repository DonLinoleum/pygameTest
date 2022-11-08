import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Ля ля ля")

x = 50
y = 435
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] is not False and x > 5:
        x = x - speed
    if keys[pygame.K_RIGHT] is not False and x < 500 - width - 5:
        x = x + speed

    if not(isJump):
        if keys[pygame.K_UP] is not False and y > 5:
            y = y - speed
        if keys[pygame.K_DOWN] is not False and y < 500 - height - 15:
            y = y + speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.flip()
