''' Define your function here '''
def is_list_even(my_list):
    for num in my_list:
        if num%2 != 0:
            return False
    return True

def is_list_odd(my_list):
    for num in my_list:
        if num%2 == 0:
            return False
    return True


if __name__ == '__main__':
    ''' Type your code here. '''
    num = int(input())
    my_list = []
    
    for i in range (0,num):
        my_list.append(int(input()))
    
    if is_list_even(my_list):
        print('all even')
    elif is_list_odd(my_list):
        print('all odd')
    else:
        print('not even or odd')
