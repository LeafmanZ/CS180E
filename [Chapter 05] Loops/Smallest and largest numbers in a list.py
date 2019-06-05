''' Type your code here. '''
num = int(input())
maximum = num
minimum = num
while num > 0:
    if(num >= maximum):
        maximum = num
    elif(num <= minimum):
        minimum = num
    num = int(input())
print(minimum, maximum)
