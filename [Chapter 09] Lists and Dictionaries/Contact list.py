''' Type your code here. '''
phrase = input()
person = input()
directory = {}
names = phrase.split()
for i in range(len(names)-1):
    directory[names[i]] = names[i+1]
    i += 1
print(directory[person])
