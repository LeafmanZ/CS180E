# Type your code here
title = input('Enter a title for the data:\n')
print('You entered:', title)
header_1 = input('\nEnter the column 1 header:\n')
print('You entered:', header_1)
header_2 = input('\nEnter the column 2 header:\n')
print('You entered:', header_2)
data_storage = {}

data = input('\nEnter a data point (-1 to stop input):\n')

while(data != '-1'):
    data_spaceless = data.replace(' ','')
    if not(',' in data):
        print('Error: No comma in string.')
    elif data.count(',') > 1:
        print('Error: Too many commas in input.')
    elif not(data_spaceless.split(',')[-1].isdigit()):
        print('Error: Comma not followed by an integer.')
    else:
        datas = data.split(',')
        print('Data string:', datas[0])
        print('Data integer:', datas[1].replace(' ', ''))
        data_storage[datas[0]] = datas[1].replace(' ', '')
        
    data = input('\nEnter a data point (-1 to stop input):\n')

print('\n%33s' % title)
line_new = '{:<20}|{:>23}'.format(header_1, header_2)
print(line_new)
line = '-' * len(line_new)
print(line)
for key in data_storage:
    line_new = '{:<20}|{:>23}'.format(key, data_storage[key])
    print(line_new)
print()

for key in data_storage:
    line_new = '{:>20} {}'.format(key, ( '*' * int(data_storage[key])))
    print(line_new)

