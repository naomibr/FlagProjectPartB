import random

import pygame

import consts


def init_screen():
    main_screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("The Flag")
    return main_screen


def load_images():

    images = {}

    soldier_img = pygame.image.load(consts.SOLDIER_IMAGE).convert_alpha()
    images['soldier'] = pygame.transform.scale(
        soldier_img,
        (consts.SOLDIER_WIDTH_CELLS * consts.CELL_WIDTH,
         consts.SOLDIER_HEIGHT_CELLS * consts.CELL_HEIGHT))

    flag_img = pygame.image.load(consts.FLAG_IMAGE).convert_alpha()
    images['flag'] = pygame.transform.scale(
        flag_img,
        (consts.FLAG_WIDTH_CELLS * consts.CELL_WIDTH,
         consts.FLAG_HEIGHT_CELLS * consts.CELL_HEIGHT))

    mine_img = pygame.image.load(consts.MINE_IMAGE).convert_alpha()
    images['mine'] = pygame.transform.scale(
        mine_img,
        (consts.MINE_WIDTH_CELLS * consts.CELL_WIDTH,
         consts.MINE_HEIGHT_CELLS * consts.CELL_HEIGHT))

    grass_img = pygame.image.load(consts.GRASS_IMAGE).convert_alpha()
    images['grass'] = pygame.transform.scale(
        grass_img, (2 * consts.CELL_WIDTH, 2 * consts.CELL_HEIGHT))

    return images


def set_grass_locations():

    grass_locations = []
    while len(grass_locations) < consts.GRASS_NUM:
        row = random.randint(0, consts.ROWS_NUM - 1)
        col = random.randint(0, consts.COLS_NUM - 1)
        location = (row, col)
        if location in grass_locations:
            continue
        grass_locations.append(location)
    return grass_locations


def to_pixels(location):
    row, col = location
    return col * consts.CELL_WIDTH, row * consts.CELL_HEIGHT


def draw_background(main_screen):
    main_screen.fill(consts.BACKGROUND_COLOR)


def draw_grass(main_screen, grass_locations, images):
    for location in grass_locations:
        main_screen.blit(images['grass'], to_pixels(location))


def draw_soldier(main_screen, soldier_location, images):
    main_screen.blit(images['soldier'], to_pixels(soldier_location))


def draw_flag(main_screen, flag_location, images):
    main_screen.blit(images['flag'], to_pixels(flag_location))


def draw_mines(main_screen, mines_locations, images):
    for location in mines_locations:
        main_screen.blit(images['mine'], to_pixels(location))


def draw_grid(main_screen):

    for col in range(consts.COLS_NUM + 1):
        x = col * consts.CELL_WIDTH
        pygame.draw.line(main_screen, consts.GRID_COLOR, (x, 0), (x, consts.WINDOW_HEIGHT))
    for row in range(consts.ROWS_NUM + 1):
        y = row * consts.CELL_HEIGHT
        pygame.draw.line(main_screen, consts.GRID_COLOR, (0, y), (consts.WINDOW_WIDTH, y))


def draw_message(main_screen, message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    x, y = location
    for line in message.split('\n'):
        text_img = font.render(line, True, color)
        main_screen.blit(text_img, (int(x), int(y)))
        y += font_size


def draw_start_message(main_screen):
    draw_message(main_screen, consts.START_MESSAGE, consts.START_FONT_SIZE,
                 consts.START_MESSAGE_COLOR, consts.START_MESSAGE_LOCATION)


def draw_win_message(main_screen):
    draw_message(main_screen, consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_lose_message(main_screen):
    draw_message(main_screen, consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
