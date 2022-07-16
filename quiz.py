# print('Quiz program!')
#
# answer = input('What is the capital of Wisconsin? ')
#
# if answer != 'Madison':
#     print('Sorry, the answer was Madison.')
#
# else:
#     print('Correct!')

# if answer != 'Madison':
#     print('Sorry, the answer was Madison')

points = float(input('How many points do you get? '))

while points < 0:
    print('Error - please enter 0 or a positive number.')
    points = int(input('Enter the number of credits you are taking this semester? '))
if points >= 6:
    print('You are a half-time student')
elif points >= 12:
    print('You are a full-time student')
else:
    print('You are less than a half-time')
#
# quiz_score = float(input('Please enter the quiz score, out of 100: '))
# if quiz_score >= 90:
#     print('Your letter grade is an A')
# elif quiz_score >= 80:
#     print('Your letter grade is a B')
# elif quiz_score >= 70:
#     print('Your letter grade is a C')
# elif quiz_score >= 60:
#     print('Your letter grade is a D')
# else:
#     print('Your letter grade is a F')
