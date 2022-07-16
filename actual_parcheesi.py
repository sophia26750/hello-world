import random

number_of_dice = 2
want_to_quit = ''
count = 1
snake_eye_count = 1
line = ''
underline = '__________________________________'
# first_player = input("Who's going first? (Type 'Yellow', 'Green', 'Red', or 'Blue': )")
# if first_player == 'Yellow':
#     player_list = ["Yellow, Green, Red, Blue"]
# elif first_player == 'Green':
#     player_list = ["Green, Red, Blue, Yellow"]
# elif first_player == 'Red':
#     player_list = ["Red, Blue, Yellow, Green"]
# elif first_player == 'Blue':
#     player_list = ["Blue, Red, Yellow, Green"]
# yellow = player_list[0]
# green = player_list[1]
# red = player_list[2]
# blue = player_list[3]
print(line)

while not want_to_quit:
    dice_value = random.randint(2, 2)
    dice_value_2 = random.randint(2, 2)

    if dice_value_2 == 1 and dice_value == 1:
        snake_eye_count = snake_eye_count + 1

    if dice_value_2 == dice_value and count != 3:
        want_to_quit = input('Please press enter to roll your two dices. ')
        print(underline)
        print(f'You rolled a {dice_value} and a {dice_value_2}.')
        print('You get another roll! ')
        print(underline)
        print(line)
        count = count + 1

        if snake_eye_count == 3:
            want_to_quit = input('Please press enter to roll your two dices. ')
            print(underline)
            print(f'You rolled a {dice_value} and a {dice_value_2}. ')
            print('YOU AUTOMATICALLY WIN!!!')
            print(underline)
            count = 1
            quit('Game Over!')

            # if snake_eye_count == 3 and count == 1:
            #     # print('Game Over!')
            #     quit('Game Over!')

        if count == 3:
            want_to_quit = input('Please press enter to roll your two dices. ')
            print(line)
            print(underline)
            print(f'You rolled a {dice_value} and a {dice_value_2}. ')
            print('Sorry, return your farthest piece back to home.')
            print(underline)
            print(line)

    else:
        print(line)
        want_to_quit = input('Please press enter to roll your two dices. ')
        print(underline)
        print(f'You rolled a {dice_value} and a {dice_value_2}.')
        print('Next player\'s turn')
        print(underline)
        print(line)
        count = 1
        snake_eye_count = 1

