"""CS 180E LAB: Extending the Finch robot API"""

from finch import Finch
import time


class SmartFinch(Finch):
    """Adds a few more methods to the standard Finch API."""
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def forward(self, delay = 1, speed = 1):
        print('%s is going forward for %.1f seconds at %d%% speed' % (self.name, delay, speed * 100))
        robot.wheels(speed, speed)
        time.sleep(delay)
        
    def reverse(self, delay = 1, speed = 1):
        print('%s is going reverse for %.1f seconds at %d%% speed' % (self.name, delay, speed * 100))
        robot.wheels(-speed, -speed)
        time.sleep(delay)
    
    def right(self, delay = 1, speed = 1):
        print('%s is going right for %.1f seconds at %d%% speed' % (self.name, delay, speed * 100))
        robot.wheels(speed, -speed)
        time.sleep(delay)
        
    def left(self, delay = 1, speed = 1):
        print('%s is going left for %.1f seconds at %d%% speed' % (self.name, delay, speed * 100))
        robot.wheels(-speed, speed)
        time.sleep(delay)
    
    def sperg(self):
        print('%s is spergin out' % self.name)
        self.left(.5,1)
        self.right(.5,1)
        self.reverse(.5,1)
    
    def vibe(self,freq, delay):
        print('%s is vibrating at %d frequency for %.1f seconds' % (self.name, freq, delay))
        robot.buzzer(delay, freq)
        
    def green(self):
        print('%s is green' % self.name)
        robot.led(0, 255, 0)

if __name__ == "__main__":
    robot = SmartFinch("Daisy")
    robot.green()
    robot.vibe(300,3)
    robot.sperg()
    robot.forward()
    robot.reverse()
    robot.right(0.5)
    robot.left(0.5)
    robot.halt()

