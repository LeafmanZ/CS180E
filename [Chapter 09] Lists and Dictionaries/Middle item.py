''' Type your code here. '''
string = input()
numbers = list(map(int, string.split()))
if len(numbers) > 9:
    print('Too many inputs')
else:
    print(numbers[len(numbers)//2])
