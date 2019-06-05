''' Type your code here. '''
change = int(input())

if change == 0:
    print('no change')
if change >= 100:
    if (change//100 > 1):
        print('%d dollars' % (change//100))
    else:
        print('1 dollar')
    change = change % 100
if change >= 25:
    if (change//25 > 1):
        print('%d quarters' % (change//25))
    else:
        print('1 quarter')
    change = change % 25
if change >= 10:
    if (change//10 > 1):
        print('%d dimes' % (change//10))
    else:
        print('1 dime')
    change = change % 10
if change >= 5:
    if (change//5 > 1):
        print('%d nickels' % (change//5))
    else:
        print('1 nickel')
    change = change % 5
if change >= 1:
    if (change//1 > 1):
        print('%d pennies' % (change//1))
    else:
        print('1 penny')

