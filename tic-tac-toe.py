from enum import Enum


class Mark(Enum):
    """Used to determine the symbol placed
    on each space on the game board."""
    EMPTY = 1
    CROSS = 2
    CIRCLE = 3


game_board = [[Mark.EMPTY for i in range(3)] for j in range(3)]


def draw_board():
    """Displays the game_board variable as a
    board in the user's terminal"""

    for i in game_board:
        print('\n')
        for j in i:
            match j:
                case Mark.EMPTY:
                    j = ' '
                case Mark.CROSS:
                    j = 'X'
                case Mark.CIRCLE:
                    j = 'O'

            print(f'| {j}', end=' |')

    print('\n')


def sanitize_string(input):
    """Removes all spaces and colons from the user's input so later processes 
    can use it properly."""

    input.strip()

    if ' ' or ',' in input:
        input = input.translate({ord(' '): None, ord(','): None})

    if not input.isdigit() or len(input) > 2:
        print('Invalid input')

    return [int(i) for i in input]


def place_on_board(is_player_one):
    """Allows the player to interact with spaces on the
    game_board object."""

    is_valid_input = False

    while is_valid_input is False:
        selection = input('Please select a square. Coordinates start from 0,0 at the top left and end at 2,2 at the bottom right.')
        coords = sanitize_string(selection)
        print(coords)

        try:
            if game_board[coords[1]][coords[0]] != Mark.EMPTY:
                print("Space is occupied. Try again.")
                continue

        except IndexError:
            print("Out of range. Try again.")
            continue

        if is_player_one is True:
            game_board[coords[1]][coords[0]] = Mark.CROSS
        else:
            game_board[coords[1]][coords[0]] = Mark.CIRCLE

        is_valid_input = True


def check_horizontal_and_vertical():
    """Checks the entire board for a contiguous line of three O's or X's, either horizontal or vertical."""

    for horizontal in range(3):
        first = game_board[0][horizontal]
        second = game_board[1][horizontal]
        third = game_board[2][horizontal]
        row = [first, second, third]

        # If all are equivalent and not empty
        if first == second == third and Mark.EMPTY not in row:
            return True

    for vertical in range(3):
        first = game_board[vertical][0]
        second = game_board[vertical][1]
        third = game_board[vertical][2]
        column  = [first, second, third]

        # If all are equivalent and not empty
        if first == second == third and Mark.EMPTY not in column:
            return True

    return False


def check_for_winners():
    """Checks for a winner, if there is one."""

    # If any horizontal or vertical lines complete the
    # criteria, skip the function
    if check_horizontal_and_vertical() is True:
        return True

    # Coordinates for both diagonals
    top_right = game_board[0][2]
    top_left = game_board[0][0]
    center = game_board[1][1]
    bottom_right = game_board[2][2]
    bottom_left = game_board[2][0]

    first_diagonal = [top_left, center, bottom_right]
    second_diagonal = [bottom_left, center, top_right]

    if top_left == center == bottom_right and Mark.EMPTY not in first_diagonal:
        return True

    if bottom_right == center == top_right and Mark.EMPTY not in second_diagonal:
        return True

    return False


def main():
    is_player_one = True
    has_been_won = False

    while has_been_won is not True:
        draw_board()
        place_on_board(is_player_one)

        if check_for_winners() is True:
            draw_board()

            if is_player_one is True:
                print("Player one wins!")
            else:
                print("Player two wins!")

            has_been_won = True

        # Swap to the other player
        is_player_one ^= True


if __name__ == '__main__':
    main()
