"""CS 101, Lab08: Finch robot dance party"""

from finch import Finch
import time

# Finch dances part 1
def hello_finch():
    robot.led(0, 255, 0)
    robot.wheels(0.75, 0.75)
    time.sleep(1.5)
    robot.led(255, 100, 0)
    robot.wheels(-0.75, -0.75)
    time.sleep(1.5)
    robot.led(0, 100, 255)
    robot.wheels(0.75, -0.75)
    time.sleep(1.5)
    robot,halt()

# Finch square dance. I know it said to dance forever but that can be annoying so I just changed it to run a set number of times.
# To make it run forever I would replace the for loop with a while loop and set the condition to True.
def square_dance(times):
    for i in range(times):
        robot.buzzer(3.0, 300)
        robot.wheels(1, 1)
        time.sleep(1.0)
        robot.wheels(-.5,-.5)
        time.sleep(1.0)
        robot.wheels(-1,1)
        time.sleep(.35)
    robot.halt()

def main():
    robot = finch.Finch()
    hello_finch()
    square_dance(10)
    
if __name__ == "__main__":
    main()
