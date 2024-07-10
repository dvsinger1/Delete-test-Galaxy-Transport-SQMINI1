import pygame

from user import (
    galaxy_x,
    galaxy_y,
    game_name,
    instruction_text,
    success_text,
    ufo_image,
    ufo_speed,
)

# window set up
pygame.init()
window_width = 1050
window_height = 750

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(game_name)

# background
background = pygame.image.load("assets/images/planetary_system.jpg")
background = pygame.transform.scale(background, (window_width, window_height))

# ufo
ufo = pygame.image.load(ufo_image)
ufo_rect = ufo.get_rect()

# galaxy
galaxy = pygame.image.load("assets/images/galaxy.png")
galaxy_rect = galaxy.get_rect()
galaxy_rect.x = galaxy_x
galaxy_rect.y = galaxy_y

# game icon
pygame.display.set_icon(galaxy)

# functions
def text_on_screen_center(text: str, font_path, font_size, color, surface, x_pos, y_pos):
    display_font = pygame.font.Font(font_path, font_size)
    text_render = display_font.render(text, 1, color)
    text_rect = text_render.get_rect(center=(x_pos, y_pos))
    surface.blit(text_render, text_rect)


# game loop
game_running = True

while game_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.blit(background, (0, 0))

    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_LEFT]:
        ufo_rect.x -= ufo_speed
    if key_press[pygame.K_RIGHT]:
        ufo_rect.x += ufo_speed
    if key_press[pygame.K_UP]:
        ufo_rect.y -= ufo_speed
    if key_press[pygame.K_DOWN]:
        ufo_rect.y += ufo_speed

    pygame.time.delay(30)
    screen.blit(ufo, ufo_rect)
    screen.blit(galaxy, galaxy_rect)
    
    text_on_screen_center(instruction_text, 'assets/fonts/CANAVAR.ttf', 30, 'white', screen, window_width / 2, 50)

    # self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    if ufo_rect.colliderect(galaxy_rect):
        text_on_screen_center(success_text, 'assets/fonts/CANAVAR.ttf', 38, 'white', screen, window_width / 2, window_height / 2)

    # your game here:

    # puts work on screen
    pygame.display.flip()

pygame.quit()