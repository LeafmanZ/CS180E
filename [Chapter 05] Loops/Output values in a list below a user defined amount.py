''' Type your code here. '''
num_inputs = int(input())
numbers = []
for i in range(0, num_inputs):
    number = int(input())
    numbers.append(number)
max = int(input())
for i in numbers:
    if(i <= max):
        print(i)

