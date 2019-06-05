''' Type your code here. '''
x1 = int(input())
x2 = int(input())
if (x1 > x2):
    print('Second integer can\'t be less than the first.')
else:
    while x1 <= x2:
        print(x1, end = ' ')
        x1 += 10
    print()