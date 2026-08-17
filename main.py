import pygame

import consts
import game_field
import Screen
import soldier


def create_game_state():
    return {
        'is_window_open': True,
        'landmines_visible': False,
        'landmines_shown_at': 0,
        'game_over': False,
        'is_win': False,
        'end_time': 0,
    }


def manage_events(state, soldier_location):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['is_window_open'] = False

        elif event.type == pygame.KEYDOWN:
            if not state['landmines_visible'] and not state['game_over']:
                if event.key == pygame.K_LEFT:
                    soldier_location = soldier.soldier_move_left(soldier_location)
                elif event.key == pygame.K_RIGHT:
                    soldier_location = soldier.soldier_move_right(soldier_location)
                elif event.key == pygame.K_UP:
                    soldier_location = soldier.soldier_move_up(soldier_location)
                elif event.key == pygame.K_DOWN:
                    soldier_location = soldier.soldier_move_down(soldier_location)
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    state['landmines_visible'] = True
                    state['landmines_shown_at'] = pygame.time.get_ticks()

    return soldier_location


def update_landmines_visibility(state):

    if state['landmines_visible']:
        elapsed_seconds = (pygame.time.get_ticks() - state['landmines_shown_at']) / 1000
        if elapsed_seconds >= consts.LANDSMINES_EXPOSE_DURATION:
            state['landmines_visible'] = False


def check_game_end(state, board, soldier_location):

    legs_cells = soldier.get_soldier_legs_cells(soldier_location)
    body_cells = soldier.get_soldier_body_cells(soldier_location)

    if game_field.is_touching_mine(board, legs_cells):
        state['game_over'] = True
        state['is_win'] = False
        state['end_time'] = pygame.time.get_ticks()
    elif game_field.is_touching_flag(board, body_cells):
        state['game_over'] = True
        state['is_win'] = True
        state['end_time'] = pygame.time.get_ticks()


def update_end_of_game(state):

    if state['game_over']:
        elapsed_seconds = (pygame.time.get_ticks() - state['end_time']) / 1000
        if elapsed_seconds >= consts.END_MESSAGE_DURATION:
            state['is_window_open'] = False


def draw_game(main_screen, images, state, board, soldier_location,
              flag_location, mines_locations, grass_locations):
    if state['landmines_visible']:
        main_screen.fill(consts.MINES_BACKGROUND_COLOR)
        Screen.draw_grid(main_screen)
        Screen.draw_mines(main_screen, mines_locations, images)
    else:
        Screen.draw_background(main_screen)
        Screen.draw_grass(main_screen, grass_locations, images)

    Screen.draw_flag(main_screen, flag_location, images)
    Screen.draw_soldier(main_screen, soldier_location, images)

    if not state['landmines_visible'] and not state['game_over']:
        Screen.draw_start_message(main_screen)

    if state['game_over']:
        if state['is_win']:
            Screen.draw_win_message(main_screen)
        else:
            Screen.draw_lose_message(main_screen)

    pygame.display.update()


def main():
    pygame.init()

    main_screen = Screen.init_screen()
    images = Screen.load_images()

    board = game_field.create_board()
    flag_location = game_field.set_flag_location(board)
    mines_locations = game_field.set_landmines_locations(board)
    grass_locations = Screen.set_grass_locations()
    soldier_location = soldier.create_soldier()

    state = create_game_state()

    while state['is_window_open']:
        soldier_location = manage_events(state, soldier_location)
        update_landmines_visibility(state)

        if not state['game_over']:
            check_game_end(state, board, soldier_location)

        draw_game(main_screen, images, state, board, soldier_location,
                  flag_location, mines_locations, grass_locations)

        update_end_of_game(state)

    pygame.quit()


if __name__ == '__main__':
    main()
