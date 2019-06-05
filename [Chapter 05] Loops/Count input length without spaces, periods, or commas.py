user_text = input()

''' Type your code here. '''
count = 0
for i in user_text:
    if (i!=' ') and (i!='.') and (i!=','):
        count+=1
print(count)
    