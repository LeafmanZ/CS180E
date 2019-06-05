''' Type your code here. '''
string_1 = input()
num_1 = list(map(int,string_1.split()))
string_2 = input()
num_2 = list(map(int,string_2.split()))


for n in num_1:
    if (num_2[0] <= n <= num_2[1]):
        print(n, end = ' ')
