''' Type your code here. '''
s = input()
quit = ["Quit", "quit", "q"]
while not (s in quit):
    for i in range (len(s)-1,-1,-1):
        print(s[i], end = '')
    print()
    s = input()