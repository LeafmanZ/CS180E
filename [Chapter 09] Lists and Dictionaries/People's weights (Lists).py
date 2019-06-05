# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.
weights = []
weights.append(float(input('Enter weight 1:\n')))
weights.append(float(input('Enter weight 2:\n')))
weights.append(float(input('Enter weight 3:\n')))
weights.append(float(input('Enter weight 4:\n')))
print('Weights:', weights)

# FIXME (2): Output average of weights.
print('\nAverage weight: %.2f'% (sum(weights)/len(weights)))


# FIXME (3): Output max weight from list.
print('Max weight: %.2f'% max(weights))

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
location = int(input('\nEnter a list location (1 - 4):\n')) - 1
# FIXME (5): Sort the list and output it.
print('Weight in pounds: %.2f' % weights[location])
print('Weight in kilograms: %.2f\n' % (round(weights[location] * 0.453592)))
print('Sorted list:',sorted(weights))
