''' Type your code here. '''
char_to_check = input()
phrase = input()
words = phrase.split()
for word in words:
    if char_to_check in word:
        print(word)
