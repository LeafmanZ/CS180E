# Type your code here
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
total = 0
print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')
service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n')

print('\nDavy\'s auto shop invoice\n')

if service_1 == '-':
    print('Service 1: No service')
else:
    print('Service 1: %s, $%d' % (service_1, services[service_1]))
    total += services[service_1]

if service_2 == '-':
    print('Service 2: No service')
else:
    print('Service 2: %s, $%d' % (service_2, services[service_2]))
    total += services[service_2]

print('\nTotal: $%d' % total)