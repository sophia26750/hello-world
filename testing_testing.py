turn = ["Green", "Red", "Blue", "Yellow"]
line = ''
beginning_player = input('What color is going first? ')
current_player = int()

while beginning_player == line:
    beginning_player = input('Please enter a color. ')

if beginning_player == 'Green':
    current_player = 0

if beginning_player == 'Red':
    current_player = 1

if beginning_player == 'Blue':
    current_player = 2

if beginning_player == 'Yellow':
    current_player = 3

#Do your turn

next_player = current_player + 1

print(f'player {turn[current_player]} turn.')
enter = input(f'{turn[current_player]} press enter to roll your dice. ')


while True:
    # player does there turn
        next_player = next_player + 1
        if next_player > 3:
            next_player = 0
        hi = input(f'player {turn[next_player]} you\'re up.')
