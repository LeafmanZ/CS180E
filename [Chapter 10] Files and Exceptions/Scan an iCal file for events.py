"""Scan an iCal file for events."""

def main():
    filename = input()
    file = open(filename)
    lines = file.readlines()
    file.close()
    
    event_begun = False
    summary_happened = False
    dt_happened = False
    summary = ''
    dt = ''
    for l in lines:
        line = l.split(':',1)
        if line[0] == 'BEGIN':
            event_begun = True

        if line[0] == 'SUMMARY' and event_begun:
            summary = line[1]
        if line[0] == 'DTSTART' and event_begun:
            dt = line[1]
        if line[0] == 'DTSTART;VALUE=DATE' and event_begun:
            dt = l.split(';')[-1]
        if line[0] == 'END' and event_begun:
            event_begun = False
            print(summary,end='')
            print(dt,end='')
            
if __name__ == "__main__":
    main()

