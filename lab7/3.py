import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
x = 25
y = 25
delta = 20
done = True
FPS = 60
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if x == 25:
            pass
        else:
            x -= delta
    if pressed[pygame.K_RIGHT]:
        if x >= 475:
            continue
        else:
            x += delta
    if pressed[pygame.K_UP]:
        if y == 25:
            pass
        else:
            y -= delta
    if pressed[pygame.K_DOWN]:
        if y >= 475:
            continue
        else:
            y += delta
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 20)
    pygame.display.flip()
    clock.tick(FPS)