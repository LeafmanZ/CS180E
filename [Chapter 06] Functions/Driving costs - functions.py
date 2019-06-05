''' Define your function here. '''
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    return driven_miles * (1/miles_per_gallon) * dollars_per_gallon
    
if __name__ == '__main__':
    ''' Type your code here. '''
    miles = [10, 50, 400]
    mpg = float(input())
    dpg = float(input())
    for m in miles:
        print('%.2f' % driving_cost(m, mpg, dpg))


