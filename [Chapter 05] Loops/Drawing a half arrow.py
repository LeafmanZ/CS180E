arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))

print('')
# Draw arrow base (height = 3, width = 2)
for i in range (0,arrow_base_height):
    for j in range (0,arrow_base_width):
        print('*', end = '')
    print()
for i in range (0, arrow_head_width):
    for j in range (arrow_head_width - i, 0, -1):
        print('*',end = '')
    print()
# Draw arrow head (width = 4)


