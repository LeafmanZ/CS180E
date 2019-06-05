# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pet_name = input('Enter pet\'s name:\n')
number = input('Enter a number:\n')
print('You entered: %s %s %s' % (favorite_color, pet_name, number))

# FIXME (2): Output two password options
password1 = favorite_color + '_' + pet_name
password2 = number + favorite_color + number
print('\nFirst password:', password1)
print('Second password:', password2)

# FIXME (3): Output the length of the two password options
print('\nNumber of characters in %s: %d' % (password1,len(password1)))
print('Number of characters in %s: %d' % (password2,len(password2)))