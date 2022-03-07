#  Problem #1: Make it so your LED waits for 10 second

from BirdBrain import Hummingbird 

bird = Hummingbird('A') 

bird.setLED(1, 100) # Turn the LED at port 1 of the HummingBird to 100 intensity
time.sleep(10) # Wait for 10 seconds

bird.stopAll() 
