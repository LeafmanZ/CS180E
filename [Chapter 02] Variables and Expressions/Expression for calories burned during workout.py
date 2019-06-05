''' Men: Calories = ((Age x 0.2017) - (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''
''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''

''' Type your code here. '''
years = float(input())
pounds = float(input())
heart_rate = float(input())
time = float(input())
print('Men: %0.2f calories' % (((years*0.2017)-(pounds*0.09036)+(heart_rate*0.6309)-55.0969)*(time/4.184)))
print('Women: %0.2f calories' % (((years*0.074)-(pounds*0.05741)+(heart_rate*0.4472)-20.4022)*(time/4.184)))