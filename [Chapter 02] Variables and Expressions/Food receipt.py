item_name = input('Enter food item name:\n')

# FIXME (1): Finish reading item price and quantity, then output a receipt
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n\n'))
item_total1 = item_price * item_quantity
total = 0
total += item_total1
print('RECEIPT')
print('%d %s @ $%.2f = $%.2f' % (item_quantity, item_name, item_price, item_total1))
print('Total cost: $%.2f\n\n' % total)
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
item_name2 = input('Enter second food item name:\n')
item_price2 = float(input('Enter item price:\n'))
item_quantity2 = int(input('Enter item quantity:\n\n'))
item_total2 = item_price2 * item_quantity2
total += item_total2
print('RECEIPT')
print('%d %s @ $%.2f = $%.2f' % (item_quantity, item_name, item_price, item_total1))
print('%d %s @ $%.2f = $%.2f' % (item_quantity2, item_name2, item_price2, item_total2))
print('Total cost: $%.2f' % total)
# FIXME (3): Add a gratuity and total with tip to the second receipt
gratuity = total * .15
print('\n15% gratuity: $', end ='')
print('%.2f'% gratuity)
print("Total with tip: $%.2f" % (total+gratuity))