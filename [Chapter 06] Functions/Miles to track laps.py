''' Define your function here '''
def miles_to_laps(user_miles):
    return user_miles/.25

if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    laps = float(input())
    print('%.2f' % miles_to_laps(laps))
