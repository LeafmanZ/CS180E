''' Type your code here. '''
red = int(input())
green = int(input())
blue = int(input())

scale = 0

if red <= green and red <= blue:
    scale = red
elif green <= red and green <= blue:
    scale = green
else:
    scale = blue

red = red - scale
blue = blue - scale
green = green - scale

print('%d %d %d' % (red, green, blue))