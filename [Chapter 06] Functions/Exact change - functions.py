''' Define your function here '''
def exact_change(change):
    
    num_dollars = 0
    num_quarters = 0 
    num_dimes = 0 
    num_nickels = 0
    num_pennies = 0
        
    if change >= 100:
        num_dollars = change//100
        change = change % 100
    if change >= 25:
        num_quarters = change//25
        change = change % 25
    if change >= 10:
        num_dimes = change//10
        change = change % 10
    if change >= 5:
        num_nickels = change//5
        change = change % 5
    if change >= 1:
        num_pennies = change//1
    
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
   

    ''' Type your code here. Your code must call the function. '''

    if num_dollars == num_quarters == num_dimes == num_nickels == num_pennies == 0:
        print('no change')
    if num_dollars > 1:
      print(num_dollars, 'dollars')
    elif num_dollars == 1:
        print(num_dollars, 'dollar')
        
    if num_quarters > 1:
      print(num_quarters, 'quarters')
    elif num_quarters == 1:
        print(num_quarters, 'quarter')
    
    if num_dimes > 1:
      print(num_dimes, 'dimes')
    elif num_dimes == 1:
        print(num_dimes, 'dime')
    
    if num_nickels > 1:
      print(num_nickels, 'nickels')
    elif num_nickels == 1:
        print(num_nickels, 'nickel')
        
    if num_pennies > 1:
      print(num_pennies, 'pennies')
    elif num_nickels == 1:
        print(num_pennies, 'penny')
        
    
