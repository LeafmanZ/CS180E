''' Type your code here. '''
phrase = input()
phrase_part = phrase.split()
num_occ = phrase.count(phrase_part[0])-1
print(num_occ)
