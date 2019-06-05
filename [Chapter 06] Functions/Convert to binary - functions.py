''' Define your function here. '''
def integer_to_reverse_binary(integer_value):
    string = ''
    while integer_value > 0:
        string = string + str(integer_value%2)
        integer_value //= 2
    return string

def reverse_string(input_string):
    string = ''
    for i in range(len(input_string)-1, -1, -1):
        string += input_string[i]
    return string


if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    print(reverse_string(integer_to_reverse_binary(int(input()))))
