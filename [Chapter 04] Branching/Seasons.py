input_month = input()
input_day = int(input())
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

''' Type your code here. '''
if not input_month in months:
    print('invalid')

if (input_month == 'September') and (input_day > 30):
    input_month = ''
    print('invalid')

if (input_month == 'February') and (input_day > 28):
    input_month = ''
    print('invalid')
    
if input_day < 1:
    input_month = ''
    print('invalid')
    
if ((input_month == 'March') and (input_day > 19)) or (input_month == 'April') or (input_month == 'May') or ((input_month == 'June') and (input_day < 21)):
    print('spring')
    
if ((input_month == 'June') and (input_day > 20)) or (input_month == 'July') or (input_month == 'August') or ((input_month == 'September') and (input_day < 22)):
    print('summer')
    
if ((input_month == 'September') and (input_day > 21)) or (input_month == 'October') or (input_month == 'November') or ((input_month == 'December') and (input_day < 21)):
    print('autumn')
    
if ((input_month == 'December') and (input_day > 20)) or (input_month == 'January') or (input_month == 'February') or ((input_month == 'March') and (input_day < 20)):
    print('winter')
