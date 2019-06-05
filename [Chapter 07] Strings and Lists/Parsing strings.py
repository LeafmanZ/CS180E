# Type your code here
name = input('Enter input string:\n')
while name != 'q':
    
    if ',' in name:
        name = name.replace(' ', '')
        words = name.split(',')
        print('First word:', words[0])
        print('Second word:', words[1] + '\n')
    else:
        print('Error: No comma in string.\n')
        
    name = input('Enter input string:\n')
