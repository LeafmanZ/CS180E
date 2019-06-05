"""Count words in a text file."""

def main():
    filename = input()
    file = open(filename)
    lines = file.readlines()
    file.close()
    words = {}
    for l in lines:
        l_no_punct = l.replace(',','')
        l_no_punct = l_no_punct.replace('.','')
        l_words = l_no_punct.lower().split()
        for w in l_words:
            if w in words.keys():
                words[w] = words[w] + 1
            else:
                words[w] = 1

    for key in sorted(words.keys()):
        print(key, words[key])
        
if __name__ == "__main__":
    main()

