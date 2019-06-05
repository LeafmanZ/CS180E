import math

''' Define your function here. '''
def max_magnitude(user_val1, user_val2):
    if abs(user_val1) >= abs(user_val2):
        return user_val1
    else:
        return user_val2

if __name__ == '__main__':
    ''' Type your code here. '''
    val1 = int(input())
    val2 = int(input())
    print(max_magnitude(val1, val2))
    
