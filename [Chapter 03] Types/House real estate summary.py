current_price = int(input())
last_months_price = int(input())

''' Type your code here. '''
print('This house is $%d. The change is $%d since last month.' % (current_price, (current_price - last_months_price)))
print('The estimated monthly mortgage is $%.2f.' % ((current_price * .045 / 12)))