highway_number = int(input())

''' Type your code here. '''
if (highway_number < 1) or (highway_number > 999):
    print('%d is not a valid interstate highway number.' % highway_number)
elif (highway_number > 0) and (highway_number < 100):
    if (highway_number % 2 == 0):
        print('The %d is primary, going east/west.' % highway_number)
    else:
        print('The %d is primary, going north/south.' % highway_number)
elif (highway_number > 99) and (highway_number < 1000):
    if (highway_number % 2 == 0):
        print('The %d is auxiliary, serving the %d, going east/west.' % (highway_number, (highway_number%100)))
    else:
        print('The %d is auxiliary, serving the %d, going north/south.' % (highway_number, (highway_number%100)))
