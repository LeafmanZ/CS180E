''' Type your code here. '''
phrase = input()
words = phrase.split()
counter = {}
for w in words:
    if w in counter.keys():
        counter[w] += 1
    else:
        counter[w] = 1

for w in words:
    print(w, counter[w])
