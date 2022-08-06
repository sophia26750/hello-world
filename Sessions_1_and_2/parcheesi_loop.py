import random

number_of_dice = 2
want_to_quit = ''
doubles = 0
snake_eye_count = 0
line = ''
underline = '________________________________________________'
snake_eye_line = '***'
print(line)

game_counter = int()

while True:
    game_counter = game_counter + 1
    print(f'roll counter: {game_counter}')
    print(line)
    print('Please press enter to roll your two dices. ')
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
            print('YOU AUTOMATICALLY WIN!!!')
            print(underline)
            doubles = 0
            print(game_counter)
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

        else:
            print(f'You rolled {doubles} doubles. You get another roll. ')
            print(underline)
            print(line)

    else:
        print('Next player\'s turn')
        print(underline)
        print(line)
        doubles = 0
        snake_eye_count = 0
