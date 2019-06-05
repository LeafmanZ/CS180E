"""Print a file's longest line."""

def main():
    filename = input()
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    location = 0
    for i in range(len(lines)):
        if len(lines[i]) > len(lines[location]):
            location = i
    print(lines[location], end = '')
    print(location+1)

if __name__ == "__main__":
    main()

