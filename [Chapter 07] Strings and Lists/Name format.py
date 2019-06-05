''' Type your code here. '''
name = input()
name_partitions = name.split()
if len(name_partitions) == 3:
    print('%s, %s %s.' % (name_partitions[-1], name_partitions[0], name_partitions[1][0]))
else:
    print('%s, %s' % (name_partitions[-1],name_partitions[0]))
