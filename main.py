def grid(turn):
    global symbols

    symbols = [[first_cell[i], second_cell[i]]
               if symbols[i] == ' ' else symbols[i] for i in range(9)]

    if move in symbols:
        symbols = [i if i != move else turn for i in symbols]

    symbols = [i if i == 'X' or i == 'O' else ' ' for i in symbols]

    print('---------')
    print('|', symbols[0], symbols[1], symbols[2], '|')
    print('|', symbols[3], symbols[4], symbols[5], '|')
    print('|', symbols[6], symbols[7], symbols[8], '|')
    print('---------')


def game_state():
    check = [symbols[0:3], symbols[3:6], symbols[6:9], symbols[0:7:3],
             symbols[1:8:3], symbols[2:9:3], symbols[0:9:4], symbols[2:7:2]]

    empty_cells = 'YES' if ' ' in symbols else 'NO'

    if ['X', 'X', 'X'] not in check and ['O', 'O', 'O'] not in check \
            and empty_cells == 'NO':
        print('Draw')
        return False
    elif ['X', 'X', 'X'] in check:
        print('X wins')
        return False
    elif ['O', 'O', 'O'] in check:
        print('O wins')
        return False


def user_move():
    global move

    numbers = [str(i) for i in range(10)]

    cell_coordinates = [[first_cell[i], second_cell[i]] for i in range(9)
                        if symbols[i] != ' ']

    while True:
        move = input('Enter the coordinates: ').split()

        if move[0] not in numbers or move[1] not in numbers:
            print('You should enter numbers!')
        elif move[0] not in numbers[1:4] or move[1] not in numbers[1:4]:
            print('Coordinates should be from 1 to 3!')
        elif move in cell_coordinates:
            print('This cell is occupied! Choose another one!')
        else:
            cell_coordinates += [move]
            break


first_cell = ['1', '1', '1', '2', '2', '2', '3', '3', '3']
second_cell = ['1', '2', '3', '1', '2', '3', '1', '2', '3']

symbols = '         '
move = str()

grid(' ')

for position in ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']:
    user_move()
    grid(position)
    if game_state() is False:
        break
