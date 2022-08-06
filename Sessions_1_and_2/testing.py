import random

turn = ["Green", "Red", "Blue", "Yellow"]
line = ''
beginning_player = ""
current_player = int()

while beginning_player != 'green' and beginning_player != 'red' and beginning_player != 'yellow' and beginning_player != 'blue':
    beginning_player = input('Please enter either Yellow, Green, Red, or Blue: ')
    beginning_player = beginning_player.lower()

if beginning_player == 'green':
    current_player = 0
if beginning_player == 'red':
    current_player = 1
if beginning_player == 'blue':
    current_player = 2
if beginning_player == 'yellow':
    current_player = 3


number_of_dice = 2
want_to_quit = ''
doubles = 0
snake_eye_count = 0
line = ''
underline = '________________________________________________'
snake_eye_line = '***'
#     player_list = ["Yellow, Green, Red, Blue"]
print(line)
next_player = current_player

while not want_to_quit:
    input(f'{turn[next_player]} you\'re up! Please press enter to roll. ')
    print(line)
    print(underline)
    dice_value = random.randint(1, 6)
    dice_value_2 = random.randint(1, 6)
    print(f'You rolled a {dice_value} and a {dice_value_2}.')

    if dice_value_2 == 1 and dice_value == 1:
        snake_eye_count = snake_eye_count + 1
        doubles = doubles + 1
        print(f'You rolled {snake_eye_count} snake eyes!')
        print(underline)

        if snake_eye_count == 3:
            print(f'Player {turn[next_player]}! YOU AUTOMATICALLY WIN!!!')
            print(underline)
            doubles = 0
            quit('Game Over!')

        if doubles == 3 and snake_eye_count >= 1:
            print(snake_eye_line)
            print('Sorry, return your farthest piece back to home. ')
            print('BUT YOU CAN STILL ROLL FOR A SNAKE EYES. ')
            print(underline)
            print(line)

    elif dice_value_2 == dice_value:
        doubles = doubles + 1
        if doubles >= 3:
            print(f'You rolled {doubles} doubles. ')
            print('Sorry, return your farthest piece back to home.')
            print(underline)
            print(line)
            doubles = 0
            next_player = next_player + 1
            if next_player > 3:
                next_player = 0
            print('******************')

        else:
            print(f'You rolled {doubles} doubles. You get another roll. ')
            print(underline)
            print(line)

    else:
        print(underline)
        print(line)
        doubles = 0
        snake_eye_count = 0
        next_player = next_player + 1
        if next_player > 3:
            next_player = 0
        print('******************')
