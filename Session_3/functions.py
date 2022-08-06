# example_class_code = 'itec 1234'
# uppercase_class_code = example_class_code.upper()
# print(f'The class code in uppercase is {uppercase_class_code}')

# email = 'MAYBO.PHAM@USBANK.COM'
# lowercase_email = email.lower()
# print(lowercase_email)

# def hello_world():
#     print('Hello World')
# hello_world()
# hello_world()
# hello_world()

def secret_message():
    return 'Top Secret Message'

def print_secret_message():
    get_secret_message = secret_message()
    print(get_secret_message)

def greeting(name):
    message = f'Hello {name}!'
    return message
    #when you call this function you get a vaule back

def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)
    print_secret_message()

main()