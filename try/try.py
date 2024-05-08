import pygame as pg


pg.init()
screen = pg.display.set_mode((400, 400))
clock = pg.time.Clock()

black_circle_surface = pg.Surface((100, 100), pg.SRCALPHA)
pg.draw.circle(black_circle_surface, (0, 0, 0), (50, 50), 25)

white_circle_surface = pg.Surface((100, 100), pg.SRCALPHA)
pg.draw.circle(white_circle_surface, (255, 255, 255), (50, 50), 25)

circle_and_shadow_surface = pg.Surface((100, 100), pg.SRCALPHA)
circle_and_shadow_surface.blit(
    pg.transform.gaussian_blur(black_circle_surface, radius=10), (0, 0)
)
circle_and_shadow_surface.blit(white_circle_surface, (0, 0))

semi_transparent_surface = pg.Surface((200, 200), pg.SRCALPHA)
semi_transparent_surface.fill(
    (255, 255, 255, 1)  # change the 1 to a 0 here to make the issue disappear
)
semi_transparent_surface.blit(
    circle_and_shadow_surface,
    (50, 50),
)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((20, 70, 80))

    screen.blit(semi_transparent_surface, (100, 100))

    pg.display.update()
    clock.tick(60)