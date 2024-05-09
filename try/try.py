import pygame
import pygame as pg


pg.init()
screen = pg.display.set_mode((400, 400))
clock = pg.time.Clock()

black_circle_surface = pg.Surface((100, 100), pg.SRCALPHA)
pg.draw.circle(black_circle_surface, (0, 0, 0), (50, 50), 25)
black_circle_surface = pg.transform.gaussian_blur(
    black_circle_surface, radius=10
)  # no need to pre-multiply as colour is zeros will not change whatever we multiply it by

white_circle_surface = pg.Surface((100, 100), pg.SRCALPHA)
white_circle_surface.fill(
    (0, 0, 0, 0)
)  # no need to pre-multiply, alpha is zero and colour is zero
pg.draw.circle(
    white_circle_surface, (255, 255, 255), (50, 50), 25
)  # no need to pre-multiply alpha and colour are the same (either 0 or 255)

circle_and_shadow_surface = pg.Surface((100, 100), pg.SRCALPHA)
circle_and_shadow_surface.fill((0, 0, 0, 0))  # no need to pre-multiply alpha is zero
circle_and_shadow_surface.blit(black_circle_surface, (0, 0))
circle_and_shadow_surface.blit(white_circle_surface, (0, 0))

semi_transparent_surface = pg.Surface((200, 200), pg.SRCALPHA)
semi_transparent_surface.fill(
    (255, 255, 255, 1)  # change the 1 to a 0 here to make the issue disappear
)
semi_transparent_surface = (
    semi_transparent_surface.convert_alpha().premul_alpha()
)  # need to pre-multiply RGB values will all be changed to 1
semi_transparent_surface.blit(
    circle_and_shadow_surface, (50, 50), special_flags=pygame.BLEND_PREMULTIPLIED
)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((20, 70, 80))

    screen.blit(
        semi_transparent_surface, (100, 100), special_flags=pygame.BLEND_PREMULTIPLIED
    )

    pg.display.update()
    clock.tick(60)
