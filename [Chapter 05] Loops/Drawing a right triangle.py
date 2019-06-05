triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n\n'))

for i in range(triangle_height, 0, -1):
    for j in range(triangle_height - i + 1,):
        print(triangle_char, end = ' ')
    print()
