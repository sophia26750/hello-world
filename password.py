# secret_password = 'kittens' # Super top secret password
# password = input('Enter the secret password: ')
#
# if password == secret_password:
#     print('Welcome, authorized user')
# else:
#     print('Sorry, wrong password.')
#
# read_syllabus = input('Enter Y if you read the syllabus for the class: ')
#
# if read_syllabus != 'Y':
#     print('Please read the syllabus carefully, there is important info in it. Thanks! ')
# else:
#     print('Great Job!')

star_id = input('Please enter your StarID: ')

if len(star_id) == 8:
    print('Your StarID is perfect! ')
elif len(star_id) > 8:
    print('Your StarId is too long')
else:
    print('Your StarID is too short.')


