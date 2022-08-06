def main():
    var_string = input('please enter a string: ')
    repeat = int(input('How many times to repeat? '))
    result = string_repeater(var_string, repeat)
    print(result)

def string_repeater(text, n):
    repeated_string = text * n
    return repeated_string

main()