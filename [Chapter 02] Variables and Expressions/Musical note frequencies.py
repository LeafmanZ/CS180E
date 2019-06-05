import math
''' Type your code here. '''
f0 = float(input())
r = math.pow(2,(1/12))
f1 = f0 * r**1
f2 = f0 * r**2
f3 = f0 * r**3
f4 = f0 * r**4

print('%0.2f %0.2f %0.2f %0.2f %0.2f' % (f0, f1, f2, f3, f4))