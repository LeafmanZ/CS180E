"""File stats (lines, words, chars)."""

def main():
    
    file = open(input())
    lines = file.readlines()
    file.close()
    print(len(lines), 'lines')
    words = 0
    chars = 0
    
    for l in lines:
        words += len(l.split())
        chars += len(l)

    print(words, 'words')
    print(chars, 'chars')

if __name__ == "__main__":
    main()


