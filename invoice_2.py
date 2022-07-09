# name = input('What is your name? ')
# years = str(input('How many years have you been in school? '))
# print(name + ' has been at school for ' + years + ' years')

rode_bus = int(input('How many times have you rode the bus? '))
cost_for_ride = float(input('What is the cost of one bus ride? $'))
total_bus_cost = rode_bus * cost_for_ride
format_float = "{:.2f}".format(total_bus_cost)

print('You rode the bus ' + str(rode_bus) + ' times last month. One bus ride costs $' + str(cost_for_ride) + '. Your total cost was $' + str(format_float))




