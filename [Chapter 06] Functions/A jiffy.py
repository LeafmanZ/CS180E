def seconds_to_jiffies(user_seconds):
    return user_seconds * 100.0
    
if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    print('%.2f' % seconds_to_jiffies(float(input())))
