''' Type your code here. '''
string = input()
numbers = list(map(int, string.split()))
positive = [i for i in numbers if i >= 0]
positive.sort()
for i in positive:
    print(i, end = ' ')
