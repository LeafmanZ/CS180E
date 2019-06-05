''' Type your code here. '''
word = input()
word_part = word.split()
acro = ''
for w in word_part:
    if w[0].isupper():
        acro += w[0]
    
print(acro)
