''' Type your code here. '''
phrase_d = input()
phrase = input()

pairs = {}
phrase_d_words = phrase_d.split()
for i in range(0,(len(phrase_d_words) - 1),2):
    pairs[phrase_d_words[i]] = phrase_d_words[i+1]

for key in pairs.keys():
    phrase = phrase.replace(key, pairs[key])

print(phrase)

