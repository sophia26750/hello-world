# pennies = int(input('How many pennies do you have? '))
#
# if pennies == 100:
#     print('You have exactly one dollar.')
# elif pennies >= 100:
#     print('You have more than one dollar.')
# else:
#     print('You have less than a dollar.')


what_state_run = input('What state do you want to be a senator in? ')
age = int(input('What is your current age? '))
citizen = input('Have you been a citizen in the US for at least the past nine years? ')
state_they_live_in = input('What state do you currently live in? ')

if what_state_run == state_they_live_in and age >= 30 and citizen == 'yes':
    print('You can run for senator!')
else:
    print(''
          'You cannot run for senator.')
