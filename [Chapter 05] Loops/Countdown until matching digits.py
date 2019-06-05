''' Type your code here. '''

number = int(input())
if number < 20 or number > 98:
    print('Input must be 20-98')
else:
    while number//10 != number%10:
        print(number)
        number -= 1
    print(number)
    