''' Define your function here. '''
def is_leap_year(user_year):
    if user_year%100 == 0 and user_year%400 == 0:
        return True
    elif user_year%100 != 0 and user_year%4 == 0:
        return True
    return False

if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    year = int(input())
    if is_leap_year(year):
        print(year, 'is a leap year.')
    else:
        print(year, 'is not a leap year.')
