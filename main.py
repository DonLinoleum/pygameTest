import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Ля ля ля")

clock = pygame.time.Clock()

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"


class Shell:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
    else:
        win.blit(playerStand, (x, y))

    for shell in shells:
        shell.draw(win)

    animCount += 1
    pygame.display.flip()


walkRight = [pygame.image.load('img/pygame_right_1.png'), pygame.image.load('img/pygame_right_2.png'),
             pygame.image.load('img/pygame_right_3.png'),
             pygame.image.load('img/pygame_right_4.png'), pygame.image.load('img/pygame_right_5.png'),
             pygame.image.load('img/pygame_right_6.png')]

walkLeft = [pygame.image.load('img/pygame_left_1.png'), pygame.image.load('img/pygame_left_2.png'),
            pygame.image.load('img/pygame_left_3.png'),
            pygame.image.load('img/pygame_left_4.png'), pygame.image.load('img/pygame_left_5.png'),
            pygame.image.load('img/pygame_left_6.png')]

playerStand = pygame.image.load('img/pygame_idle.png')
bg = pygame.image.load('img/pygame_bg.jpg')

run = True
shells = []
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for shell in shells:
        if 500 > shell.x > 0:
            shell.x += shell.vel
        else:
            shells.pop(shells.index(shell))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] is not False and x > 5:
        x = x - speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] is not False and x < 500 - width - 5:
        x = x + speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0

    if not isJump:
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

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(shells) < 5:
            shells.append(Shell(round(x+width // 2), round(y+height // 2), 5, (255, 0, 0), facing))

    drawWindow()
