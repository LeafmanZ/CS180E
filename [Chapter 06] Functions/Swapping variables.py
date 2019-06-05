''' Define your function here. '''
def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__': 
    ''' Type your code here. Your code must call the function. '''
    val1 = int(input())
    val2 = int(input())
    val1, val2 = swap_values(val1, val2)

    print(val1, val2)
