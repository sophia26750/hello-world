import random

number_of_dice = 2
want_to_quit = ''
doubles = 0
snake_eye_count = 0
line = ''
underline = '________________________________________________'
snake_eye_line = '***'
player_list = ["Yellow", "Green", "Red", "Blue"]

user_input = ""
current_player = int()
print()
print(underline + underline + underline)
print(underline + "Welcome to Parcheesi Dice Roller" + underline)
print(underline + underline + underline)
print()

while user_input != "yellow" and user_input != "green" and user_input != "red" and user_input != "blue":
    user_input = input('Please enter your starting color: ')
    user_input = user_input.lower()

if user_input == "yellow":
    current_player = 0
elif user_input == "green":
    current_player = 1
elif user_input == "red":
    current_player = 2
else:
    current_player = 3

print(line)

while True:

    # print()
    input(f'Player {player_list[current_player]} - Press enter to roll. ')
    # print(underline)
    dice_value = random.randint(1, 6)
    dice_value_2 = random.randint(1, 6)
    print()
    print(f'You rolled a [ {dice_value} ] and a [ {dice_value_2} ].')
    print()

    if dice_value_2 == 1 and dice_value == 1:
        snake_eye_count = snake_eye_count + 1
        doubles = doubles + 1
        print(f'You rolled {snake_eye_count} snake eyes!')
        # print(underline)

        if snake_eye_count == 3:
            print('YOU AUTOMATICALLY WIN!!!')
            print(underline)
            doubles = 0
            quit('Game Over!')

        if doubles == 3 and snake_eye_count >= 1:
            print(snake_eye_line)
            print('Sorry, return your farthest piece back to home. ')
            print('BUT YOU CAN STILL ROLL FOR A SNAKE EYES. ')
            # print(underline)
            # print(line)

    elif dice_value_2 == dice_value:
        doubles = doubles + 1
        if doubles >= 3:
            print(f'You rolled {doubles} doubles. ')
            print('Sorry, return your farthest piece back to home.')
            # print(underline)
            # print(line)
            doubles = 0

        else:
            print(f'You rolled {doubles} doubles. You get another roll. ')
            # print(underline)
            print(line)

    else:
        current_player = current_player + 1
        if current_player == 4:
            # reset current player to zero if number is 4
            current_player = 0
        print(underline)
        print()
        print(f' ****** {player_list[current_player]} player\'s turn ******')

        print(line)
        doubles = 0
        snake_eye_count = 0
