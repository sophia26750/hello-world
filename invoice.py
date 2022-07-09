item_name = input('Enter the name of your item: ')
item_price = float(input('Enter the price of the ' + item_name +': $'))
items_quantity = int(input('Enter the quantity of your item: '))

total_price = item_price * items_quantity
format_total_price = "{:.2f}".format(total_price)

print(''
      '')
print(item_name + ' sales')
print('Quantity bought: ' + str(items_quantity))
print('The price of the ' + item_name + ': $' + str(item_price))
print('Total: $' + format_total_price)




