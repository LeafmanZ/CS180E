''' Type your code here. '''
name = input()
name_part = name.split()
name_no_space = ''.join(name_part)
if name_no_space != name_no_space[::-1]:
    print('%s is not a palindrome' % name)
else:
    print('%s is a palindrome' % name)
