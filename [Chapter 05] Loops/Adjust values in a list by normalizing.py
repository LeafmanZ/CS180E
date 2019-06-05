''' Type your code here. '''
list_size = int(input())

numbers = []
smol = 0
for i in range (0, list_size):
    number = int(input())
    numbers.append(number)
    
min_num = min(numbers)
new_numbers = [(x-min_num) for x in numbers]
print(*new_numbers, sep = '\n')
