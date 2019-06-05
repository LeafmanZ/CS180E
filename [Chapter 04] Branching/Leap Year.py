is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if (input_year%100 == 0) and (input_year%400 == 0):
    is_leap_year == True
    print('%d is a leap year.' % input_year)
elif (input_year%100 != 0) and (input_year%4 == 0):
    is_leap_year == True
    print('%d is a leap year.' % input_year)
else:
    is_leap_year == False
    print('%d is not a leap year.' % input_year)