#  Problem #3: Wait for 2 seconds and then turn off your LED at port 2

from BirdBrain import Hummingbird 

bird = Hummingbird('A') 

bird.setLED(2, 100) # Turn the LED at port 2 of the HummingBird to 100 intensity
time.sleep(2) # Wait for 2 seconds

bird.stopAll() 