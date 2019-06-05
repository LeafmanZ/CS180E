''' Type your code here. '''
data = input()
strings = data.split()
numbers = list(map(int, strings))
print('%d %d'%(sum(numbers)/len(numbers), max(numbers)))

