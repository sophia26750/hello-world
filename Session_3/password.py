from re import A


def is_password_long_enough (password):
    if len(password) >= 8:
        return 'Good password!' 
    else:
        return 'Your password needs to be at least eight characters long. '


def main():
    while password != 'Good password!': 
        password = input('What is your password? ')
        print(is_password_long_enough(password))

main()