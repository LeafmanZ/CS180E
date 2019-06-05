services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7}
# Type your code here
service = input('Enter desired auto service:\n')
print('You entered: %s' % service)
if service in services.keys():
    print('Cost of %s: $%d' % (service.lower(),services[service]))   
else:
    print('Error: Requested service is not recognized')