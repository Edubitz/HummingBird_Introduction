#  Problem #2: Turn on the LED at port 2

from BirdBrain import Hummingbird 

bird = Hummingbird('A') 

bird.setLED(2, 100) # Turn the LED at port 2 of the HummingBird to 100 intensity
time.sleep(1) # Wait for 1 second

bird.stopAll() 