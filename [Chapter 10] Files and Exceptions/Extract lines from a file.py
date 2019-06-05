"""Extract lines from a file."""

def main():
    filename = input()
    start = int(input())
    end = int(input())
    
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    for i in range(start-1, end):
        print(lines[i],end ='')

if __name__ == "__main__":
    main()

