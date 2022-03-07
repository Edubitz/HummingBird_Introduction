'''
Problem #4:
Turn all three LEDs on at 100 intensity for 2 seconds, 
turn the second LED to 75 intensity for 3 seconds, 
turn the first and third LEDs off for 4 seconds, 
and lastly turn everything off.
'''

from BirdBrain import Hummingbird 

bird = Hummingbird('A') 

# Turn LED 1, 2, and 3 all to 100 intensity
bird.setLED(1, 100)
bird.setLED(2, 100)
bird.setLED(3, 100)

time.sleep(2) # Wait for 2 seconds

bird.setLED(2, 75)

time.sleep(3) # Wait for 3 seconds

# Turn LED 1 and 3 all to 0 (off)
bird.setLED(1, 0)
bird.setLED(3, 0)

time.sleep(4) # Wait for 4 seconds

bird.setLED(2, 0) # Turn LED 2 off

bird.stopAll() 