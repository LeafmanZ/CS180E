''' Type your code here. '''
i = input()
i_part = i.split()
while i_part[0] != 'quit':
    print('Eating %s %s a day keeps the doctor away.' % (i_part[1], i_part[0]))
    i = input()
    i_part = i.split()
